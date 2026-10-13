import pandas as pd
import matplotlib.pyplot as plt

# Carregando a base de dados
df = pd.read_csv("data/streaming_customers.csv")

# Separando clientes que cancelaram e que continuam ativos
df["cancelou"] = (
    df["subscription_status"] == "Cancelado"
)

# Calculando a taxa de cancelamento por satisfação com o preço
taxa_preco = (
    df.groupby("price_satisfaction")["cancelou"]
    .mean() * 100
)

# Calculando a taxa de cancelamento por satisfação com o conteúdo
taxa_conteudo = (
    df.groupby("content_satisfaction")["cancelou"]
    .mean() * 100
)

# Exibindo os resultados no terminal
print("Cancelamento por satisfação com o preço:")
print(taxa_preco.round(2))

print("\nCancelamento por satisfação com o conteúdo:")
print(taxa_conteudo.round(2))

# Criando dois gráficos
fig, eixos = plt.subplots(1, 2, figsize=(12, 5))

eixos[0].bar(
    taxa_preco.index,
    taxa_preco.values
)
eixos[0].set_title("Cancelamento por satisfação com o preço")
eixos[0].set_xlabel("Satisfação (1 = baixa, 5 = alta)")
eixos[0].set_ylabel("Taxa de cancelamento (%)")

eixos[1].bar(
    taxa_conteudo.index,
    taxa_conteudo.values
)
eixos[1].set_title("Cancelamento por satisfação com o conteúdo")
eixos[1].set_xlabel("Satisfação (1 = baixa, 5 = alta)")
eixos[1].set_ylabel("Taxa de cancelamento (%)")

plt.tight_layout()
plt.savefig(
    "imagens/analise_satisfacao.png",
    dpi=300,
    bbox_inches="tight"
)
plt.show()

print("\nGráficos salvos na pasta imagens!")