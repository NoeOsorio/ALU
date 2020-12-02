from bitarray import bitarray


class Index:
    def __init__(self):
        print("init: {}".format(self.__class__))

    def run(self, v):
        if v["cs"] == bitarray('11010'):
            v["ix"] = v["pcontrol"]

        elif v["cs"] == bitarray('11011'):
            ix = int(v["ix"].to01(), 2)
            v["ix"] = bitarray(format((ix + 1), 'b'))

        else:
            return
        print("ix <= {}".format(v["ix"]))
        return v["ix"].to01()
