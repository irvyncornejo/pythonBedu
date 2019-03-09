# Clase padre 
class Producto():
    def  __init__(self, nombre, cantidad, precio ):
        self.nombre = nombre
        self.cantidad = cantidad
        self.precio = precio
# claseque hereda las  propiedades
class Auto(Producto):
    def __init__(self,nombre, cantidad, precio, marca, modelo):
        Producto.__init__(self,nombre,cantidad,precio)#llamdo a los atributos heredados de la clase padre
        self.marca = marca
        self.modelo = modelo
#Instanciación de objetos 
Camioneta = Auto (

    nombre = "Carga",
    cantidad = 12,
    precio = 2872525.36,
    marca = "Toyota",
    modelo = "Cabina doble"
)

Deportivo = Auto (

    nombre = "A10",
    cantidad = 3,
    precio = 18.898955,
    marca = "Audi",
    modelo = "A10 - 10"
)

print (Camioneta.nombre)
print (Deportivo.nombre)



