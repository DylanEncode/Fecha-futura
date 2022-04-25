import datetime
from datetime import *
fecha_actual = datetime.now()
print("la fecha actual es :",fecha_actual)
print("ve el futuro. agrega dias")
x = int(input(">>"))
fecha_futura = datetime.now() + timedelta(days = x)
print(fecha_futura)
#~si estas en internet esta dylan
