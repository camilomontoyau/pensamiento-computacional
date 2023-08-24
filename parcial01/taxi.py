dia_de_la_semana = input("Ingrese el dia de la semana: ")
hora = int(input("Ingrese la hora: "))
esta_lloviendo = input("Esta lloviendo? (si/no): ")
precio_gasolina = float(input("Ingrese el precio de la gasolina: "))



if esta_lloviendo == 'si': 
  print("Es buen momento para salir a trabajar")
elif dia_de_la_semana == 'sabado' and hora >= 8 and hora <= 19:
  print("No es buen momento para salir a trabajar")
elif hora >= 6 and hora <= 9:
  print("No es buen momento para salir a trabajar")
elif hora >= 15 and hora <= 19:
  print("No es buen momento para salir a trabajar")
elif precio_gasolina >= 15000:
  print("No es buen momento para salir a trabajar")
else:
  print("Es buen momento para salir a trabajar")