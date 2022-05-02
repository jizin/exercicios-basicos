segundos = (int(input("Por favor, entre com o número de segundos que deseja converter: ")))

dias = segundos // 86400
segsRestantesDia = segundos % 86400
horas = segsRestantesDia // 3600
segsRestantesHora = segundos % 3600
minutos = segsRestantesHora // 60
segsRestantesMinuto = segundos % 60

print(dias, "dias", horas, "horas", minutos, "minutos e", segsRestantesMinuto, "segundos.")