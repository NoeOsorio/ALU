from bitarray import bitarray
import re
from PC import PC
from Index import Index
from Stack import Stack
from RegA import RegA
from RegB import RegB
from SelDato import SelDato
from TriEst import TriEst
from SelDir import SelDir
from DirVal import DirVal
from Alu4 import Alu4


variables = {}


def reset():
    # Clock
    variables["clk"] = bitarray('0')
    # Reset
    variables["reset"] = bitarray('0')
    # Pcontrol
    variables["pcontrol"] = bitarray('00000000')
    # PC
    variables["pc"] = bitarray('00000000')
    # Indice
    variables["ix"] = bitarray('00000000')
    # Stack
    variables["pila"] = bitarray('00000000')
    # Pcout
    variables["pcout"] = bitarray('00000000')
    # Rega5
    variables["a"] = bitarray('0000')
    # Regb5
    variables["b"] = bitarray('0000')
    # Direccion
    variables["direccion"] = bitarray('00000000')


pc = PC()
ix = Index()
pila = Stack()
a = RegA()
b = RegB()
sel_dato = SelDato()
tri_est = TriEst()
sel_dir = SelDir()
dir_val = DirVal()
alu = Alu4()


def run(instruction=None, state=0):
    if instruction == None:
        pass
    else:
        print(variables)
        if instruction == bitarray('0000'):
            pass
        elif instruction == bitarray('0001'):
            pass
        elif instruction == bitarray('0010'):
            pass
        elif instruction == bitarray('0011'):
            pass
        elif instruction == bitarray('0100'):
            pass
        elif instruction == bitarray('0101'):
            pass
        elif instruction == bitarray('0110'):
            pass
        elif instruction == bitarray('0111'):
            pass
        elif instruction == bitarray('1000'):
            pass
        elif instruction == bitarray('1001'):
            pass
        elif instruction == bitarray('1010'):
            pass
        elif instruction == bitarray('1011'):
            pass
        elif instruction == bitarray('1100'):
            pass
        elif instruction == bitarray('1101'):
            pass
        elif instruction == bitarray('1110'):
            pass
        elif instruction == bitarray('1111'):
            pass


reset()
run()
