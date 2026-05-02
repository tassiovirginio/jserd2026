use pdf_oxide::converters::ConversionOptions;
use pdf_oxide::PdfDocument;
use rayon::prelude::*;
use serde::Serialize;
use std::fs;
use std::path::{Path, PathBuf};
use std::time::Instant;

/// Representação do conteúdo extraído de uma página
struct PageContent {
    page_number: usize,
    markdown: String,
}

/// Representação completa de um documento PDF extraído
struct PdfExtractedDocument {
    filename: String,
    page_count: usize,
    pages: Vec<PageContent>,
}

/// Resultado do processamento de um PDF
#[derive(Serialize)]
struct ProcessingResult {
    filename: String,
    success: bool,
    pages_extracted: usize,
    duration_ms: u128,
    #[serde(skip_serializing_if = "Option::is_none")]
    error: Option<String>,
}

/// Resumo final da execução
#[derive(Serialize)]
struct Summary {
    total_pdfs: usize,
    successful: usize,
    failed: usize,
    total_pages: usize,
    total_duration_ms: u128,
    results: Vec<ProcessingResult>,
}

fn extract_pdf(pdf_path: &Path, images_output_dir: &Path) -> Result<PdfExtractedDocument, String> {
    let mut doc = PdfDocument::open(pdf_path).map_err(|e| format!("Erro ao abrir PDF: {}", e))?;

    let page_count = doc
        .page_count()
        .map_err(|e| format!("Erro ao obter número de páginas: {}", e))?;

    let options = ConversionOptions {
        detect_headings: true,
        ..Default::default()
    };

    let mut pages = Vec::with_capacity(page_count);

    for page_idx in 0..page_count {
        let markdown = doc
            .to_markdown(page_idx, &options)
            .unwrap_or_else(|e| format!("[Erro ao converter para markdown: {}]", e));

        // Extrai imagens para a pasta dedicada deste PDF se existirem imagens na página
        if let Err(e) = doc.extract_images_to_files(page_idx, images_output_dir, None, None) {
            eprintln!(
                "Aviso: Ocorreu um erro ao extrair as imagens da página {} do pdf {}: {}",
                page_idx + 1,
                pdf_path.display(),
                e
            );
        }

        pages.push(PageContent {
            page_number: page_idx + 1,
            markdown,
        });
    }

    let filename = pdf_path
        .file_name()
        .unwrap_or_default()
        .to_string_lossy()
        .to_string();

    Ok(PdfExtractedDocument {
        filename,
        page_count,
        pages,
    })
}

fn process_single_pdf(pdf_path: &Path, output_base_dir: &Path) -> ProcessingResult {
    let filename = pdf_path
        .file_name()
        .unwrap_or_default()
        .to_string_lossy()
        .to_string();

    let start = Instant::now();

    // Cria diretório próprio para os arquivos deste PDF
    let pdf_name_no_ext = filename.replace(".pdf", "");
    let pdf_output_dir = output_base_dir.join(&pdf_name_no_ext);

    if let Err(e) = fs::create_dir_all(&pdf_output_dir) {
        return ProcessingResult {
            filename,
            success: false,
            pages_extracted: 0,
            duration_ms: start.elapsed().as_millis(),
            error: Some(format!("Erro ao criar diretório do PDF: {}", e)),
        };
    }

    match extract_pdf(pdf_path, &pdf_output_dir) {
        Ok(doc_extracted) => {
            let md_filename = format!("{}.md", pdf_name_no_ext);
            let md_path = pdf_output_dir.join(&md_filename);
            let pages_extracted = doc_extracted.pages.len();

            let mut md_content = String::new();
            for page in &doc_extracted.pages {
                md_content.push_str(&format!("<!-- Página {} -->\n\n", page.page_number));
                md_content.push_str(&page.markdown);
                md_content.push_str("\n\n---\n\n");
            }

            if let Err(e) = fs::write(&md_path, &md_content) {
                return ProcessingResult {
                    filename,
                    success: false,
                    pages_extracted: 0,
                    duration_ms: start.elapsed().as_millis(),
                    error: Some(format!("Erro ao salvar Markdown: {}", e)),
                };
            }

            ProcessingResult {
                filename,
                success: true,
                pages_extracted,
                duration_ms: start.elapsed().as_millis(),
                error: None,
            }
        }
        Err(e) => ProcessingResult {
            filename,
            success: false,
            pages_extracted: 0,
            duration_ms: start.elapsed().as_millis(),
            error: Some(e),
        },
    }
}

