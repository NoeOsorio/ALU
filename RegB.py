from bitarray import bitarray


class RegB:
    def __init__(self, clk, cs, datoin, reset):
        self.clk = clk
        self.cs = cs  # 5 bits
        self.datoin = bitarray(datoin)  # 4 bits
        self.reset = reset
        self.b = bitarray('0000')  # 4 bits
        self.bres = bitarray('0000')

    def impedancia(self):
        if self.reset == '1':
            self.b = bitarray('0000')
        else:

            if self.clk == '1':

                if self.cs == '10010':
                    self.b = self.datoin

                elif self.cs == '11100':
                    self.bres = self.b

                elif self.cs == '11101':
                    self.b = self.bres

            return self.b.to01()
