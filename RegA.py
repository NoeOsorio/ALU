from bitarray import bitarray


class RegA:
    def __init__(self, clk, cs, datoin, reset):
        self.clk = clk
        self.cs = cs  # 5 bits
        self.datoin = bitarray(datoin)  # 4 bits
        self.reset = reset
        self.a = bitarray('0000')  # 4 bits
        self.ares = bitarray('0000')

    def impedancia(self):
        if self.reset == '1':
            self.a = bitarray('0000')
        else:

            if self.clk == '1':

                if self.cs == '10001':
                    self.a = self.datoin

                elif self.cs == '11100':
                    self.ares = self.a

                elif self.cs == '11101':
                    self.a = self.ares

            return self.a.to01()
