from bitarray import bitarray


class Stack:
    def __init__(self, clk, cs, reset, pcout):
        self.clk = clk
        self.cs = cs  # 5 bits
        self.reset = reset
        self.pcout = bitarray(pcout)  # 8 bits
        self.pila = bitarray('00000000')  # 8 bits

    def arq_stack(self):
        q = bitarray('00000000')

        if self.reset == '1':
            self.pila = bitarray('00000000')
        else:

            if self.clk == '1':

                if self.cs == '11100':
                    self.pila = self.pcout

        return self.pila.to01()
