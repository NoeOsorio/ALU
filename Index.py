from bitarray import bitarray


class Index:
    def __init__(self):
        print("init: {}".format(self.__class__))

    def run(self, variables):
        if variables.cs == '11010':
            variables.ix = variables.pcontrol

        elif variables.cs == '11011':
            ix = int(variables.ix.to01(), 2)
            variables.ix = bitarray(format((ix + 1), 'b'))
        return variables.ix.to01()
