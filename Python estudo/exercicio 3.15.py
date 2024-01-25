cigarrosFDia = int (input("Você fuma quantos cigarros por dia? "))
anos = int (input("Há quantos anos você fuma? "))
vidaPerdidaMinutos = 10  * cigarrosFDia
horasPerdidas = vidaPerdidaMinutos / 60
diasPerdidos = horasPerdidas / 24
anosPerdidos = diasPerdidos /365

print("Você fuma ", cigarrosFDia, " cigarros ao dia, já há ", anos, " anos, você perdeu ", vidaPerdidaMinutos,
      "minutos da sua vida, além de ", horasPerdidas," horas de sua vida, além de ", diasPerdidos, " dias perdidos da sua vida, que resultou em ",
      anosPerdidos, " anos de vida perdidos" )
