import pandas as pd
import matplotlib.pyplot as plt
from pathlib import Path

# Carregando os dados
df = pd.read_csv("data/streaming_customers.csv")

# Separando os clientes cancelados e ativos
cancelados = df[
    df["subscription_status"] == "Cancelado"
]

ativos = df[
    df["subscription_status"] == "Ativo"
]

# Contando os motivos mais frequentes
motivos_cancelamento = (
    cancelados["cancellation_reason"]
    .value_counts()
)

motivos_retencao = (
    ativos["retention_reason"]
    .value_counts()
)

# Exibindo os resultados
print("=== MOTIVOS DE CANCELAMENTO ===")
print(motivos_cancelamento)

print("\n=== MOTIVOS DE RETENÇÃO ===")
print(motivos_retencao)

# Criando dois gráficos
fig, eixos = plt.subplots(1, 2, figsize=(14, 6))

motivos_cancelamento.sort_values().plot(
    kind="barh",
    ax=eixos[0]
)

eixos[0].set_title("Motivos de cancelamento")
eixos[0].set_xlabel("Quantidade de clientes")
eixos[0].set_ylabel("Motivo")

motivos_retencao.sort_values().plot(
    kind="barh",
    ax=eixos[1]
)

eixos[1].set_title("Motivos de retenção")
eixos[1].set_xlabel("Quantidade de clientes")
eixos[1].set_ylabel("Motivo")

plt.tight_layout()

# Salvando o gráfico
Path("imagens").mkdir(exist_ok=True)

plt.savefig(
    "imagens/motivos_cancelamento_retencao.png",
    dpi=300,
    bbox_inches="tight"
)

plt.show()

print("\nGráfico salvo na pasta imagens!")
