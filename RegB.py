from bitarray import bitarray


class RegB:
    # def __init__(self, clk, cs, datoin, reset):
    #     self.clk = clk
    #     self.cs = cs  # 5 bits
    #     self.datoin = bitarray(datoin)  # 4 bits
    #     self.reset = reset
    #     self.b = bitarray('0000')  # 4 bits
    #     self.bres = bitarray('0000')
    def __init__(self):
        print("init: {}".format(self.__class__))

    def run(self, variables):
        if variables.cs == '10010':
            variables.b = variables.datoin

        elif variables.cs == '11100':
            variables.bres = variables.b

        elif variables.cs == '11101':
            variables.b = variables.bres

        return variables.b.to01()
