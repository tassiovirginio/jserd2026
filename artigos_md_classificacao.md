# Classificação dos Artigos em `artigos_md` vs. Citações do Estudo

## Metodologia

- Cruzamento entre os **50 diretórios** em `artigos_md` e os **57 citation keys** usados no estudo
- Classificação por tema: 🧪 Test Smells | 💭 Sentimentos | 🔬 Testes/Qualidade | 🤖 LLM | 📊 Outro

---

## Artigos na pasta `artigos_md` - Classificação e Status de Citação

### 🧪 Test Smells (Tema principal do estudo)

| # | Pasta em `artigos_md` | Tema | Citado? | Observação |
|---|---|---|---|---|
| 1 | `DNose_Dart_Test_Smell_Detector` | 🧪 Test Smells | ✅ `dnose_2025` | Ferramenta dos autores |
| 2 | `DNose__Dart_Test_Smell_Detector` | 🧪 Test Smells | ✅ `dnose_2025` | **Duplicado** do anterior |
| 3 | `On_the_prevalence_of_test_smells_in_mobile_develop` | 🧪 Test Smells | ✅ (autor) | Artigo dos autores |
| 4 | `On_the_test_smells_detection__an_empirical_study_o` | 🧪 Test Smells | ✅ (autor) | Artigo dos autores |
| 5 | `How_are_test_smells_treated_in_the_wild_A_tale_of_two_empirical_studies` | 🧪 Test Smells | ✅ (provavelmente) | Test smells em projetos reais |
| 6 | `Machine_learning_based_test_smell_detection` | 🧪 Test Smells | ✅ `pontillo2024machine` | ML para detectar test smells |
| 7 | `On_the_use_of_test_smells_for_prediction_of_flaky_tests` | 🧪 Test Smells | ✅ `camara2021use` | Test smells e flaky tests |
| 8 | `Do_the_Test_Smells_Assertion_Roulette_and_Eager_Te` | 🧪 Test Smells | ✅ `Assertion_Roulette_and_Eager_Test` | AR e Eager Test |
| 9 | `TestAXE_Automatically_Refactoring_Test_Smells_Using_JUnit_5_Features` | 🧪 Test Smells | ❌ Não citado | Refatoração de test smells |
| 10 | `TestAXE__Automatically_Refactoring_Test_Smells_Usi` | 🧪 Test Smells | ❌ Não citado | **Duplicado** do anterior |
| 11 | `RAIDE_A_Tool_for_Assertion_Roulette_and_Duplicate_Assert_Identification_and_Refactoring` | 🧪 Test Smells | ✅ `santana2020raide` | Ferramenta RAIDE |
| 12 | `Refactoring_Assertion_Roulette_and_Duplicate_Asser` | 🧪 Test Smells | ✅ `santana2020raide` | **Duplicado** do anterior |
| 13 | `PyNose_a_test_smell_detector_for_python` | 🧪 Test Smells | ✅ `pynose` | Detector para Python |
| 14 | `Manual_Tests_Do_Smell_Cataloging_and_Identifying_Natural_Language_Test_Smells` | 🧪 Test Smells | ✅ `elvys2023` | Test smells em testes manuais |
| 15 | `paper_1777762520` | 🧪 Test Smells | ✅ | **Duplicado** do Manual_Tests_Do_Smell |
| 16 | `JNose_Java_Test_Smell_Detector` | 🧪 Test Smells | ✅ `virginio2020_JNose` | Ferramenta JNose |
| 17 | `test_smells_jnose_2021` | 🧪 Test Smells | ✅ (autor) | PDF inválido |
| 18 | `jserd2021` | 🧪 Test Smells | ✅ (autor) | PDF inválido |
| 19 | `raide_2023` | 🧪 Test Smells | ✅ `santana2020raide` | PDF inválido |
| 20 | `raide_sciencedirect` | 🧪 Test Smells | ✅ | PDF inválido |
| 21 | `On_the_Relation_of_Test_Smells_to_Software_Code_Qu` | 🧪 Test Smells | ❌ Não citado | PDF inválido |
| 22 | `Test_Code_Quality_and_Its_Relation_to_Issue_Handli` | 🧪 Test Smells | ❌ Não citado | PDF inválido |
| 23 | `Detecting_Test_Smells_in_Python_Test_Code_Generate` | 🧪 Test Smells | ❌ Não citado | Test smells em código Python gerado |

### 💭 Sentimentos (Tema secundário do estudo)

