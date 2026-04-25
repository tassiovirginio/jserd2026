Caro Tássio Virgínio, Márcio Ribeiro, Ivan Machado,

Uma decisão foi tomada sobre o seu artigo "More than one million test smells: how are Dart projects and their sentiments?", submetido ao Journal of Software Engineering Research and Development.

A decisão é: Reenviar para Revisão

A versão revisada do artigo deve ser submetida até 24 de maio de 2026.

Os revisores encontraram o manuscrito estendido relevante e melhorado, mas solicitam revisões em duas áreas principais. Primeiro, os autores devem esclarecer as mudanças no conjunto de dados/ferramenta que levaram ao aumento do número de cheiros de teste detectados apesar do uso dos mesmos repositórios. Segundo, devem fortalecer ou reformular a análise de sentimento, justificando melhor a ligação entre cheiros de teste e sentimento das mensagens de commit e discutindo explicitamente as ameaças de validade de construto relacionadas.

Os comentários dos revisores estão anexados abaixo. Ao preparar a versão revisada do seu artigo, por favor considere-os cuidadosamente. Além da versão revisada do artigo, você DEVE submeter uma carta de resposta fornecendo respostas às perguntas dos revisores e indicando as alterações feitas no artigo para atender aos comentários dos revisores. Na versão revisada do artigo, você DEVE destacar as alterações usando uma cor de fonte diferente (por exemplo, azul ou vermelho).

Atenciosamente,

Rohit

Editor - Journal of Software Engineering Research and Development


------------------------------------------------------
Revisor A:

Este artigo é uma versão extendida de um trabalho anteriormente apresentado no 10th Brazilian Symposium on Systematic and Automated Software Testing (SAST 2025).

O objetivo principal do estudo é avaliar a qualidade do código de teste em projetos baseados em Dart analisando os cheiros de teste identificados nos conjuntos de testes. Para isso, os autores desenvolveram a ferramenta DNose, projetada para detectar cheiros de teste na linguagem Dart. O artigo então apresenta uma avaliação da precisão da ferramenta, seguida por uma análise em grande escala dos cheiros de teste em projetos Dart de código aberto. Finalmente, o estudo investiga a relação entre a presença de cheiros de teste e os sentimentos dos desenvolvedores.

Comparado à versão inicial, esta versão extendida traz contribuições relevantes, incluindo: (i) a adição de 208.372 novas ocorrências de cheiros de teste, e (ii) a incorporação de análise de sentimento baseada em mensagens de commit.

De modo geral, o artigo é bem escrito e fácil de seguir. A versão extendida representa uma melhoria clara em relação à anterior, particularmente devido a uma introdução mais estruturada e um projeto experimental melhor definido.

No entanto, o artigo se beneficiaria de revisões menores para abordar os seguintes pontos:

1) Ambas as versões do artigo se baseiam no mesmo conjunto de dados, compreendendo 5.410 projetos de código aberto e 4.154 clones. Por que, então, o número de cheiros de teste detectados difere entre as versões original e extendida? A ferramenta DNose foi atualizada ou modificada? Isso deve ser esclarecido.

2) O estudo é baseado na hipótese de que a presença de cheiros de teste leva à frustração do desenvolvedor, refletida como sentimento negativo nas mensagens de commit. No entanto, os desenvolvedores tipicamente não têm consciência de que estão introduzindo cheiros de teste. Dado isso, não está claro como o sentimento expresso no momento do commit pode ser diretamente associado à introdução de cheiros de teste. Os autores devem justificar ou esclarecer ainda mais esta suposição.

Recomendação: Revisões Necessárias

------------------------------------------------------



------------------------------------------------------
Revisor B:

Esta versão expandida do artigo apresenta um estudo tripartido: 
(i) uma avaliação empírica de uma ferramenta projetada para identificar cheiros de teste em código de teste Dart, 
(ii) uma investigação empírica em grande escala destinada a avaliar a qualidade geral do código de teste em projetos Dart, e 
(iii) o que os autores descrevem como uma análise da relação entre os sentimentos dos desenvolvedores e os cheiros de teste identificados. 

