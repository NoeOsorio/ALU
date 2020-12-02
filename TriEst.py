from bitarray import bitarray


class TriEst:
    # def __init__(self, clk, cs, datout, operacion):
    #     self.clk = clk
    #     self.cs = cs  # 5 bits
    #     self.datout = bitarray(datout)  # 4 bits
    #     self.operacion = bitarray(operacion)  # 4 bits
    def __init__(self):
        print("init: {}".format(self.__class__))

    def run(self, v):
        if v["cs"] == bitarray('11000'):
            v["datout"] = v["operacion"]

        else:
                # el libro lo pone asi:
                # v.datout = 'ZZZZ'
                # pero no se que significan las Z
            v["datout"] = bitarray('0000')

        print("pcout <= {}".format(v["pcout"]))
        return v["datout"].to01()
