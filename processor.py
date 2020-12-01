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
from UnitControl import Unit_Control


variables = {}


def reset():
    # Interrupción
    variables["irq"] = bitarray('00')
    # Clock
    variables["clk"] = bitarray('0')
    # Reset
    variables["reset"] = bitarray('0')
    # Pcontrol
    variables["pcontrol"] = bitarray('11111111')
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
    # Regb5
    variables["cs"] = bitarray('00000')
    # Estado de unidad de control
    variables["q"] = 0
    # RE
    variables["re"] = bitarray('0000')


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
unit_control = Unit_Control()


def run(instruction=None, state=0):
    if instruction == None:
        pass
    else:
        if instruction == bitarray('0000'):
            alu.run(variables)
            sel_dato.run(variables)
            a.run(variables)
            pc.run(variables)
            sel_dato.run(variables)
            pass
        elif instruction == bitarray('0001'):
            alu.run(variables)
            sel_dato.run(variables)
            a.run(variables)
            pc.run(variables)
            sel_dato.run(variables)
            pass
        elif instruction == bitarray('0010'):
            alu.run(variables)
            sel_dato.run(variables)
            a.run(variables)
            pc.run(variables)
            sel_dato.run(variables)
            pass
        elif instruction == bitarray('0011'):
            alu.run(variables)
            sel_dato.run(variables)
            a.run(variables)
            pc.run(variables)
            sel_dato.run(variables)
            pass
        elif instruction == bitarray('0100'):
            alu.run(variables)
            sel_dato.run(variables)
            a.run(variables)
            pc.run(variables)
            sel_dato.run(variables)
            pass
        elif instruction == bitarray('0101'):
            alu.run(variables)
            sel_dato.run(variables)
            a.run(variables)
            pc.run(variables)
            sel_dato.run(variables)
            pass
        elif instruction == bitarray('0110'):
            pc.run(variables)
            sel_dato.run(variables)
            pc.run(variables)
            sel_dato.run(variables)
            ix.run(variables)
            pc.run(variables)
            sel_dato.run(variables)
            pass
        elif instruction == bitarray('0111'):
            pc.run(variables)
            sel_dato.run(variables)
            a.run(variables)
            pc.run(variables)
            sel_dato.run(variables)
            pass
        elif instruction == bitarray('1000'):
            pc.run(variables)
            sel_dato.run(variables)
            b.run(variables)
            pc.run(variables)
            sel_dato.run(variables)
            pass
        elif instruction == bitarray('1001'):
            alu.run(variables)
            sel_dir.run(variables)
            tri_est.run(variables)
            pc.run(variables)
            sel_dato(variables)
            pass
        elif instruction == bitarray('1010'):
            ix.run(variables)
            pc.run(variables)
            sel_dato(variables)
            pass
        elif instruction == bitarray('1011'):
            pc.run(variables)
            sel_dato(variables)
            # Salto que no se que rayos es
            pc.run(variables)
            pc.run(variables)
            sel_dato(variables)
            pass
        elif instruction == bitarray('1100'):
            pc.run(variables)
            sel_dato(variables)
            # Salto que no se que rayos es
            pc.run(variables)
            pc.run(variables)
            sel_dato(variables)
            pass
        elif instruction == bitarray('1101'):
            pc.run(variables)
            sel_dato(variables)
            # Salto que no se que rayos es
            pc.run(variables)
            pc.run(variables)
            sel_dato(variables)
            pass
        elif instruction == bitarray('1110'):
            pc.run(variables)
            sel_dato(variables)
            # Salto que no se que rayos es
            pc.run(variables)
            pc.run(variables)
            sel_dato(variables)
            pass
        elif instruction == bitarray('1111'):
            pc.run(variables)
            a.run(variables)
            b.run(variables)
            pc.run(variables)
            sel_dato.run(variables)
            pass
        unit_control.run(variables)


reset()
run("1001")
