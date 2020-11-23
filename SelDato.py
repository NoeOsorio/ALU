from bitarray import bitarray


class SelDato:
    def __init__(self, clk, cs, datoin, datout, operacion):
        self.clk = clk
        self.cs = cs  # 5 bits
        self.datoin = bitarray(datoin)  # 4 bits
        self.datout = bitarray(datout)  # 4 bits
        self.operacion = bitarray(operacion)  # 4 bits

    def arq_sel_dato(self):
        if self.clk == '1':

            if self.cs == '10110':
                self.datoin = self.datout

            elif self.cs == '10101':
                self.datoin = self.operacion

        return self.datoin.to01()
