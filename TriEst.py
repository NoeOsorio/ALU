from bitarray import bitarray


class TriEst:
    def __init__(self, clk, cs, datout, operacion):
        self.clk = clk
        self.cs = cs  # 5 bits
        self.datout = bitarray(datout)  # 4 bits
        self.operacion = bitarray(operacion)  # 4 bits

    def arq_tri_est(self):
        if self.clk == '1':

            if self.cs == '11000':
                self.datout = self.operacion

            else:
                # el libro lo pone asi:
                # self.datout = 'ZZZZ'
                # pero no se que significan las Z
                self.datout = bitarray('0000')

        return self.datout.to01()
