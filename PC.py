from bitarray import bitarray


class PC:
    def __init__(self, clk, pcontrol, cs, reset, pila):
        self.clk = bitarray(clk)
        self.pcontrol = bitarray(pcontrol) # 8 bits
        self.cs = bitarray(cs) # 5 bits
        self.reset = bitarray(reset)
        self.pila = bitarray(pila) # 8 bits
        self.pcout = bitarray('00000000') # 8 bits

    def arq_pc(self):
        if self.reset.to01() == '1':
            self.cs = bitarray('00000000')
        else:

            if self.clk.to01() == '1':

                if self.cs.to01() == '11110':
                    self.pcout = self.pcontrol

                elif self.cs.to01() == '11111':
                    pcout = int(self.pcout.to01(), 2)
                    self.pcout = bitarray(format((pcout + 1), 'b'))

                elif self.cs.to01() == '11101':
                    self.pcout = self.pila

        return self.pcout.to01()
