from bitarray import bitarray


class SelDir:
    def __init__(self, clk, cs, pcout, ix, direccion):
        self.clk = clk
        self.cs = cs  # 5 bits
        self.pcout = bitarray(pcout)  # 8 bits
        self.ix = bitarray(ix)  # 8 bits
        self.direccion = bitarray('00000000')  # 8 bits

    def arq_sel_dir(self):
        if self.clk == '1':

            if self.cs == '11000':
                self.direccion = self.ix

            else:
                self.direccion = self.pcout

        return self.direccion.to01()
