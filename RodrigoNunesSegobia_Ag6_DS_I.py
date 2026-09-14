# Sistema de desconto progressivo para loja online

# Pede ao usuário o valor total da compra
valor_compra = float(input("Digite o valor total da compra: R$ "))

# Define o desconto de acordo com o valor da compra
if valor_compra < 200:
    percentual_desconto = 5
elif valor_compra < 300:
    percentual_desconto = 10
else:
    percentual_desconto = 15

# Calcula o desconto e o valor final da compra
valor_desconto = valor_compra * (percentual_desconto / 100)
valor_final = valor_compra - valor_desconto

# Mostra os resultados na tela
print(f"\nValor da compra: R$ {valor_compra:.2f}")
print(f"Desconto aplicado: {percentual_desconto}%")
print(f"Valor do desconto: R$ {valor_desconto:.2f}")
print(f"Valor final a pagar: R$ {valor_final:.2f}")