Dentro deste contexto, a presença e distribuição de cheiros de teste são usadas como proxies primárias para a qualidade do código de teste.

O estudo é baseado na análise de 4.154 repositórios (após filtragem), resultando em um conjunto de dados compreendendo mais de um milhão de ocorrências de cheiros de teste. 

Os resultados indicam que cheiros de teste estão presentes na vasta maioria dos arquivos de teste analisados, destacando sua prevalência generalizada no ecossistema.

Uma das principais forças do artigo reside em seu projeto de pesquisa bem estruturado, que combina desenvolvimento de ferramentas, validação e análise empírica em grande escala. Embora não seja fortemente enfatizado, a introdução da ferramenta DNose para detectar cheiros de teste em Dart representa uma contribuição significativa, particularmente dado o suporte limitado de ferramentas disponível para este ecossistema. Além disso, a precisão da ferramenta é avaliada através de um estudo empírico envolvendo validação manual por múltiplos desenvolvedores com vários níveis de experiência, o que fortalece a confiança na confiabilidade dos resultados relatados.

Dicho isso, a descrição da expansão do conjunto de dados na versão extendida permanece insuficientemente detalhada. 

A versão anterior do artigo relata aproximadamente 907.566 instâncias de cheiros de teste, enquanto a versão atual relata 1.115.938 ocorrências—um aumento de aproximadamente 23%. 

No entanto, ambas as versões parecem se basear no mesmo conjunto de 4.154 repositórios clonados (derivados de 5.410 projetos Dart). Portanto, não está claro como este aumento foi alcançado. O manuscrito não declara explicitamente se a expansão resulta de uma estratégia de mineração "mais profunda" (por exemplo, analisar commits adicionais ou revisões históricas), mudanças no pipeline de detecção (por exemplo, novas heurísticas ou "relaxadas"), ou outras modificações no processo de extração de dados.

Acredito que esclarecer este ponto é importante para avaliar a comparabilidade entre versões (e garantir a reprodutibilidade do estudo). Os autores são encorajados a fornecer uma conta mais detalhada das etapas que levaram ao conjunto de dados expandido.

Minha principal preocupação com a versão extendida relaciona-se à análise da relação entre os sentimentos dos desenvolvedores e cheiros de teste.
O construto latente de interesse (frustração do desenvolvedor ou percepção negativa associada à dívida técnica) é apenas fracamente e indiretamente refletido no proxy escolhido, ou seja, a polaridade de sentimento nas mensagens de commit.

Isso levanta várias ameaças à validade de construto que não são suficientemente discutidas (na seção de ameaças à validade). Mensagens de commit não são projetadas para capturar estados emocionais dos desenvolvedores. 

Elas são tipicamente usadas para documentar alterações de código. Como tal, elas tendem a ser curtas, técnicas e principalmente neutras, frequentemente seguindo modelos padronizados (por exemplo, "corrigir bug", "refatorar teste", "atualizar config"), e em alguns casos são automaticamente geradas (por exemplo, merges ou operações de CI/CD). Mesmo quando o sentimento está presente, raramente é atribuível a uma única causa bem definida.

Consequentemente, há uma lacuna fundamental de inferência no projeto experimental. A análise não permite determinar se os desenvolvedores estavam cientes da presença de cheiros de teste, se tais cheiros causaram alguma forma de frustração, ou se o sentimento expresso (se houver) está realmente relacionado àqueles cheiros. Isso introduz fatores de confusão não observados e limita a interpretabilidade dos resultados. Em minha opinião, a parte de análise de sentimento aparece metodologicamente desconectada do restante do estudo.

De modo geral, deixando de lado a parte de análise de sentimento, que em minha visão parece um pouco deslocada, o artigo apresenta uma contribuição relevante e metodologicamente sólida. Ele combina com sucesso desenvolvimento de ferramentas, validação e avaliação empírica em grande escala, e os resultados provavelmente serão de interesse para o público do periódico. Além disso, a apresentação geral melhorou em comparação com a versão anterior.

Recomendação: Aceitar Submissão

------------------------------------------------------



________________________________________________________________________
Journal of Software Engineering Research and Development