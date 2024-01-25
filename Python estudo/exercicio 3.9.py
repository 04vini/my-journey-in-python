dia = int (input("Insira a quantidade de dias:"))
hora = int (input("insira a hora:"))
minuto = int (input("insira o minuto"))
segundo = int (input ("insira o segundo"))
dia = dia * 24 * 60 * 60
hora = hora * 60 * 60
minuto = minuto * 60

print("a quantidade de segundos que voce tem é: ", dia + hora + minuto + segundo)