# Streaming Churn & Customer Retention Analytics

## Sobre o projeto

Este projeto tem como objetivo explorar fatores associados ao cancelamento e à retenção de clientes de plataformas de streaming, utilizando Python para geração, tratamento, análise e visualização de dados.

O projeto foi desenvolvido como parte dos meus estudos em Análise e Desenvolvimento de Sistemas, com foco no desenvolvimento de habilidades práticas em Análise de Dados.

## Objetivos

- Analisar taxas de cancelamento por tipo de plano.
- Comparar cancelamentos entre planos com e sem anúncios.
- Investigar a relação entre satisfação com preço, satisfação com conteúdo e cancelamento.
- Praticar análise exploratória e visualização de dados.
- Comunicar resultados de forma clara e organizada.

## Tecnologias utilizadas

- Python
- Pandas
- NumPy
- Matplotlib
- Git e GitHub

## Base de dados

A base contém 2.000 registros de clientes fictícios e 13 colunas, incluindo:

- Plataforma de streaming
- Tipo de plano
- Presença de anúncios
- Tempo de assinatura
- Satisfação com preço e conteúdo
- Tolerância aos anúncios
- Situação da assinatura
- Motivos ilustrativos de cancelamento e retenção

**Importante:** os dados são inteiramente simulados para fins educacionais. Os padrões encontrados não representam estatísticas reais das plataformas citadas. Algumas relações foram incorporadas artificialmente na geração dos dados, portanto os resultados não permitem concluir relações causais no mundo real.

## Análises realizadas

### 1. Cancelamento por tipo de plano

Na base simulada, as taxas de cancelamento observadas foram:

- Básico com anúncios: 46,0%
- Padrão: 44,4%
- Premium: 40,1%

### 2. Comparação entre planos com e sem anúncios

- Clientes sem anúncios: 42,55% de cancelamento.
- Clientes com anúncios: 46,04% de cancelamento.

A diferença observada foi de 3,49 pontos percentuais. Esse resultado descreve apenas a base simulada e não comprova que os anúncios causam cancelamentos.

### 3. Satisfação com preço e conteúdo

Foram criados gráficos para explorar as taxas de cancelamento de acordo com os níveis de satisfação declarados nos dados simulados.

### 4. Motivos de cancelamento e retenção

Foram analisadas as frequências de categorias ilustrativas de cancelamento e retenção na base simulada.

#### Motivos de cancelamento

- Preço alto: 240 registros.
- Pouco uso da plataforma: 217 registros.
- Excesso de anúncios: 213 registros.
- Insatisfação com o catálogo: 208 registros.

#### Motivos de retenção

- Catálogo de conteúdo: 301 registros.
- Uso compartilhado: 285 registros.
- Tolerância aos anúncios: 276 registros.
- Preço acessível: 260 registros.

#### Limitação da análise

Os motivos foram atribuídos artificialmente durante a geração da base. Portanto, essas frequências não representam respostas reais de clientes nem permitem concluir quais fatores efetivamente causam cancelamento ou retenção.

Em um estudo com dados reais, essas categorias poderiam orientar investigações sobre preço, engajamento, publicidade e satisfação com o conteúdo.

## Estrutura do projeto

```text
streaming-churn-analysis/
├── data/
│   └── streaming_customers.csv
├── imagens/
│   ├── taxa_cancelamento_anuncios.png
│   └── analise_satisfacao.png
├── notebooks/
│   └── analise_churn_retencao.ipynb
├── gerar_dados.py
├── gerar_graficos.py
├── analisar_cancelamentos.py
├── .gitignore
└── README.md
```

## Como executar

1. Instale o Python e as bibliotecas Pandas, NumPy e Matplotlib.
2. Gere a base de dados:

   `python gerar_dados.py`

3. Gere o gráfico de anúncios:

   `python gerar_graficos.py`

4. Gere os gráficos de satisfação:

   `python analisar_cancelamentos.py`

Os comandos pressupõem que as dependências estejam instaladas no ambiente Python utilizado.

## Próximos passos

- Investigar com mais detalhes a tolerância aos anúncios.
- Criar indicadores adicionais e comparar diferentes segmentos de clientes.
- Aprimorar as visualizações e a documentação conforme a evolução do projeto.
- Explorar novas perguntas de negócio utilizando a base simulada.

## Autoria

Projeto acadêmico e de portfólio desenvolvido durante meus estudos em Análise e Desenvolvimento de Sistemas.

