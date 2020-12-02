from bitarray import bitarray


class Stack:

    def __init__(self):
        print("init: {}".format(self.__class__))

    def run(self, v):

        if v["cs"] == bitarray('11100'):
            v["pila"] = v["pcout"]
        else:
            return
        print("pila <= {}".format(v["pila"]))
        return v["pila"].to01()
