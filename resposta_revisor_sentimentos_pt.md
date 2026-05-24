# Resposta ao Revisor: Análise de Sentimentos e Validade de Construto

**Comentário do Revisor:**
*O construto latente de interesse (frustração do desenvolvedor ou percepção negativa associada à dívida técnica) é apenas fracamente e indiretamente refletido no proxy escolhido, ou seja, a polaridade de sentimento nas mensagens de commit. Isso levanta várias ameaças à validade de construto que não são suficientemente discutidas. Mensagens de commit não são projetadas para capturar estados emocionais. Elas são tipicamente curtas, técnicas e neutras, e em alguns casos, geradas automaticamente. Consequentemente, há uma lacuna fundamental de inferência. A análise não permite determinar se os desenvolvedores estavam cientes dos cheiros de teste, se tais cheiros causaram frustração, ou se o sentimento expresso está realmente relacionado àqueles cheiros. Em minha opinião, a parte de análise de sentimento aparece metodologicamente desconectada do restante do estudo.*

**Resposta dos Autores:**

Agradecemos profundamente a crítica construtiva do revisor sobre a validade de construto e, em particular, a observação de que a análise de sentimentos parecia metodologicamente desconectada do restante do estudo. Concordamos plenamente que mensagens de commit são primariamente artefatos técnicos, tipicamente curtos ou neutros, e que assumir causalidade estrita entre a introdução de um *test smell* e o sentimento negativo constitui uma lacuna de inferência. Nesta versão revisada, endereçamos essa preocupação em três frentes:

---

## 1. Conexão Narrativa entre as Duas Partes do Estudo (Desconexão Metodológica)

O revisor apontou com precisão que a análise de sentimentos parecia "deslocada" (*misplaced*) em relação à análise técnica de *test smells* (RQ1–RQ4). Para resolver isso, adicionamos um parágrafo de transição explícito ao final da Seção 6.1 (Análise e Discussão) que articula o elo narrativo entre as duas dimensões do estudo:

- As RQ1–RQ4 estabelecem o **panorama técnico** dos *test smells* em Dart: sua distribuição, frequência e padrões de co-ocorrência.
- No entanto, *test smells* não são meramente artefatos estáticos de código — são introduzidos, tolerados e acumulados por **desenvolvedores** trabalhando sob condições reais. Pesquisas anteriores demonstraram que o afeto do desenvolvedor e a qualidade do código estão interligados (Guzman et al., 2014; Lin et al., 2018).
- Portanto, as RQ5–RQ6 estendem a investigação para a **dimensão humana da dívida técnica**, examinando de forma exploratória o contexto emocional que envolve a introdução de *test smells*.

Esse parágrafo de ponte deixa claro que a análise de sentimentos não é um estudo separado, mas uma extensão natural e complementar que adiciona uma lente centrada no humano aos achados técnicos.

---

## 2. Lacuna de Inferência e Enquadramento como Estudo de Co-ocorrência

Conforme apontado por Guzman et al. (2014) e Sinha et al. (2016), determinar emoções em projetos de software é particularmente desafiador porque os desenvolvedores discutem tecnicalidades, o que leva a uma grande maioria de mensagens classificadas como neutras. Além disso, Lin et al. (2018) destaca o risco do jargão técnico (*technical lexicon*) confundir ferramentas de análise de sentimentos.

Reformulamos nossas afirmações no manuscrito para eliminar qualquer alegação de relação de causa e efeito. Agora, enquadramos nossa investigação estritamente como um **estudo observacional de co-ocorrência**. Não afirmamos que o desenvolvedor estava ciente do *test smell* ou que ele causou sua frustração. Em vez disso, propomos que o **ambiente ou contexto de desenvolvimento** que propicia a introdução de um *test smell* (como prazos curtos, dívida técnica acumulada ou tarefas altamente complexas) é o mesmo contexto que frequentemente se manifesta em mensagens de commit com polaridade negativa.

Adicionalmente, reformulamos as próprias **Questões de Pesquisa** para refletir esse enquadramento:
- **RQ5 (revisada):** *"What is the exploratory relationship between the occurrence of different test smells and the overall sentiment score in the analyzed projects?"* — removemos o termo "impact" que sugeria causalidade.
- **RQ6 (revisada):** Ajustamos a descrição para enfatizar a observação de co-ocorrência em vez de associação direta.

---

## 3. Caráter Exploratório e Trabalhos Futuros com IAs Avançadas

Reconhecemos explicitamente que nossa metodologia de extração de sentimentos é **exploratória** e representa um *baseline* inicial. Estudos recentes, como o de Dey et al. (2025), propõem o uso de *Language Models* (LLMs) pré-treinados e específicos do domínio de Engenharia de Software para identificar emoções em artefatos de software com maior precisão. Embora nosso trabalho não empregue essas técnicas avançadas, ele estabelece os **dados iniciais** sobre a co-ocorrência de *test smells* e sentimentos no ecossistema Dart/Flutter, servindo como fundação para que estudos futuros apliquem esses modelos mais sofisticados.

---

## Alterações no manuscrito:

| Alteração | Localização | Destaque |
|---|---|---|
| Parágrafo de ponte conectando análise técnica (RQ1–RQ4) e análise de sentimentos (RQ5–RQ6) | **Seção 6.1**, final da subseção de co-ocorrências | Azul |
| Reformulação das Questões de Pesquisa RQ5 e RQ6 com tom exploratório | **Seção 4.1** (Research Questions) | Azul |
| Fundamentação e reconhecimento da natureza técnica das mensagens de commit | **Seção 6.2** (Sentiment Analysis), parágrafo introdutório | Azul |
| Reconhecimento da lacuna de inferência e limite a co-ocorrência | **Seção 7** (Threats to Validity), Construct Validity | Azul |
| Reconhecimento do caráter exploratório e citação de Dey et al. (2025) como trabalho futuro | **Seção 7** (Threats to Validity), novo parágrafo | Azul |