| # | Pasta em `artigos_md` | Tema | Citado? | Observação |
|---|---|---|---|---|
| 24 | `2901739.2903501` | 💭 Sentimentos | ✅ `sinha2016` | Sinha et al. - Sentiment in commit logs |
| 25 | `Emotion_SW_commit` | 💭 Sentimentos | ✅ `lin2018` (provável) | Emoções em commits de SW |
| 26 | `eInformatica2022Art02` | 💭 Sentimentos | ✅ `kaur2022` | Fatores influenciando sentimentos em commits |
| 27 | `Sentiment_Polarity_Detection_for_Software_Developm` | 💭 Sentimentos | ✅ `calefato2018sentiment` | Senti4SD |
| 28 | `3180155.3180195` | 💭 Sentimentos | ✅ `ahmed2017senticr` (provável) | SentiCR |
| 29 | `SentimentAnalysis-and-OpinionMining` | 💭 Sentimentos | ❌ Não citado | Livro: Sentiment Analysis (Bing Liu) |
| 30 | `Sentiment_analysis_for_software_engineering_How_far_can_we_go_` | 💭 Sentimentos | ❌ Não citado | Sentiment analysis para SE (ZSL) |

### 🔬 Testes / Qualidade de Software (Apoio)

| # | Pasta em `artigos_md` | Tema | Citado? | Observação |
|---|---|---|---|---|
| 31 | `A_Large-Scale_Study_on_the_Usage_of_Testing_Patter` | 🔬 Testes | ✅ (provável) | Testing patterns |
| 32 | `A_Large_Scale_Study_on_the_Usage_of_Testing_Patterns_That_Address_Maintainability_Attributes_Pattern` | 🔬 Testes | ✅ (provável) | **Duplicado** do anterior |
| 33 | `Computing_inter_rater_reliability_for_observational_data_an_overview_and_tutorial` | 📊 Metodologia | ✅ `hallgren2012computing` | Inter-rater reliability |
| 34 | `Search_based_software_test_data_generation_using_evolutionary_computation` | 🔬 Testes | ❌ Não citado | Search-based testing |
| 35 | `When__how__and_why_developers__do_not__test_in_the` | 🔬 Testes | ❌ Não citado | PDF inválido |
| 36 | `A_review_on_quality_models_to_analyse_the_impact_of_refactored_code_on_maintainability_with_referenc` | 🔬 Qualidade | ❌ Não citado | Modelos de qualidade para refatoração |

### 🤖 LLM / IA (Fora do escopo principal)

| # | Pasta em `artigos_md` | Tema | Citado? | Observação |
|---|---|---|---|---|
| 37 | `An_Empirical_Evaluation_of_Using_Large_Language_Mo` | 🤖 LLM | ❌ Não citado | LLM em testes |
| 38 | `A_Survey_on_Large_Language_Model__LLM__Security_an` | 🤖 LLM | ❌ Não citado | Segurança de LLMs |
| 39 | `ChatGPT` | 🤖 LLM | ❌ Não citado | ChatGPT geral |
| 40 | `Large_Language_Models_for_Software_Engineering__Su` | 🤖 LLM | ❌ Não citado | Survey LLMs para SE |
| 41 | `LLM_for_Test_Script_Generation_and_Migration_Challenges_Capabilities_and_Opportunities` | 🤖 LLM | ❌ Não citado | LLM para geração de testes |
| 42 | `Engenharia_de_Prompt_em_Grandes_Modelos_de_Linguagem` | 🤖 LLM | ❌ Não citado | Prompt engineering |
| 43 | `Fine-tuning_and_prompt_engineering_for_large_langu` | 🤖 LLM | ❌ Não citado | Fine-tuning de LLMs |
| 44 | `GPT_4_Technical_Report` | 🤖 LLM | ❌ Não citado | GPT-4 report |
| 45 | `Tc-llama_2__fine-tuning_LLM_for_technology_and_com` | 🤖 LLM | ❌ Não citado | Tc-Llama 2 |
| 46 | `Tc_llama_2_Fine_tuning_LLM_for_Technology_and_Commercialization_Applications` | 🤖 LLM | ❌ Não citado | **Duplicado** do anterior |
| 47 | `Use_Chat_GPT_to_Solve_Programming_Bugs` | 🤖 LLM | ❌ Não citado | ChatGPT para bugs |

### 📊 Outro

