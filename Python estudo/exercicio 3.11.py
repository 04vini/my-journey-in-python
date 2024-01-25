preco = float (input("Digite o preço da mercadoria: "))
desconto = int (input("Digite a porcentagem de desconto: "))
descontoAplicado = preco * desconto/100

print("O desconto que irá ser aplicado na mercadoria é: ", descontoAplicado, " o novo preço de usa mercadoria é: ", preco - descontoAplicado)
