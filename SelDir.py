from bitarray import bitarray


class SelDir:
    # def __init__(self, clk, cs, pcout, ix, direccion):
    #     self.clk = clk
    #     self.cs = cs  # 5 bits
    #     self.pcout = bitarray(pcout)  # 8 bits
    #     self.ix = bitarray(ix)  # 8 bits
    #     self.direccion = bitarray('00000000')  # 8 bits
    def __init__(self):
        print("init: {}".format(self.__class__))

    def run(self, variables):
        if variables.cs == '11000':
            variables.direccion = variables.ix
        else:
            variables.direccion = variables.pcout
        return variables.direccion.to01()
