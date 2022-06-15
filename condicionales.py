#Es necesario recordar que todo lo que viene del teclado se toma como string
calificacion=int(input("Introduce tu calificación de la az-900: "))

if calificacion<700:
    print("Vees, por no estudiar") # Si es menor a 700 muestra esto
elif calificacion>1000:
    print("mientes, no puedes sacar más de 1000")
else:
    print("Felicidades, pasa por tu certificado") # Se ejecuta si ninguno de los if se cumple

edad= int(input("Introduce tu edad: "))

if edad>=18 and edad <=100:
    print("Bienvenido al mamitas")
elif edad>100:
    print("Si vienes acompañado de tus abuelitos, si te podemos fiar")
elif edad<0:
    print("Ni que fueras viajero del tiempo")
else:
    print("No puedes quedarte eres menor de edad")
