from bitarray import bitarray


class PC:
    # def __init__(self, clk, pcontrol, cs, reset, pila):
    #     self.clk = bitarray(clk)
    #     self.pcontrol = bitarray(pcontrol)  # 8 bits
    #     self.cs = bitarray(cs)  # 5 bits
    #     self.reset = bitarray(reset)
    #     self.pila = bitarray(pila)  # 8 bits
    #     self.pcout = bitarray('00000000')  # 8 bits
    def __init__(self):
        print("init: {}".format(self.__class__))

    def run(self, v):

        if v["cs"].to01() == bitarray('11110'):
            v["pcout"] = v["pcontrol"]

        elif v["cs"].to01() == bitarray('11111'):
            pcout = int(v["pcout"].to01(), 2)
            v["pcout"] = bitarray(format((pcout + 1), 'b'))

        elif v["cs"].to01() == bitarray('11101'):
            v["pcout"] = v["pila"]

        else:
            return
        print("pcout <= {}".format(v["pcout"]))
        return v["pcout"].to01()
