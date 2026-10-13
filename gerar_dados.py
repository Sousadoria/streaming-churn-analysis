import pandas as pd
import numpy as np
from pathlib import Path

# Permite gerar os mesmos resultados ao executar novamente
np.random.seed(42)

# Quantidade de clientes fictícios
quantidade_clientes = 2000

# Plataformas fictícias para fins de análise
plataformas = ["Netflix", "Prime Video", "Disney+", "HBO Max"]

# Criando os dados dos clientes
dados = pd.DataFrame({
    "customer_id": [
        f"C{i:04d}" for i in range(1, quantidade_clientes + 1)
    ],
    "platform": np.random.choice(plataformas, quantidade_clientes),
    "months_subscribed": np.random.randint(
        1, 49, quantidade_clientes
    ),
    "price_satisfaction": np.random.randint(
        1, 6, quantidade_clientes
    ),
    "content_satisfaction": np.random.randint(
        1, 6, quantidade_clientes
    ),
    "ad_tolerance": np.random.randint(
        1, 6, quantidade_clientes
    ),
})

# Definindo planos fictícios
dados["plan_type"] = np.random.choice(
    ["Básico com anúncios", "Padrão", "Premium"],
    quantidade_clientes,
    p=[0.4, 0.35, 0.25]
)

dados["has_ads"] = dados["plan_type"].eq(
    "Básico com anúncios"
)

# Satisfação com anúncios: escala de 1 a 5
dados["ad_satisfaction"] = np.where(
    dados["has_ads"],
    np.random.randint(1, 6, quantidade_clientes),
    np.nan
)

# Interesse em mudar para um plano sem anúncios
dados["ad_free_upgrade_interest"] = np.where(
    dados["has_ads"],
    np.random.choice(
        ["Sim", "Não"],
        quantidade_clientes,
        p=[0.55, 0.45]
    ),
    "Não se aplica"
)

# Probabilidade artificial de cancelamento.
# Estes relacionamentos são simulados para fins de aprendizado.
probabilidade = (
    0.35
    + (dados["price_satisfaction"] <= 2) * 0.15
    + (dados["content_satisfaction"] <= 2) * 0.15
    + (dados["ad_tolerance"] <= 2) * dados["has_ads"] * 0.12
    - (dados["months_subscribed"] >= 24) * 0.10
)

probabilidade = np.clip(probabilidade, 0.05, 0.90)

dados["subscription_status"] = np.where(
    np.random.random(quantidade_clientes) < probabilidade,
    "Cancelado",
    "Ativo"
)

# Motivos ilustrativos, criados artificialmente
motivos_cancelamento = [
    "Preço alto",
    "Insatisfação com o catálogo",
    "Excesso de anúncios",
    "Pouco uso da plataforma"
]

motivos_retencao = [
    "Preço acessível",
    "Catálogo de conteúdo",
    "Tolerância aos anúncios",
    "Uso compartilhado"
]

dados["cancellation_reason"] = np.where(
    dados["subscription_status"] == "Cancelado",
    np.random.choice(motivos_cancelamento, quantidade_clientes),
    "Não se aplica"
)

dados["retention_reason"] = np.where(
    dados["subscription_status"] == "Ativo",
    np.random.choice(motivos_retencao, quantidade_clientes),
    "Não se aplica"
)

# Criando a pasta de destino, caso necessário
pasta_destino = Path("data")
pasta_destino.mkdir(exist_ok=True)

# Exportando a base para CSV
dados.to_csv(
    pasta_destino / "streaming_customers.csv",
    index=False,
    encoding="utf-8-sig"
)

print("Base de dados criada com sucesso!")
print(f"Quantidade de clientes: {len(dados)}")
print("\nPrimeiros cinco registros:")
print(dados.head())
