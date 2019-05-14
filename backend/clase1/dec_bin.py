# !/user/bin/env python
# -*- coding: utf-8 -*-

#convertir un valor decimal a binario e imprimir el resultado

#Ingresar los datos desde la consola para el usuario
dec = input('ingresa el valor a convertir: ')

#convertir str a int
dec = int(dec)

#conertir a binario
vbin = bin(dec)

#imprimir el resultado
print('valor en binario:', vbin)

#

bin2 = input('ingresa el valor binario a convertir: ')

#conertir a entero
vdec = int(bin2, base=2)

#imprimir el resultado
print('valor en binario:', vdec)


