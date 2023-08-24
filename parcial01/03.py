nombre_primer_nino = input("Ingrese el nombre del primer niño: ")
cantidad_cicatrices_primer_nino = int(input("Ingrese la cantidad de cicatrices del primer niño: "))
nombre_segundo_nino = input("Ingrese el nombre del segundo niño: ")
cantidad_cicatrices_segundo_nino = int(input("Ingrese la cantidad de cicatrices del segundo niño: "))

if cantidad_cicatrices_primer_nino > cantidad_cicatrices_segundo_nino:
  print(nombre_primer_nino + " es el más valiente!")
elif cantidad_cicatrices_primer_nino < cantidad_cicatrices_segundo_nino:
  print(nombre_segundo_nino + " es el más valiente!")
else:
  print("Es un empate!")