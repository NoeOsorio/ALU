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

    def run(self, v):
        if v["cs"] == bitarray('10010'):
            v["b"] = v["datoin"]

        elif v["cs"] == bitarray('11100'):
            v["bres"] = v["b"]

        elif v["cs"] == bitarray('11101'):
            v["b"] = v["bres"]

        else:
            return

        print("b <= {}".format(v["b"]))
        return v["b"].to01()
