from modelo import *

class Menu:

    def agreagar_moto(self) -> None:
        placa = input("ingrese placa: ")
        modelo = input("ingrese modelo: ")
        marca = input("ingrese marca: ")
        cilindraje = input("ingrese cilindraje: ")
        categoria = input("ingrese categoria: ")
        precio_unitario = float(input("ingrese precio: "))
        Compraventa.ingre_moto.append(Moto(placa, modelo, marca, cilindraje, categoria, precio_unitario))

    def menu(self):

        opciones = {1:self.agreagar_moto,2:Compraventa().catalogo_moto}

        while (True):
            print("1. para ingresar moto")
            print("2. catalogo motos")
            print('otro. salir')
            opcion = int(input("elige una opcion: "))
            #Con cualquier otro numero diferente a 1 o 2, salir

            if opcion not in opciones.keys():
                break;
            opciones[opcion]()


if __name__ == '__main__':
    Menu().menu()


