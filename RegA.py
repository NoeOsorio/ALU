from bitarray import bitarray


class RegA:
    def __init__(self):
        print("init: {}".format(self.__class__))

    def run(self, variables):
        if variables.cs == '10001':
            variables.a = variables.datoin

        elif variables.cs == '11100':
            variables.ares = variables.a

        elif variables.cs == '11101':
            variables.a = variables.ares
        return variables.a.to01()
