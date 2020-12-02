from bitarray import bitarray


class RegA:
    def __init__(self):
        print("init: {}".format(self.__class__))

    def run(self, v):
        if v["cs"] == bitarray('10001'):
            v["a"] = v["datoin"]

        elif v["cs"] == bitarray('11100'):
            v["ares"] = v["a"]

        elif v["cs"] == bitarray('11101'):
            v["a"] = v["ares"]

        else:
            return

        print("a <= {}".format(v["a"]))
        return v["a"].to01()
