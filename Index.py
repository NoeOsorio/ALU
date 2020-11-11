from bitarray import bitarray


class Index:
    def __init_(self, clk, pcontrol, cs, reset):
        self.clk = clk
        self.pcontrol = bitarray(pcontrol)  # 8 bits
        self.cs = cs  # 5 bits
        self.reset = reset
        self.ix = bitarray('00000000')  # 8 bits

    def arq_indice(self):
        if self.reset == '1':
            self.ix = bitarray('00000000')
        else:

            if self.clk == '1':

                if self.cs == '11010':
                    self.ix = self.pcontrol

                elif self.cs == '11011':
                    ix = int(self.ix.to01(), 2)
                    self.ix = bitarray(format((ix + 1), 'b'))

        return self.ix.to01()

