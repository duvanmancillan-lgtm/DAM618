# Ingreso, bienvenida

Name = input("Regalame tu nombre: ")
Edad = input("Regalame tu edad: ")

print(f"Bienvenido {Name}, tienes {Edad} años")
print("_______________________")

#Confirmacion de informacion

while True:
    print("¿Es correcta esta informacion?")
    respuesta = input("Escribe SI o NO: ")

    if respuesta == "SI":
        print("Informacion confirmada")
        break
 
    elif respuesta == "NO":
        Name = input("Regalame tu nombre: ")
        Edad = input("Regalame tu edad: ")
        

    else:
        print ("?")
        

print("_______________________")

#contraseña

contraseña = ""
while contraseña != "123":
    contraseña = input("Ingrese contraseña: ")
if contraseña == "123":
            print ("puede pasar")
else:
    print ("no puede pasar")
