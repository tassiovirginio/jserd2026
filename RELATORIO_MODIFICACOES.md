# Relatório de Modificações — DNose
## Período: 27 de Setembro de 2025 até 30 de Abril de 2026

---

## Sumário

| Métrica | Valor |
|---------|-------|
| Total de Commits | 36 |
| Contribuidores | 2 (Tássio Virginio, Eronildo Júnior) |
| Arquivos Criados | 29 |
| Arquivos Modificados | 60+ |
| Arquivos Deletados | 13 |

---

## Índice

1. [Outubro 2025](#outubro-2025)
2. [Novembro 2025](#novembro-2025)
3. [Dezembro 2025](#dezembro-2025)
4. [Janeiro 2026](#janeiro-2026)
5. [Fevereiro 2026](#fevereiro-2026)
6. [Arquivos Criados](#arquivos-criados)
7. [Arquivos Deletados](#arquivos-deletados)
8. [Novos Detectors Adicionados](#novos-detectors-adicionados)
9. [Métricas Adicionadas](#métricas-adicionadas)
10. [Evolução de Versão](#evolução-de-versão)

---

## Outubro 2025

### 2025-10-02 — `8333a47` — Inicio da correção do bugs das recomendações
**Autor:** Tassio Virginio

**Arquivos modificados:**
- `public/solutions.js`

**Mudanças:** Correção inicial de bugs nas recomendações da interface web.

---

### 2025-10-02 — `17539cf` — Corrigindo bugs
**Autor:** Tassio Virginio

**Arquivos modificados:**
- `.gitignore` — Adição de novas entradas ao ignore
- `bin/dnose.dart` — Correções no binário principal

---

### 2025-10-03 — `40e7e7c` — Corrigindo bugs
**Autor:** Tassio Virginio

**Arquivos modificados:**
- `bin/dnose.dart` — Continuação das correções
- `public/solutions.js` — Correções na página de soluções

---

### 2025-10-11 — `9f6bdbd` — Add mise
**Autor:** Tassio Virginio

**Arquivos modificados/criados:**
- `.gitignore` — Adição de entradas do mise
- `mise.toml` *(NOVO)* — Configuração do mise (task runner) com comandos: `test`, `build`, `format`, `analyze`, `compile`, `run_compiled`

**Conteúdo do `mise.toml`:**
```toml
[tools]
dart = "latest"

[tasks]
test = "dart test"
build = "dart run build_runner clean && dart run build_runner build --delete-conflicting-outputs"
format = "dart format ."
analyze = "dart analyze"
compile = "dart compile exe bin/dnose.dart -o dnose.run"
run_compiled = "./dnose.run"
```

---

### 2025-10-11 — `a16bcf6` — Add mise
**Autor:** Tassio Virginio

**Arquivos modificados:**
- `README.md` — Documentação do mise

---

## Novembro 2025

### 2025-11-16 — `be2e268` — Corrigindo bug na detecção
**Autor:** Tassio Virginio

**Descrição:** O Unknown Test é para detectar quando tem o `verify`. Correção na lógica do detector.

**Arquivos modificados:**
- `lib/detectors/unknown_test_detector.dart`

**Mudança principal:** Ajuste na detecção para que o `verify` do mock não seja confundido com a lógica do teste.

```dart
// Antes: detectava verify incorretamente como lógica
// Depois: verify é reconhecido como parte do mock, não da lógica do teste
```

---

## Dezembro 2025

### 2025-12-08 — `5e1c91b` — Adicionando visual parte 1
**Autor:** Eronildo Júnior

**Arquivos modificados:**
- `bin/dnose.dart`
- `lib/dnose_core.dart`
- `lib/main.dart`
- `public/about.html`
- `public/config.html`
- `public/index.html`
- `public/index.js`
- `public/mining.html`
- `public/projects.html`
- `public/projects.js`
- `public/solutions.html`

**Mudanças:** Reformulação visual completa da interface web do projeto.

---

### 2025-12-08 — `62636a4` — Retirando tudo que não seja do resource optimism
**Autor:** Eronildo Júnior

**Arquivos modificados:**
- `lib/dnose_core.dart`

**Arquivos deletados:**
- `lib/detectors/expected_resolution_omission_detector.dart`
- `lib/detectors/redundant_assertion_detector.dart`
- `lib/detectors/residual_state_test_detector.dart`
- `lib/detectors/widget_setup_smell_detector.dart`
- `test/oracle/expected_resolution_omission_test.dart_`
- `test/oracle/redundant_assertion_test.dart_`
- `test/oracle/residual_state_test.dart_`
- `test/oracle/widget_setup_smell_test.dart_`
- `test/samples/expected_resolution_omission_test.dart`
- `test/samples/redundant_assertion_test.dart`
- `test/samples/residual_state_test.dart`
- `test/samples/widget_setup_smell_test.dart`

**Mudanças:** Limpeza de código — remoção de detectors que não eram do resource optimism.

---

### 2025-12-08 — `dafcbae` — Movendo alterações da main para nova branch
**Autor:** Eronildo Júnior

**Arquivos criados:**
- `lib/detectors/expected_resolution_omission_detector.dart` *(NOVO)*
- `lib/detectors/mystery_guest_detector.dart` *(NOVO)*
- `lib/detectors/redundant_assertion_detector.dart` *(NOVO)*
- `lib/detectors/residual_state_test_detector.dart` *(NOVO)*
- `lib/detectors/widget_setup_smell_detector.dart` *(NOVO)*
- `test/oracle/expected_resolution_omission_test.dart_` *(NOVO)*
- `test/oracle/mystery_guest_test.dart_` *(NOVO)*
- `test/oracle/redundant_assertion_test.dart_` *(NOVO)*
- `test/oracle/residual_state_test.dart_` *(NOVO)*
- `test/oracle/widget_setup_smell_test.dart_` *(NOVO)*
- `test/samples/expected_resolution_omission_test.dart` *(NOVO)*
- `test/samples/mystery_guest_test.dart` *(NOVO)*
- `test/samples/redundant_assertion_test.dart` *(NOVO)*
- `test/samples/residual_state_test.dart` *(NOVO)*
- `test/samples/widget_setup_smell_test.dart` *(NOVO)*
- `package-lock.json` *(NOVO)*
- `build/` *(NOVO — arquivos de build)*

**Arquivos modificados:**
- `lib/detectors/abstract_detector.dart`
- `lib/detectors/test_without_description_detector.dart`
- `lib/dnose_core.dart`
- `lib/models/test_class.dart`
- `test/dnose_all_test.dart`

---

### 2025-12-09 — `f2c6b6d` — Adicionando style e mystery guest
**Autor:** Eronildo Júnior

**Arquivos modificados:**
- `public/about.html`
- `public/index.js`
- `public/projects.js`
- `public/solutions.html`
- `public/solutions.js`

**Mudanças:** Adição de estilos e integração do detector Mystery Guest na interface.

---

### 2025-12-09 — `bec22d0` — Arrumando a nav bar das soluções
**Autor:** Eronildo Júnior

**Arquivos modificados:**
- `public/solutions.html`

---

### 2025-12-09 — `bba601d` — Update README.md
**Autor:** Eronildo Júnior (via GitHub)

**Arquivos modificados:**
- `README.md`

---

### 2025-12-09 — `1cbf534` — Adicionando redundant assertion
**Autor:** Eronildo Júnior

**Arquivos criados:**
- `lib/detectors/redundant_assertion_detector.dart` *(NOVO)* — Detector de asserções redundantes
- `test/oracle/redundant_assertion_test.dart_` *(NOVO)* — Oracle de teste
- `test/samples/redundant_assertion_test.dart` *(NOVO)* — Amostra de teste

**Arquivos modificados:**
- `README.md`
- `lib/dnose_core.dart`
- `public/about.html`
- `public/index.html`
- `test/dnose_all_test.dart`

**Código do `redundant_assertion_detector.dart`:**
```dart
import 'package:analyzer/dart/ast/ast.dart';
import 'package:dnose/detectors/abstract_detector.dart';
import 'package:dnose/models/test_smell.dart';

class RedundantAssertionDetector extends AbstractDetector {
  @override
  void run() {
    for (var testClass in testClasses) {
      final visitor = _Visitor();
      testClass.unit.visitChildren(visitor);
      addSmells(visitor.smells.map((e) => TestSmell(
        name: 'Redundant Assertion',
        path: testClass.path,
        projectName: testClass.projectName,
        moduleAtual: testClass.moduleAtual,
        commit: testClass.commit,
        code: e.toSource(),
        start: testClass.lineNumber(e.offset),
        end: testClass.lineNumber(e.end),
      )).toList());
    }
  }
}
```

---

### 2025-12-12 — `591a995` — Adicionando ERO test smells detection
**Autor:** Eronildo Júnior

**Arquivos criados:**
- `lib/detectors/expected_resolution_omission_detector.dart` *(NOVO)* — Detector de Expected Resolution Omission
- `test/oracle/expected_resolution_omission_test.dart_` *(NOVO)* — Oracle de teste
- `test/samples/expected_resolution_omission_test.dart` *(NOVO)* — Amostra de teste com casos positivos e negativos

**Arquivos modificados:**
- `README.md`
- `lib/dnose_core.dart`
- `public/about.html`
- `public/index.html`
- `test/dnose_all_test.dart`

---

### 2025-12-14 — `74246a1` — Inserindo default test
**Autor:** Eronildo Júnior

**Arquivos criados:**
- `lib/detectors/default_test_detector.dart` *(NOVO)* — Detector de Default Test
- `test/oracle/default_test.dart_` *(NOVO)* — Oracle de teste
- `test/samples/default_test.dart` *(NOVO)* — Amostra de teste

**Arquivos modificados:**
- `README.md`
- `bin/dnose.dart`
- `lib/dnose_core.dart`
- `public/about.html`
- `public/index.html`
- `test/dnose_all_test.dart`

**Código do `default_test_detector.dart`:**
```dart
import 'package:analyzer/dart/ast/ast.dart';
import 'package:analyzer/dart/ast/visitor.dart';
import 'package:dnose/detectors/abstract_detector.dart';
import 'package:dnose/models/test_class.dart';
import 'package:dnose/models/test_smell.dart';

class DefaultTestDetector extends AbstractDetector {
  @override
  void run() {
    for (var testClass in testClasses) {
      final visitor = _Visitor();
      testClass.unit.visitChildren(visitor);
      addSmells(visitor.smells.map((e) => TestSmell(
        name: 'Default Test',
        path: testClass.path,
        projectName: testClass.projectName,
        moduleAtual: testClass.moduleAtual,
        commit: testClass.commit,
        code: e.toSource(),
        start: testClass.lineNumber(e.offset),
        end: testClass.lineNumber(e.end),
      )).toList());
    }
  }
}
```

---

### 2025-12-14 — `cb4adca` — Adicionando residual state
**Autor:** Eronildo Júnior

**Arquivos criados:**
- `lib/detectors/residual_state_test_detector.dart` *(NOVO)* — Detector de Residual State
- `test/oracle/residual_state_test.dart_` *(NOVO)* — Oracle de teste
- `test/samples/residual_state_test.dart` *(NOVO)* — Amostra de teste

**Arquivos modificados:**
- `bin/dnose.dart`
- `lib/dnose_core.dart`
- `public/about.html`
- `public/index.html`
- `test/dnose_all_test.dart`
- `test/samples/default_test.dart`

---

### 2025-12-14 — `e3695be` — Adicionando eager test
**Autor:** Eronildo Júnior

**Arquivos criados:**
- `lib/detectors/eager_test_detector.dart` *(NOVO)* — Detector de Eager Test
- `test/oracle/eager_test.dart_` *(NOVO)* — Oracle de teste
- `test/samples/eager_test.dart` *(NOVO)* — Amostra de teste

**Arquivos modificados:**
- `bin/dnose.dart`
- `lib/dnose_core.dart`
- `public/about.html`
- `public/index.html`
- `test/dnose_all_test.dart`

**Código do `eager_test_detector.dart`:**
```dart
import 'package:analyzer/dart/ast/ast.dart';
import 'package:analyzer/dart/ast/visitor.dart';
import 'package:dnose/detectors/abstract_detector.dart';
import 'package:dnose/models/test_smell.dart';

class EagerTestDetector extends AbstractDetector {
  @override
  void run() {
    for (var testClass in testClasses) {
      final visitor = _Visitor();
      testClass.unit.visitChildren(visitor);
      addSmells(visitor.smells.map((e) => TestSmell(
        name: 'Eager Test',
        path: testClass.path,
        projectName: testClass.projectName,
        moduleAtual: testClass.moduleAtual,
        commit: testClass.commit,
        code: e.toSource(),
        start: testClass.lineNumber(e.offset),
        end: testClass.lineNumber(e.end),
      )).toList());
    }
  }
}
```

---

### 2025-12-14 — `6df4d20` — Adicionando lazy test
**Autor:** Eronildo Júnior

**Arquivos criados:**
- `lib/detectors/lazy_test_detector.dart` *(NOVO)* — Detector de Lazy Test
- `test/oracle/lazy_test.dart_` *(NOVO)* — Oracle de teste

**Arquivos modificados:**
- `bin/dnose.dart`
- `lib/detectors/eager_test_detector.dart` — Ajustes no detector de eager test
- `lib/dnose_core.dart`
- `public/about.html`
- `public/index.html`
- `test/dnose_all_test.dart`

---

### 2025-12-14 — `c797433` — Adicionando widget setup
**Autor:** Eronildo Júnior

**Arquivos criados:**
- `lib/detectors/widget_setup_detector.dart` *(NOVO)* — Detector de Widget Setup
- `test/oracle/widget_setup_test.dart_` *(NOVO)* — Oracle de teste

**Arquivos modificados:**
- `bin/dnose.dart`
- `lib/dnose_core.dart`
- `public/about.html`
- `public/index.html`
- `test/dnose_all_test.dart`

---

### 2025-12-21 — `078e20d` — Adicionando todos os smells
**Autor:** Eronildo Júnior

**Arquivos modificados:**
- `README.md` — Atualização da lista de smells detectados
- `bin/dnose.dart` — Registro de todos os detectors
- `lib/dnose_core.dart` — Integração completa dos detectors

---

## Janeiro 2026

### 2026-01-05 — `870d3e9` — Refatorando blameFile
**Autor:** Tássio Virgínio

**Descrição:** Refatoração para melhorar a legibilidade e tratamento de erros na função `blameFile`.

**Arquivos modificados:**
- `lib/main.dart`
- `lib/utils/blame.dart`

**Mudanças no `blame.dart`:**
```dart
// Antes: tratamento de erros simplificado
// Depois: tratamento robusto com try/catch e mensagens de erro descritivas
```

---

### 2026-01-11 — `1b4d88b` — Adicionando dependent test detector
**Autor:** Eronildo Júnior

**Arquivos criados:**
- `lib/detectors/dependent_test_detector.dart` *(NOVO)* — Detector de Dependent Test
- `test/oracle/dependent_test.dart_` *(NOVO)* — Oracle de teste
- `test/samples/dependent_test.dart` *(NOVO)* — Amostra de teste

**Arquivos modificados:**
- `README.md`
- `bin/dnose.dart`
- `lib/dnose_core.dart`
- `public/about.html`
- `public/index.html`
- `test/dnose_all_test.dart`

**Código do `dependent_test_detector.dart`:**
```dart
import 'package:analyzer/dart/ast/ast.dart';
import 'package:analyzer/dart/ast/visitor.dart';
import 'package:dnose/detectors/abstract_detector.dart';
import 'package:dnose/models/test_class.dart';
import 'package:dnose/models/test_smell.dart';

class DependentTestDetector extends AbstractDetector {
  @override
  void run() {
    for (var testClass in testClasses) {
      final visitor = _Visitor();
      testClass.unit.visitChildren(visitor);
      addSmells(visitor.smells.map((e) => TestSmell(
        name: 'Dependent Test',
        path: testClass.path,
        projectName: testClass.projectName,
        moduleAtual: testClass.moduleAtual,
        commit: testClass.commit,
        code: e.toSource(),
        start: testClass.lineNumber(e.offset),
        end: testClass.lineNumber(e.end),
      )).toList());
    }
  }
}
```

---

## Fevereiro 2026

### 2026-02-20 — `0fabca6` — Atualizando Dart para 3.11.0
**Autor:** Tássio Virgínio

**Descrição:** Atualização da versão do Dart para 3.11.0, formatação de código e adição de linha removida.

**Arquivos modificados:**
- `lib/main.dart`
- `mise.toml`

**Mudança no `mise.toml`:**
```toml
[tools]
dart = "3.11.0"  # Antes: "latest"
```

---

### 2026-02-20 — `48e4045` — Constructor Initialization + Negative Oracles
**Autor:** Eronildo Júnior

**Descrição:** Adição do detector Constructor Initialization, remoção de falsos positivos do Widget Setup, adição de negative oracles.

**Arquivos criados:**
- `lib/detectors/constructor_initialization_detector.dart` *(NOVO)*
- `test/oracle/negative/default_test_clean_test.dart_` *(NOVO)*
- `test/oracle/negative/dependent_test_clean_test.dart_` *(NOVO)*
- `test/oracle/negative/eager_test_clean_test.dart_` *(NOVO)*
- `test/oracle/negative/ero_clean_test.dart_` *(NOVO)*
- `test/oracle/negative/lazy_test_clean_test.dart_` *(NOVO)*
- `test/oracle/negative/mystery_guest_clean_test.dart_` *(NOVO)*
- `test/oracle/negative/redundant_assertion_clean_test.dart_` *(NOVO)*
- `test/oracle/negative/residual_state_clean_test.dart_` *(NOVO)*
- `test/oracle/negative/widget_setup_clean_test.dart_` *(NOVO)*
- `test/samples/constructor_initialization_test.dart` *(NOVO)*

**Arquivos modificados:**
- `README.md`
- `bin/dnose.dart`
- `lib/detectors/widget_setup_detector.dart` — Remoção de falsos positivos
- `lib/dnose_core.dart`
- `public/about.html`
- `public/index.html`
- `test/dnose_all_test.dart`
- `test/oracle/default_test.dart_`
- `test/oracle/mystery_guest_test.dart_`

---

### 2026-02-23 — `0b991f0` — Processamento Concorrente + Flatten Metadata
**Autor:** Tássio Virgínio

**Descrição:** Implementação de processamento concorrente de arquivos com semaphore e flatten de metadados de test class em test metrics para performance melhorada.

**Arquivos modificados (32 arquivos):**
- `lib/detectors/abstract_detector.dart`
- `lib/detectors/assertion_roulette_detector.dart`
- `lib/detectors/conditional_test_logic_detector.dart`
- `lib/detectors/constructor_initialization_detector.dart`
- `lib/detectors/default_test_detector.dart`
- `lib/detectors/dependent_test_detector.dart`
- `lib/detectors/duplicate_assert_detector.dart`
- `lib/detectors/eager_test_detector.dart`
- `lib/detectors/empty_test_detector.dart`
- `lib/detectors/exception_handling_detector.dart`
- `lib/detectors/expected_resolution_omission_detector.dart`
- `lib/detectors/ignored_test_detector.dart`
- `lib/detectors/lazy_test_detector.dart`
- `lib/detectors/magic_number_detector.dart`
- `lib/detectors/mystery_guest_detector.dart`
- `lib/detectors/print_statment_fixture_detector.dart`
- `lib/detectors/redundant_assertion_detector.dart`
- `lib/detectors/residual_state_test_detector.dart`
- `lib/detectors/resource_optimism_detector.dart`
- `lib/detectors/sensitive_equality_detector.dart`
- `lib/detectors/sleepy_fixture_detector.dart`
- `lib/detectors/test_without_description_detector.dart`
- `lib/detectors/unknown_test_detector.dart`
- `lib/detectors/verbose_test_detector.dart`
- `lib/detectors/widget_setup_detector.dart`
- `lib/dnose_core.dart`
- `lib/main.dart`
- `lib/metrics/cyclomatic_complexity_metric.dart`
- `lib/metrics/lines_of_code_metric.dart`
- `lib/models/test_metric.dart`
- `lib/models/test_smell.dart`
- `lib/utils/blame.dart`

**Mudança principal no `dnose_core.dart`:**
```dart
// Antes: processamento sequencial
for (var path in paths) {
  final content = await File(path).readAsString();
  // ...
}

// Depois: processamento concorrente com semaphore
final semaphore = Semaphore(concurrency);
for (var path in paths) {
  await semaphore.withResource(() async {
    final content = await File(path).readAsString();
    // ...
  });
}
```

**Mudança no `test_metric.dart`:**
```dart
// Antes: dados aninhados do TestClass
// Depois: dados flatten diretamente no TestMetric
class TestMetric {
  final String name;
  final String testName;
  final String path;
  final String projectName;
  final String moduleAtual;
  final String commit;
  final String code;
  final int start;
  final int end;
  final dynamic value;
  // ...
}
```

---

### 2026-02-23 — `14d26c0` — TUI Dashboard
**Autor:** Tássio Virgínio

**Descrição:** Implementação de um rico dashboard TUI com barras de progresso em tempo real, logs de detecção e status de workers.

**Arquivos criados:**
- `lib/utils/tui.dart` *(NOVO)* — Terminal UI com barras de progresso animadas

**Arquivos modificados:**
- `lib/main.dart` — Integração do TUI
- `lib/utils/git_log.dart` — Adaptação para o TUI

**Código do `tui.dart`:**
```dart
import 'dart:io';

const _barWidth = 22;

class Tui {
  final List<DetectionLog> _logs = [];
  final List<WorkerStatus> _workers = [];
  final List<ProgressBar> _progressBars = [];

  void render() {
    stdout.write('\x1B[2J\x1B[H');
    _renderProgressBars();
    _renderLogs();
    _renderWorkers();
  }

  void _renderProgressBars() {
    for (var bar in _progressBars) {
      final filled = (bar.progress * _barWidth).round();
      final empty = _barWidth - filled;
      final barStr = '█' * filled + '░' * empty;
      stdout.write('[$barStr] ${bar.project}\n');
    }
  }

  void _renderLogs() {
    for (var log in _logs) {
      stdout.write('  ${log.smell} — ${log.path}\n');
    }
  }

  void _renderWorkers() {
    for (var worker in _workers) {
      stdout.write('Worker ${worker.id}: ${worker.status}\n');
    }
  }

  void addLog(DetectionLog log) {
    _logs.add(log);
    render();
  }

  void updateWorker(WorkerStatus worker) {
    final index = _workers.indexWhere((w) => w.id == worker.id);
    if (index != -1) {
      _workers[index] = worker;
    } else {
      _workers.add(worker);
    }
    render();
  }
}
```

---

### 2026-02-23 — `67dce69` — Fix: barWidth de 30 para 22
**Autor:** Tássio Virgínio

**Descrição:** Correção da constante `_barWidth` de 30 para 22 para melhor ajuste em terminais.

**Arquivos modificados:**
- `lib/utils/tui.dart`

---

### 2026-02-23 — Vários commits de `update`
**Autor:** Tássio Virgínio

#### `6ebef72` — Remoção de arquivo de teste
- `test/samples/residual_state_test.dart` — Deletado

#### `d882d9e` — Update release workflow
- `.github/workflows/release.yml` — Atualização do workflow de release

#### `b76016a`, `1137a76` — Update CI workflow
- `.github/workflows/dart.yml` — Atualizações do workflow de CI/CD

#### `9b2a18c` — Update CI e analysis
- `.github/workflows/dart.yml` — Mais ajustes de CI
- `analysis_options.yaml` — Configurações de análise

---

### 2026-02-23 — `417ddad` — Logical Lines of Code + Cyclomatic Complexity
**Autor:** Tássio Virgínio

**Descrição:** Adição da métrica Logical Lines of Code (LLOC) e refinamento do cálculo de Cyclomatic Complexity.

**Arquivos criados:**
- `lib/metrics/logical_lines_of_code_metric.dart` *(NOVO)*

**Arquivos modificados:**
- `lib/dnose_core.dart` — Registro da nova métrica
- `lib/metrics/cyclomatic_complexity_metric.dart` — Refinamento do cálculo

**Código do `logical_lines_of_code_metric.dart`:**
```dart
import 'package:analyzer/dart/ast/ast.dart';
import 'package:dnose/metrics/abstract_metric.dart';
import 'package:dnose/models/test_class.dart';
import 'package:dnose/models/test_metric.dart';

class LogicalLinesOfCodeMetric implements AbstractMetric {
  int _lloc = 0;

  @override
  TestMetric calculate(
    ExpressionStatement e,
    TestClass testClass,
    String testName,
  ) {
    _lloc = 0;
    _calculate(e);

    return TestMetric(
      name: metricName,
      testName: testName,
      path: testClass.path,
      projectName: testClass.projectName,
      moduleAtual: testClass.moduleAtual,
      commit: testClass.commit,
      code: e.toSource(),
      start: testClass.lineNumber(e.offset),
      end: testClass.lineNumber(e.end),
      value: _lloc,
    );
  }

  void _calculate(AstNode e) {
    if (e is Statement && e is! Block && e is! EmptyStatement) {
      _lloc++;
    }
    if (e is VariableDeclarationList &&
        e.parent is! VariableDeclarationStatement) {
      _lloc++;
    }
    e.childEntities.whereType<AstNode>().forEach((child) => _calculate(child));
  }

  @override
  String get metricName => "Logical Lines Of Code";
}
```

**Refinamento no `cyclomatic_complexity_metric.dart`:**
```dart
// Adição de operadores lógicos ao cálculo:
} else if (e is BinaryExpression) {
  final operator = e.operator.lexeme;
  if (operator == '&&' || operator == '||' || operator == '??') {
    cont++;
  }
}
```

**Registro no `dnose_core.dart`:**
```dart
List<AbstractMetric> _createMetrics() {
  return [
    LinesOfCodeMetric(),
    CyclomaticComplexityMetric(),
    LogicalLinesOfCodeMetric(),  // NOVO
  ];
}
```

---

### 2026-02-23 — `afb65d7` — Format
**Autor:** Tássio Virgínio

**Descrição:** Formatação automática de código em massa (dart format).

**Arquivos modificados (40 arquivos):**
- `bin/dnose.dart`
- `lib/detectors/expected_resolution_omission_detector.dart`
- `lib/detectors/unknown_test_detector.dart`
- `lib/experiment.dart`
- `lib/isolations.dart`
- `lib/lints/empty_test_lint.dart`
- `lib/lints/my_custom_lint_code.dart`
- `lib/lints/my_custom_lint_package.dart`
- `lib/lints/sleep_test_lint.dart`
- `lib/lints/unknown_test_lint.dart`
- `lib/lints/verbose_test_lint.dart`
- `lib/math/co_ocurrence.dart`
- `lib/math/pearson2.dart`
- `lib/metrics/abstract_metric.dart`
- `lib/pages.dart`
- `lib/utils/progresso.dart`
- `lib/utils/util.dart`
- `test/others/google_ai.dart`
- `test/samples/assertion_roulette_test.dart`
- `test/samples/conditional_test_logic_test.dart`
- `test/samples/dependent_test.dart`
- `test/samples/duplicate_assert_test.dart`
- `test/samples/empty_test.dart`
- `test/samples/expected_resolution_omission_test.dart`
- `test/samples/ignored_test.dart`
- `test/samples/magic_number_test.dart`
- `test/samples/mystery_guest_test.dart`
- `test/samples/print_statment_fixture_test.dart`
- `test/samples/redundant_assertion_test.dart`
- `test/samples/resource_optimism_test.dart`
- `test/samples/sensitive_equality_test.dart`
- `test/samples/sleepy_fixture_test.dart`
- `test/samples/test_without_description_test.dart`
- `test/samples/unknown_test.dart`
- `test/samples/verbose_test.dart`

---

### 2026-02-23 — `271120e` — Update version (2.0.1)
**Autor:** Tássio Virgínio

**Arquivos modificados:**
- `pubspec.yaml` — Versão de 2.0.0 para 2.0.1

---

### 2026-02-26 — `57cede9` — Criando pacote AUR
**Autor:** Tassio Virginio

**Descrição:** Configuração de workflow GitHub Actions para atualização automática do pacote AUR (Arch Linux).

**Arquivos criados:**
- `.github/workflows/update_aur.yml` *(NOVO)*

**Arquivos modificados:**
- `bin/dnose.dart` — Adição de `--version` e `--help`
- `mise.toml` — Renomeação do binário compilado

**Código do `update_aur.yml`:**
```yaml
name: Update AUR

on:
  workflow_run:
    workflows: ["Build and Release Multi-Platform"]
    types:
      - completed
  workflow_dispatch:
    inputs:
      tag_name:
        description: 'Tag version (ex: v0.1.0)'
        required: true
        default: 'v0.1.0'

jobs:
  aur:
    runs-on: ubuntu-latest
    container: archlinux:base-devel
    if: ${{ github.event_name == 'workflow_dispatch' || 
           (github.event_name == 'workflow_run' && 
            github.event.workflow_run.conclusion == 'success') }}
    steps:
      - name: Checkout
        uses: actions/checkout@v4
      - name: Install dependencies
        run: pacman -Sy --noconfirm git openssh pacman-contrib
      - name: Setup SSH
        run: |
          mkdir -p /root/.ssh
          printf "%s\n" "${{ secrets.AUR_SSH_PRIVATE_KEY }}" > /root/.ssh/id_ed25519
          chmod 600 /root/.ssh/id_ed25519
          ssh-keyscan aur.archlinux.org >> /root/.ssh/known_hosts
      - name: Clone AUR repo
        run: git clone ssh://aur@aur.archlinux.org/dnose-bin.git aur
      - name: Update PKGBUILD and Checksums
        run: |
          # ... atualização automática do PKGBUILD
      - name: Commit and push
        run: |
          # ... push para o AUR
```

**Adição no `bin/dnose.dart`:**
```dart
const String version = '2.0.1';

void main(List<String> args) async {
  if (args.isNotEmpty && args[0] == '--version') {
    print('dnose version $version');
    exit(0);
  }
  if (args.isNotEmpty && args[0] == '--help') {
    print('''
dnose - Dart Test Smell Detector

Usage:
  dnose           Start the web interface
  dnose --version Show version
  dnose --help    Show this help message
''');
    exit(0);
  }
  // ...
}
```

---

### 2026-02-26 — `081fbbc` — dnose-bin v2.0.2
**Autor:** Tassio Virginio

**Arquivos modificados:**
- `pubspec.yaml` — Versão de 2.0.1 para 2.0.2

---

### 2026-02-26 — `102f733` — dnose-bin v2.0.3
**Autor:** Tassio Virginio

**Arquivos modificados:**
- `pubspec.yaml` — Versão de 2.0.2 para 2.0.3

---

### 2026-02-26 — `60cd5a3` — Add script of the install
**Autor:** Tassio Virginio

**Arquivos criados:**
- `install.sh` *(NOVO)* — Script de instalação automatizada para Linux

**Conteúdo do `install.sh`:**
```bash
#!/bin/sh
set -e

REPO="tassiovirginio/dnose"
BIN_NAME="dnose"
ASSET_NAME="dnose_linux_amd64"

# ANSI colors
GREEN="\033[0;32m"
BLUE="\033[0;34m"
RED="\033[0;31m"
RESET="\033[0m"

echo "${BLUE}==> Fetching latest release of $BIN_NAME...${RESET}"

# Require curl or wget
if command -v curl >/dev/null 2>&1; then
    FETCH_CMD="curl -sSL"
elif command -v wget >/dev/null 2>&1; then
    FETCH_CMD="wget -qO-"
else
    echo "${RED}Error: curl or wget is required to install $BIN_NAME.${RESET}"
    exit 1
fi

# Fetch latest release tag
LATEST_RELEASE=$($FETCH_CMD "https://api.github.com/repos/$REPO/releases/latest" | grep '"tag_name":' | sed -E 's/.*"([^"]+)".*/\1/')

if [ -z "$LATEST_RELEASE" ]; then
    echo "${RED}Error: Could not retrieve latest release from GitHub.${RESET}"
    exit 1
fi

echo "${BLUE}==> Latest release is $LATEST_RELEASE${RESET}"

DOWNLOAD_URL="https://github.com/$REPO/releases/download/$LATEST_RELEASE/$ASSET_NAME"

INSTALL_DIR="$HOME/.local/bin"
if [ "$(id -u)" = "0" ]; then
    INSTALL_DIR="/usr/local/bin"
fi

if [ ! -d "$INSTALL_DIR" ]; then
    echo "${BLUE}==> Creating directory $INSTALL_DIR...${RESET}"
    mkdir -p "$INSTALL_DIR"
fi

echo "${BLUE}==> Downloading $BIN_NAME to $INSTALL_DIR...${RESET}"
if command -v curl >/dev/null 2>&1; then
    curl -sSL "$DOWNLOAD_URL" -o "$INSTALL_DIR/$BIN_NAME"
else
    wget -q "$DOWNLOAD_URL" -O "$INSTALL_DIR/$BIN_NAME"
fi
chmod +x "$INSTALL_DIR/$BIN_NAME"

echo "${GREEN}==> $BIN_NAME installed successfully in $INSTALL_DIR!${RESET}"
```

---

### 2026-02-26 — `2f0b18e` — Add script of the install (README)
**Autor:** Tassio Virginio

**Arquivos modificados:**
- `README.md` — Adição de instruções de instalação via curl/wget

**Adição ao README:**
```markdown
### Install via Command Line (Linux)

You can easily install or update DNose on Linux by running one of the commands below:

**Using curl:**
curl -sSL https://raw.githubusercontent.com/tassiovirginio/dnose/main/install.sh | sh

**Using wget:**
wget -qO- https://raw.githubusercontent.com/tassiovirginio/dnose/main/install.sh | sh
```

---

## Arquivos Criados

### Detectors (lib/detectors/)
| Arquivo | Data | Autor |
|---------|------|-------|
| `constructor_initialization_detector.dart` | 2026-02-20 | Eronildo Júnior |
| `dependent_test_detector.dart` | 2026-01-11 | Eronildo Júnior |
| `expected_resolution_omission_detector.dart` | 2025-12-12 | Eronildo Júnior |
| `redundant_assertion_detector.dart` | 2025-12-09 | Eronildo Júnior |
| `default_test_detector.dart` | 2025-12-14 | Eronildo Júnior |
| `residual_state_test_detector.dart` | 2025-12-14 | Eronildo Júnior |
| `eager_test_detector.dart` | 2025-12-14 | Eronildo Júnior |
| `lazy_test_detector.dart` | 2025-12-14 | Eronildo Júnior |
| `widget_setup_detector.dart` | 2025-12-14 | Eronildo Júnior |
| `mystery_guest_detector.dart` | 2025-12-08 | Eronildo Júnior |

### Métricas (lib/metrics/)
| Arquivo | Data | Autor |
|---------|------|-------|
| `logical_lines_of_code_metric.dart` | 2026-02-23 | Tássio Virgínio |

### Testes Oracle (test/oracle/)
| Arquivo | Data |
|---------|------|
| `constructor_initialization_test.dart` | 2026-02-20 |
| `dependent_test.dart_` | 2026-01-11 |
| `expected_resolution_omission_test.dart_` | 2025-12-12 |
| `redundant_assertion_test.dart_` | 2025-12-09 |
| `default_test.dart_` | 2025-12-14 |
| `residual_state_test.dart_` | 2025-12-14 |
| `eager_test.dart_` | 2025-12-14 |
| `lazy_test.dart_` | 2025-12-14 |
| `widget_setup_test.dart_` | 2025-12-14 |
| `mystery_guest_test.dart_` | 2025-12-08 |

### Negative Oracles (test/oracle/negative/)
| Arquivo | Data |
|---------|------|
| `default_test_clean_test.dart_` | 2026-02-20 |
| `dependent_test_clean_test.dart_` | 2026-02-20 |
| `eager_test_clean_test.dart_` | 2026-02-20 |
| `ero_clean_test.dart_` | 2026-02-20 |
| `lazy_test_clean_test.dart_` | 2026-02-20 |
| `mystery_guest_clean_test.dart_` | 2026-02-20 |
| `redundant_assertion_clean_test.dart_` | 2026-02-20 |
| `residual_state_clean_test.dart_` | 2026-02-20 |
| `widget_setup_clean_test.dart_` | 2026-02-20 |

### Infraestrutura
| Arquivo | Data |
|---------|------|
| `.github/workflows/update_aur.yml` | 2026-02-26 |
| `install.sh` | 2026-02-26 |
| `mise.toml` | 2025-10-11 |
| `lib/utils/tui.dart` | 2026-02-23 |

### Test Samples
| Arquivo | Data |
|---------|------|
| `test/samples/constructor_initialization_test.dart` | 2026-02-20 |
| `test/samples/dependent_test.dart` | 2026-01-11 |
| `test/samples/expected_resolution_omission_test.dart` | 2025-12-12 |
| `test/samples/redundant_assertion_test.dart` | 2025-12-09 |
| `test/samples/default_test.dart` | 2025-12-14 |
| `test/samples/residual_state_test.dart` | 2025-12-14 |
| `test/samples/eager_test.dart` | 2025-12-14 |
| `test/samples/mystery_guest_test.dart` | 2025-12-08 |
| `test/samples/widget_setup_smell_test.dart` | 2025-12-08 |

---

## Arquivos Deletados

| Arquivo | Data | Commit |
|---------|------|--------|
| `test/samples/residual_state_test.dart` | 2026-02-23 | `6ebef72` |
| `lib/detectors/expected_resolution_omission_detector.dart` | 2025-12-08 | `62636a4` (temporário, re-adicionado depois) |
| `lib/detectors/redundant_assertion_detector.dart` | 2025-12-08 | `62636a4` (temporário, re-adicionado depois) |
| `lib/detectors/residual_state_test_detector.dart` | 2025-12-08 | `62636a4` (temporário, re-adicionado depois) |
| `lib/detectors/widget_setup_smell_detector.dart` | 2025-12-08 | `62636a4` |
| `test/oracle/expected_resolution_omission_test.dart_` | 2025-12-08 | `62636a4` (temporário, re-adicionado depois) |
| `test/oracle/redundant_assertion_test.dart_` | 2025-12-08 | `62636a4` (temporário, re-adicionado depois) |
| `test/oracle/residual_state_test.dart_` | 2025-12-08 | `62636a4` (temporário, re-adicionado depois) |
| `test/oracle/widget_setup_smell_test.dart_` | 2025-12-08 | `62636a4` |
| `test/samples/expected_resolution_omission_test.dart` | 2025-12-08 | `62636a4` (temporário, re-adicionado depois) |
| `test/samples/redundant_assertion_test.dart` | 2025-12-08 | `62636a4` (temporário, re-adicionado depois) |
| `test/samples/residual_state_test.dart` | 2025-12-08 | `62636a4` (temporário, re-adicionado depois) |
| `test/samples/widget_setup_smell_test.dart` | 2025-12-08 | `62636a4` |

---

## Novos Detectors Adicionados

| # | Detector | Data | Autor |
|---|----------|------|-------|
| 1 | **Mystery Guest** | 2025-12-08 | Eronildo Júnior |
| 2 | **Expected Resolution Omission** | 2025-12-12 | Eronildo Júnior |
| 3 | **Redundant Assertion** | 2025-12-09 | Eronildo Júnior |
| 4 | **Default Test** | 2025-12-14 | Eronildo Júnior |
| 5 | **Residual State** | 2025-12-14 | Eronildo Júnior |
| 6 | **Eager Test** | 2025-12-14 | Eronildo Júnior |
| 7 | **Lazy Test** | 2025-12-14 | Eronildo Júnior |
| 8 | **Widget Setup** | 2025-12-14 | Eronildo Júnior |
| 9 | **Dependent Test** | 2026-01-11 | Eronildo Júnior |
| 10 | **Constructor Initialization** | 2026-02-20 | Eronildo Júnior |

---

## Métricas Adicionadas

| # | Métrica | Data | Autor |
|---|---------|------|-------|
| 1 | **Lines Of Code** | Existente | — |
| 2 | **Cyclomatic Complexity** (refinado) | 2026-02-23 | Tássio Virgínio |
| 3 | **Logical Lines Of Code** *(NOVO)* | 2026-02-23 | Tássio Virgínio |

---

## Evolução de Versão

| Versão | Data | Notas |
|--------|------|-------|
| 2.0.0 | Antes do período | Versão base |
| 2.0.1 | 2026-02-23 | TUI Dashboard, métricas, processamento concorrente |
| 2.0.2 | 2026-02-26 | Pacote AUR, CLI --version/--help |
| 2.0.3 | 2026-02-26 | Script de instalação |

---

## Lista Completa de Commits

| Hash | Data | Mensagem | Autor |
|------|------|----------|-------|
| `8333a47` | 2025-10-02 | inicio da correção do bugs das recomendacoes | Tassio Virginio |
| `17539cf` | 2025-10-02 | corrigindo bugs | Tassio Virginio |
| `40e7e7c` | 2025-10-03 | corrigindo bugs | Tassio Virginio |
| `9f6bdbd` | 2025-10-11 | add mise | Tassio Virginio |
| `a16bcf6` | 2025-10-11 | add mise | Tassio Virginio |
| `be2e268` | 2025-11-16 | corrigindo bug na detecção | Tassio Virginio |
| `5e1c91b` | 2025-12-08 | adicionando visual parte 1 | Eronildo Júnior |
| `62636a4` | 2025-12-08 | retirando tudo que n seja do resource optimism | Eronildo Júnior |
| `dafcbae` | 2025-12-08 | movendo alterações da main para nova branch | Eronildo Júnior |
| `f2c6b6d` | 2025-12-09 | adicoandno style e mystery guest | Eronildo Júnior |
| `bec22d0` | 2025-12-09 | arruamndo a nav bar das soluções | Eronildo Júnior |
| `bba601d` | 2025-12-09 | Update README.md | Eronildo Júnior |
| `1cbf534` | 2025-12-09 | adicionando redundant assertion | Eronildo Júnior |
| `591a995` | 2025-12-12 | adicionando ero test smells detection | Eronildo Júnior |
| `74246a1` | 2025-12-14 | inserindo default test | Eronildo Júnior |
| `cb4adca` | 2025-12-14 | adicionando residual state | Eronildo Júnior |
| `e3695be` | 2025-12-14 | adicionando eager test | Eronildo Júnior |
| `6df4d20` | 2025-12-14 | adicionando lazy test | Eronildo Júnior |
| `c797433` | 2025-12-14 | adicionando widget setup | Eronildo Júnior |
| `078e20d` | 2025-12-21 | adiconando todos os smells | Eronildo Júnior |
| `870d3e9` | 2026-01-05 | refatorando blameFile | Tássio Virgínio |
| `1b4d88b` | 2026-01-11 | adicionando dependent test detector | Eronildo Júnior |
| `0fabca6` | 2026-02-20 | atualizando Dart para 3.11.0 | Tássio Virgínio |
| `48e4045` | 2026-02-20 | constructor initialization + negative oracles | Eronildo Júnior |
| `0b991f0` | 2026-02-23 | processamento concorrente + flatten metadata | Tássio Virgínio |
| `14d26c0` | 2026-02-23 | TUI dashboard | Tássio Virgínio |
| `67dce69` | 2026-02-23 | fix: barWidth 30 → 22 | Tássio Virgínio |
| `6ebef72` | 2026-02-23 | update | Tássio Virgínio |
| `d882d9e` | 2026-02-23 | update | Tássio Virgínio |
| `1137a76` | 2026-02-23 | update | Tássio Virgínio |
| `b76016a` | 2026-02-23 | update | Tássio Virgínio |
| `9b2a18c` | 2026-02-23 | update | Tássio Virgínio |
| `417ddad` | 2026-02-23 | Logical Lines of Code + Cyclomatic Complexity | Tássio Virgínio |
| `afb65d7` | 2026-02-23 | format | Tássio Virgínio |
| `271120e` | 2026-02-23 | update version (2.0.1) | Tássio Virgínio |
| `57cede9` | 2026-02-26 | criando pacote AUR | Tassio Virginio |
| `081fbbc` | 2026-02-26 | dnose-bin v2.0.2 | Tassio Virginio |
| `102f733` | 2026-02-26 | dnose-bin v2.0.3 | Tassio Virginio |
| `60cd5a3` | 2026-02-26 | add script of the install | Tassio Virginio |
| `2f0b18e` | 2026-02-26 | add script of the install (README) | Tassio Virginio |

---

*Relatório gerado em 30 de Abril de 2026*
