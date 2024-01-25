dias = float (input("Quantos dias você ficou com o carro? "))
kmPercorridos = float(input ("Quantos quilometros percorridos? "))
precoPerKm = kmPercorridos * 0.15
precoPerDia = dias * 60

print ("Você percorreu ", kmPercorridos, " km, durante ", dias, " dias, sendo assim o valor a pagar é ", precoPerKm + precoPerDia)
