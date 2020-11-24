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

    def run(self, variables):
        if variables.clk.to01() == '1':
            if variables.cs.to01() == '11110':
                variables.pcout = variables.pcontrol

            elif variables.cs.to01() == '11111':
                pcout = int(variables.pcout.to01(), 2)
                variables.pcout = bitarray(format((pcout + 1), 'b'))

            elif variables.cs.to01() == '11101':
                variables.pcout = variables.pila

        return variables.pcout.to01()
