x = int(input("Valor de x: "))
y = int(input("Valor de y: "))

print("1.- Suma")
print("2.- Resta")
print("3.- Multiplicacion")
print("4.- Division")
opcion = int(input("Seleccione una opcion: "))

match opcion:
    case 1:
        print(f"La suma es: {x + y}")
    case 2:
        print(f"La resta es: {x + y}")
    case 3:
        print(f"La multiplicacion es: {x * y}")
    case 4:
        print(f"La division es: {x / y}")
    case _:
        print("Opcion incorrecta")