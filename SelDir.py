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

    def run(self, v):
        if v["cs"] == bitarray('11000'):
            v["direccion"] = v["ix"]
        else:
            v["direccion"] = v["pcout"]

        print("direccion <= {}".format(v["direccion"]))
        return v["direccion"].to01()
