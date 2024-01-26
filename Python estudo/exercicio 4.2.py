velocidade = float (input("Qual velocidade o carro passou? "))

if velocidade > 80:
    multa = (velocidade - 80) * 5
    print(f"Você foi multado R$ {multa:7.2f}!")
else:
    print ("Está no limite de velocidade permitido")
