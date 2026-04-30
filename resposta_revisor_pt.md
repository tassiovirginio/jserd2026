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

Em resumo, as 1.115.938 ocorrências representam um retrato muito mais maduro, realista e completo dos *test smells* presentes nos 4.154 repositórios originais. Adicionamos uma nova subseção na **Metodologia** do artigo para detalhar explicitamente essa evolução da ferramenta de detecção e justificar adequadamente a expansão do *dataset* para os leitores.

---

# Resposta ao Revisor: Análise de Sentimentos e Validade de Construto

**Comentário do Revisor:**
*O construto latente de interesse (frustração do desenvolvedor ou percepção negativa associada à dívida técnica) é apenas fracamente e indiretamente refletido no proxy escolhido, ou seja, a polaridade de sentimento nas mensagens de commit. Isso levanta várias ameaças à validade de construto que não são suficientemente discutidas. Mensagens de commit não são projetadas para capturar estados emocionais. Elas são tipicamente curtas, técnicas e neutras, e em alguns casos, geradas automaticamente. Consequentemente, há uma lacuna fundamental de inferência. A análise não permite determinar se os desenvolvedores estavam cientes dos cheiros de teste, se tais cheiros causaram frustração, ou se o sentimento expresso está realmente relacionado àqueles cheiros.*

**Resposta dos Autores:**
Agradecemos profundamente a crítica construtiva do revisor sobre a validade de construto. Concordamos plenamente que mensagens de commit são primariamente artefatos técnicos e que assumir causalidade estrita — ou seja, que um *test smell* causou diretamente o sentimento negativo expresso em um commit — constitui uma lacuna de inferência.

Nesta versão estendida, refinamos nossa metodologia e discussão para nos alinharmos com a literatura estabelecida em Engenharia de Software Empírica, em vez de alegar causalidade direta. Estudos seminais, como os de Guzman et al. (2014), demonstraram que mensagens de commit, apesar de sua natureza técnica, podem servir como um *proxy* válido para extrair o sentimento do desenvolvedor e correlacioná-lo com artefatos de software. Mais recentemente, Lin et al. (2018) e Kaur et al. (2022) exploraram as limitações desta abordagem, questionando explicitamente até onde a análise de sentimentos pode ir e discutindo os vários fatores que influenciam as emoções dos desenvolvedores. Além disso, Dey et al. (2025) fornecem diretrizes modernas para a extração de emoções em mensagens de commit.

Com base nestes trabalhos fundamentais, reformulamos significativamente nossas afirmações no manuscrito. Agora, enquadramos nossa investigação não como uma relação de causa e efeito, mas como um estudo observacional de *coocorrência*. Buscamos entender se a degradação da qualidade do código de teste (indicada pela presença de *test smells*) coocorre com uma polaridade emocional negativa durante o momento do commit.

Para abordar adequadamente a preocupação do revisor no manuscrito:
1. Expandimos a Seção 6.2 (Análise de Sentimentos) para incluir uma fundamentação teórica citando Guzman et al. (2014), Lin et al. (2018), Kaur et al. (2022) e Dey et al. (2025), justificando o uso de mensagens de commit como um *proxy* estabelecido, embora imperfeito, na pesquisa em engenharia de software.
2. Reescrevemos completamente a subseção de Validade de Construto na Seção 7 (Ameaças à Validade). Agora reconhecemos explicitamente a "lacuna de inferência" apontada pelo revisor. Afirmamos que nossa análise mede a coocorrência em vez de causalidade, reconhecendo que mensagens de commit são frequentemente breves ou geradas automaticamente, e que um sentimento negativo pode ser multicausal. Ao limitar nossas afirmações, acreditamos que a análise de sentimentos está agora metodologicamente sólida e firmemente conectada ao restante do estudo.
