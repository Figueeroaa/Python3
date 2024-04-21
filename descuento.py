""" 
programa de descuento
"""

precio=int(input("Ingrese el precio:\n "))
descuento=int(input("Ingresa un descuento:\n "))
# se realiza descuento
resultado=precio*descuento/100
print(resultado)
# descuento con el precio
precio_final=precio-resultado
print(precio_final)
