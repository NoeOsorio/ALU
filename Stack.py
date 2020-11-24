from bitarray import bitarray


class Stack:

    def __init__(self):
        print("init: {}".format(self.__class__))

    def run(self, variables):
        q = bitarray('00000000')
        if variables.cs == '11100':
            variables.pila = variables.pcout
        return variables.pila.to01()
