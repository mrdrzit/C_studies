segundos = input("Por favor, entre com o número de segundos que deseja converter: ")
segundos = int(segundos)

secsIndia = 3600*24

dias = segundos // secsIndia
segundos1 = segundos % secsIndia
horas = segundos1 // 3600
segs_restantes = segundos % 3600
minutos = segs_restantes // 60 
segs = segs_restantes % 60

print(dias,"dias,",horas,"horas,",minutos,"minutos e",segs,"segundos.")