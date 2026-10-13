import pandas as pd
import matplotlib.pyplot as plt
from pathlib import Path

# Carregando a base de dados
df = pd.read_csv("data/streaming_customers.csv")

# Calculando a taxa de cancelamento de cada grupo
taxas = (
    df.groupby("has_ads")["subscription_status"]
    .apply(lambda grupo: (grupo == "Cancelado").mean() * 100)
)

# Organizando os nomes para o gráfico
taxas.index = ["Sem anúncios", "Com anúncios"]

# Criando o gráfico
plt.figure(figsize=(8, 5))

barras = plt.bar(
    taxas.index,
    taxas.values,
    color=["steelblue", "darkorange"],
    width=0.55
)

# Adicionando os percentuais sobre as barras
for barra in barras:
    altura = barra.get_height()
    plt.text(
        barra.get_x() + barra.get_width() / 2,
        altura + 0.5,
        f"{altura:.2f}%",
        ha="center",
        fontsize=11
    )

plt.title(
    "Taxa de cancelamento por presença de anúncios",
    fontsize=13
)
plt.ylabel("Taxa de cancelamento (%)")
plt.xlabel("Tipo de plano")
plt.ylim(0, 55)
plt.grid(axis="y", alpha=0.25)
plt.tight_layout()

# Salvando o gráfico na pasta imagens
Path("imagens").mkdir(exist_ok=True)
plt.savefig(
    "imagens/taxa_cancelamento_anuncios.png",
    dpi=300,
    bbox_inches="tight"
)

plt.show()

print("Gráfico salvo na pasta imagens!")