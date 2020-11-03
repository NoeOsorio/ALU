from Alu4 import Alu4
import re


a = input("a (4 bits): ")
if not re.fullmatch('[10]{4}', a):
    print("Debe ser un numero de 4 bits")
    quit()

b = input("b (4 bits): ")
if not re.fullmatch('[10]{4}', b):
    print("Debe ser un numero de 4 bits")
    quit()

cs = input("cs (5 bits): ")
if not re.fullmatch('[10]{5}', cs):
    print("Debe ser un numero de 5 bits")
    quit()

clk = '1'

alu = Alu4(clk, a, b, cs)
rc, operacion = alu.sumar()

print("Valor de RC: ", rc)
print("Valor de Operacion", operacion)
