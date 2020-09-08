import sys
import operations

bits_one = "1111"
bits_two = "1010"

if (len(sys.argv) < 2):
    print("No se proporciono arreglos de bits, bits_one será: 1111")
else:
    bits_one = sys.argv[1]
if (len(sys.argv) < 3):
    print("No se proporciono segundo arreglo de bits, bits_two será: 1010")
else:
    bits_two = sys.argv[2]

if (operations.bits(bits_one) == None) or (operations.bits(bits_two) == None):
    print("Bits no validos")
    exit()


print("""
    >>>>>>> Arithmetic Logic Unit <<<<<<<


""")


print("    bits_one: \t{}".format(bits_one))
print("    bits_two: \t{}".format(bits_two))

print("    not bits_one: \t{}".format(operations.bit_not(bits_one)))
print("    not bits_two: \t{}".format(operations.bit_not(bits_two)))

print("    and: \t\t{}".format(operations.bit_and(bits_one, bits_two)))

print("    or: \t\t{}".format(operations.bit_or(bits_one, bits_two)))

print("    xor: \t\t{}".format(operations.bit_xor(bits_one, bits_two)))

print("    sum: \t\t{}".format(operations.bit_sum(bits_one, bits_two)))


"""
Creado por:

Noe Osorio
Mauricio Araujo
Eliuth R. Leon
Victor Rojas

"""