| # | Pasta em `artigos_md` | Tema | Citado? | Observação |
|---|---|---|---|---|
| 48 | `2597073.2597118` | 📊 Outro | ❓ A verificar | Precisa de inspeção |
| 49 | `Cross_platform_mobile_frameworks_used_by_software_developers_worldwide_from_2019_to_2023` | 📊 Estatísticas | ✅ `statista2023` | Dados de frameworks mobile |
| 50 | `TIOBE_Index_2024` | 📊 Estatísticas | ❌ Não citado | Ranking de linguagens TIOBE |
| 51 | `Automatic_Generation_of_Acceptance_Test_Cases_From` | 🔬 Testes | ❌ Não citado | Geração automática de testes |

---

## Resumo

### Distribuição temática dos artigos em `artigos_md`

| Categoria | Quantidade | Citados pelo estudo |
|---|---|---|
| 🧪 Test Smells | 23 (~45%) | ~18 |
| 💭 Sentimentos | 7 (~14%) | ~5 |
| 🔬 Testes/Qualidade | 6 (~12%) | ~3 |
| 🤖 LLM / IA | 11 (~22%) | 0 |
| 📊 Outro | 4 (~8%) | ~1 |

### Artigos NÃO citados pelo estudo

> [!WARNING]
> Os seguintes **11 artigos sobre LLM** na pasta `artigos_md` **NÃO são citados pelo estudo** e **NÃO são sobre o tema do estudo** (test smells ou sentimentos):
> 
> 1. `An_Empirical_Evaluation_of_Using_Large_Language_Mo`
> 2. `A_Survey_on_Large_Language_Model__LLM__Security_an`
> 3. `ChatGPT`
> 4. `Large_Language_Models_for_Software_Engineering__Su`
> 5. `LLM_for_Test_Script_Generation_and_Migration_...`
> 6. `Engenharia_de_Prompt_em_Grandes_Modelos_de_Linguagem`
> 7. `Fine-tuning_and_prompt_engineering_for_large_langu`
> 8. `GPT_4_Technical_Report`
> 9. `Tc-llama_2__fine-tuning_LLM_for_technology_...`
> 10. `Tc_llama_2_Fine_tuning_LLM_for_...` (duplicado)
> 11. `Use_Chat_GPT_to_Solve_Programming_Bugs`

Estes artigos parecem ser de um **outro projeto/estudo** (possivelmente sobre LLMs para geração de testes) e **não são relevantes** para o artigo atual do JSERD.

### Outros artigos não citados (mas sobre o tema)

> [!NOTE]
> Alguns artigos **sobre o tema** (test smells/sentimentos) também **não são citados**:
>
> - `TestAXE_Automatically_Refactoring_Test_Smells_...` — Refatoração automática de test smells
> - `On_the_Relation_of_Test_Smells_to_Software_Code_Qu` — Relação test smells e qualidade (PDF inválido)
> - `SentimentAnalysis-and-OpinionMining` — Livro clássico de Bing Liu
> - `Sentiment_analysis_for_software_engineering_How_far...` — Sentiment analysis ZSL para SE
> - `Detecting_Test_Smells_in_Python_Test_Code_Generate` — Test smells em código Python gerado
> - `Search_based_software_test_data_generation_...` — Search-based testing
> - `TIOBE_Index_2024` — Ranking de linguagens

### Duplicados identificados

> [!IMPORTANT]
> Foram encontrados **6 pares de duplicados** na pasta `artigos_md`:
>
> 1. `DNose_Dart_Test_Smell_Detector` ≡ `DNose__Dart_Test_Smell_Detector`
> 2. `TestAXE_Automatically_Refactoring_...` ≡ `TestAXE__Automatically_Refactoring_...`
> 3. `RAIDE_A_Tool_for_...` ≡ `Refactoring_Assertion_Roulette_...`
> 4. `Manual_Tests_Do_Smell_...` ≡ `paper_1777762520`
> 5. `Tc-llama_2__...` ≡ `Tc_llama_2_Fine_tuning_...`
> 6. `A_Large-Scale_Study_on_...` ≡ `A_Large_Scale_Study_on_...`

---

## Conclusão

> [!TIP]
> **Todos os artigos citados pelo estudo são relevantes ao tema** (test smells, sentimentos ou tópicos de apoio como metodologia/estatísticas). Não há nenhuma citação fora do escopo.

A pasta `artigos_md` contém ~11 artigos sobre LLM que **não são citados** pelo estudo e provavelmente pertencem a outro projeto de pesquisa. Os demais artigos não citados são artigos relacionados ao tema que podem ter sido consultados durante a pesquisa mas não foram incluídos no texto final.