fn collect_pdf_files(pdfs_dir: &Path) -> Vec<PathBuf> {
    let mut pdfs: Vec<PathBuf> = fs::read_dir(pdfs_dir)
        .expect("Não foi possível ler o diretório de PDFs")
        .filter_map(|entry| {
            let entry = entry.ok()?;
            let path = entry.path();
            if path.extension().and_then(|e| e.to_str()) == Some("pdf") {
                Some(path)
            } else {
                None
            }
        })
        .collect();

    pdfs.sort();
    pdfs
}

fn main() {
    let total_start = Instant::now();

    // Diretórios relativos à raiz do projeto
    let pdfs_dir = Path::new("../pdfs");
    let output_dir = Path::new("../markdown");

    if !pdfs_dir.exists() {
        eprintln!(
            "❌ Diretório de PDFs não encontrado: {}",
            pdfs_dir.display()
        );
        eprintln!("   Execute a partir da pasta pdf-to-json/");
        std::process::exit(1);
    }

    // Cria diretório de saída
    fs::create_dir_all(output_dir).expect("Não foi possível criar diretório de saída markdown");

    let pdf_files = collect_pdf_files(pdfs_dir);

    if pdf_files.is_empty() {
        eprintln!(
            "⚠️  Nenhum arquivo PDF encontrado em {}",
            pdfs_dir.display()
        );
        std::process::exit(0);
    }

    println!("📄 Encontrados {} PDFs para processar", pdf_files.len());
    println!("📂 Saída em: {}/", output_dir.display());
    println!("─────────────────────────────────────────");

    // Processa PDFs em paralelo usando rayon
    let results: Vec<ProcessingResult> = pdf_files
        .par_iter()
        .map(|pdf_path| {
            let result = process_single_pdf(pdf_path, output_dir);
            if result.success {
                println!(
                    "  ✅ {} ({} páginas, {}ms)",
                    result.filename, result.pages_extracted, result.duration_ms
                );
            } else {
                println!(
                    "  ❌ {} - {}",
                    result.filename,
                    result.error.as_deref().unwrap_or("Erro desconhecido")
                );
            }
            result
        })
        .collect();

    let successful = results.iter().filter(|r| r.success).count();
    let failed = results.iter().filter(|r| !r.success).count();
    let total_pages: usize = results.iter().map(|r| r.pages_extracted).sum();

    let summary = Summary {
        total_pdfs: pdf_files.len(),
        successful,
        failed,
        total_pages,
        total_duration_ms: total_start.elapsed().as_millis(),
        results,
    };

    // Salva resumo
    let summary_path = output_dir.join("_summary.json");
    let summary_json = serde_json::to_string_pretty(&summary).expect("Erro ao serializar resumo");
    fs::write(&summary_path, &summary_json).expect("Erro ao salvar resumo");

    println!("─────────────────────────────────────────");
    println!("📊 Resumo:");
    println!("   Total: {} PDFs", summary.total_pdfs);
    println!("   ✅ Sucesso: {}", summary.successful);
    println!("   ❌ Falhas: {}", summary.failed);
    println!("   📄 Páginas extraídas: {}", summary.total_pages);
    println!("   ⏱️  Tempo total: {}ms", summary.total_duration_ms);
    println!("   📋 Resumo salvo em: {}", summary_path.display());
}
