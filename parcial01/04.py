cantidad_mascotas = int(input("Ingrese la cantidad de mascotas: "))

if cantidad_mascotas > 1:
  print("Demasidas mascotas :(")
elif cantidad_mascotas == 1:
  especie_mascota = input("Ingrese la especie de la mascota: ")
  if especie_mascota == "gato":
    print("Amo los gatos!")
  else:
    print("No me gustan los " + especie_mascota + "s")
else:
  print("Excelente :)")