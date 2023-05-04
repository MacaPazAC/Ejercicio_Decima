nombre = str(input("Ingresa tu nombre:"))
apellido = str(input("Ingresa tu primer apellido:"))
run = input("Ingresa tu run: (sin puntos y sin guión)")
anio_nac = int(input("Ingresa tu año de nacimiento:"))
equipo = str(input("Ingresa tu equipo de fútbol favorito:"))
num_favorito = int(input("Ingresa tu número favorito:"))
cant_mascota = int(input("Ingresa la cantidad de mascotas que tienes:"))

a = nombre[0] + nombre[1] #primeras 2 letras nombre
b = apellido[-3] + apellido[-2] + apellido[-1] #últimas 3 letras apellido
largo = round(((len(run))/2)) - 1 #dígito de al medio del run
edad_actual = 2023 - anio_nac
edad = edad_actual - 2 #edad que tienes -2
c = equipo[0] + equipo[1] + equipo[2] #las 3 iniciales equipo
correo = "@duocuc.cl"
guion1 = "_"
guion2 = "_"
 
correo_final = str(a) + str(b) + str(largo) + str(edad) + str(guion1) + str(c) + str(guion2) + str(num_favorito) + str(cant_mascota) + str(correo)

print("Correo final: " + correo_final)