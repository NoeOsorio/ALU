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

    def run(self, v):
        if v["cs"] == bitarray('10110'):
            v["datoin"] = v["datout"]

        elif v["cs"] == bitarray('10101'):
            v["datoin"] = v["operacion"]

        else:
            return

        print("datoin <= {}".format(v["datoin"]))
        return v["datoin"].to01()
