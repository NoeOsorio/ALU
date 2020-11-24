from bitarray import bitarray


class SelDato:
    # def __init__(self, clk, cs, datoin, datout, operacion):
    #     self.clk = clk
    #     self.cs = cs  # 5 bits
    #     self.datoin = bitarray(datoin)  # 4 bits
    #     self.datout = bitarray(datout)  # 4 bits
    #     self.operacion = bitarray(operacion)  # 4 bits
    def __init__(self):
        print("init: {}".format(self.__class__))

    def run(self, variables):
        if variables.cs == '10110':
            variables.datoin = variables.datout

        elif variables.cs == '10101':
            variables.datoin = variables.operacion

        return variables.datoin.to01()
