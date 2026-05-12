# Resposta ao Revisor: Explicação sobre o Crescimento do Dataset

**Comentário do Revisor:**
*Os autores precisam esclarecer por que o conjunto de dados de test smells cresceu de forma tão significativa (de 907.566 para 1.115.938 ocorrências), apesar de utilizarem exatamente o mesmo conjunto de 4.154 repositórios clonados do artigo original do SAST 2025.*

**Resposta dos Autores:**
Agradecemos sinceramente ao revisor por destacar este ponto. Concordamos que o aumento significativo no número de *test smells* detectados dentro do mesmo conjunto de repositórios exige uma explicação técnica clara.

A discrepância no tamanho do *dataset* não se deve à adição de novos repositórios ou novos tipos de *test smells*. Em vez disso, é o resultado direto de uma grande reformulação arquitetural em nossa ferramenta de detecção, o DNose. Entre a submissão original do SAST e esta versão estendida para o JSERD, refatoramos fortemente o motor principal do DNose para resolver problemas graves de subnotificação causados por limitações técnicas anteriores da ferramenta. O aumento nas ocorrências reflete um processo de mineração muito mais preciso e exaustivo. As principais melhorias técnicas que levaram a esse aumento são:

**1. Refatoração Completa para Navegação Nativa na AST (`RecursiveAstVisitor`):**
Na versão anterior, o DNose dependia de um *loop* manual e *ad-hoc* para percorrer a Árvore Sintática Abstrata (AST) dos arquivos Dart (por exemplo, iterando sobre `childEntities`). Essa abordagem manual era inerentemente falha, pois frequentemente falhava ao percorrer ramificações sintáticas muito profundas ou padrões estruturais complexos, fazendo com que a ferramenta ignorasse silenciosamente grandes partes do código de teste. Para a versão do JSERD, reescrevemos completamente o núcleo de todos os detectores para herdar e implementar de forma nativa a classe `RecursiveAstVisitor`, fornecida pelo Dart Analyzer oficial. Essa mudança estrutural garante uma travessia 100% precisa, exaustiva e recursiva da AST. Ao visitar adequadamente cada nó, instrução e expressão, a ferramenta conseguiu identificar mais de 200.000 ocorrências de *test smells* que antes eram "invisíveis" para o método de varredura antigo.

**2. Processamento Concorrente Robusto e Tolerância a Falhas:**
A versão inicial da ferramenta processava os arquivos de forma sequencial. Quando encontrava um arquivo particularmente grande, malformado ou altamente complexo, o *parser* podia travar ou dar *timeout*, abortando silenciosamente a análise daquele arquivo específico ou até pulando diretórios inteiros para evitar que a execução parasse. Para resolver isso, implementamos um *pipeline* de processamento concorrente altamente robusto utilizando semáforos (*semaphores*) e blocos `try-catch` isolados para cada arquivo analisado. Essa arquitetura tolerante a falhas garantiu que a falha no processamento de um arquivo específico não impactasse mais o *pipeline* de extração. Consequentemente, a ferramenta analisou com sucesso milhares de arquivos que foram pulados inadvertidamente durante o processo de mineração do SAST 2025.

**3. Atualização do Parser para o Dart SDK 3.11.0:**
Desde o estudo original, a linguagem Dart e o *framework* Flutter evoluíram significativamente. Atualizamos o analisador interno do DNose para ser totalmente compatível com o Dart 3.11.0. Isso permitiu que a ferramenta gerasse corretamente a AST para repositórios que empregam recursos modernos de sintaxe do Dart (como *pattern matching* e *records*). Anteriormente, encontrar uma sintaxe moderna não reconhecida fazia com que o *parser* falhasse, enquanto o motor atualizado processa esses arquivos com sucesso, expondo os *test smells* contidos neles.

**4. Refinamento de Heurísticas de Detecção Específicas:**
Por fim, corrigimos falsos negativos em detectores específicos. Por exemplo, a heurística para o *smell Unknown Test* foi corrigida para que não confunda mais métodos de verificação de *mocks* (como o `verify` do Mockito) com a lógica real do teste.

Em resumo, as 1.115.938 ocorrências representam um retrato muito mais maduro, realista e completo dos *test smells* presentes nos 4.154 repositórios originais.

**Alterações no manuscrito:**
- **Seção 4.2 (Design):** Adicionamos um novo parágrafo (destacado em azul) detalhando explicitamente a evolução arquitetural do DNose entre a versão do SAST 2025 e esta versão estendida para o JSERD, incluindo a refatoração do `RecursiveAstVisitor`, o pipeline concorrente tolerante a falhas e a atualização para o Dart SDK 3.11.0.


