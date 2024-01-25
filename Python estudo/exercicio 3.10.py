salario = float (input("Digite o valor de um salário: "))
porcentagem = int (input("Digite a porcentagem de aumento: "))
aumento = salario * porcentagem/100

print("Este e o aumento do seu salário: ", aumento, "Este é seu novo salário: ", salario + aumento)
