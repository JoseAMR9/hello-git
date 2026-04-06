x = int(input("Valor de x: "))
y = int(input("Valor de y: "))

print("1.- Suma")
print("2.- Resta")
print("3.- Multiplicacion")
print("4.- Division")
opcion = int(input("Elija una opcion: "))

match opcion:
    case 1:
        print(f"La suma es: {x + y}")