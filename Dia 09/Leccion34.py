"""
    Modulo datetime
"""


from datetime import datetime, date

#Hora

# hora = datetime.time(17,35,50,1500)
# print(type(hora))
# print(hora)
# print(hora.minute)

#Dia

# dia = datetime.date(2025,10,17)
# print(dia)
# print(dia.year)
# print(dia.ctime())
# print(dia.today().ctime())

#Datetime
fecha = datetime(2025,5,15,22,23,25,1200)
print(fecha)
fecha = fecha.replace(month=11)
print(fecha)


nacimiento = date(1995, 3, 5)
defuncion = date(2095, 6, 19)
vida = defuncion - nacimiento
print(vida)
print(vida.days)


despierta = datetime(2022, 10, 5, 7, 30)
duerme = datetime(2022, 10, 5, 23, 45)
tiempo = duerme - despierta
print(tiempo)
print(tiempo.seconds)