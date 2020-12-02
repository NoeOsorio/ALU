from bitarray import bitarray


def suma(a, b):
    a = int(a.to01(), 2)
    b = int(b.to01(), 2)
    return bitarray(format((a + b), '04b'))


def resta(a, b):
    a = int(a.to01(), 2)
    b = int(b.to01(), 2)
    f = format((a - b), '05b')

    if f.startswith('-'):
        f = f.replace('-', '')
        negative = True
        print(f)
    return bitarray(f)


class Alu4:
    # def __init__(self, clk, a, b, cs):
        # self.clk = clk  # 1 bit
        # self.a = bitarray(a)  # 4 bits
        # self.b = bitarray(b)  # 4 bits
        # self.cs = cs  # 5 bits
        # self.operacion = bitarray('0000')
        # self.rc = bitarray('0000')
    def __init__(self):
        print("init: {}".format(self.__class__))

    def run(self, v):
        cout = bitarray('0')
        cl = bitarray('00')
        negative = False

        if v["cs"] == bitarray('00001'):
            a = int(v["a"].to01(), 2)
            b = int(v["b"].to01(), 2)

            v["operacion"] = bitarray(format((a + b), '04b'))

            cl[0] = (v["a"][1] & v["b"][1]) | (
                v["a"][0] & v["b"][0]) & (v["a"][1] ^ v["b"][1])
            cl[1] = (v["a"][2] & v["b"][2]) | (
                cl[0] & (v["a"][2] ^ v["b"][2]))
            cout[0] = (v["a"][3] & v["b"][3]) | (
                cl[1] & (v["a"][3] ^ v["b"][3]))

        elif v["cs"] == bitarray('00010'):
            a = int(v["a"].to01(), 2)
            b = int(v["b"].to01(), 2)
            f = format((a - b), '05b')

            if f.startswith('-'):
                f = f.replace('-', '')
                negative = True

            print(f)
            v["operacion"] = bitarray(f)
            if (v["a"] > v["b"]):
                cout[0] = '1'
                cl[0] = '1'
            else:
                cout[0] = '0'
                cl[0] = '0'

        elif v["cs"] == bitarray('00011'):
            v["operacion"] = (v["a"] & v["b"])
            cout[0] = '0'
            cl[0] = '0'

        elif v["cs"] == bitarray('00100'):
            v["operacion"] = (v["a"] | v["b"])
            cout[0] = '0'
            cl[0] = '0'

        elif v["cs"] == bitarray('00101'):
            v["operacion"] = (~v["a"])
            cout[0] = '0'
            cl[0] = '0'

        elif v["cs"] == bitarray('00110'):
            v["operacion"] = (v["a"] ^ v["b"])
            cout[0] = '0'
            cl[0] = '0'

        elif v["cs"] == bitarray('00111'):
            v["operacion"] = (v["a"] & bitarray('1111'))
            cout[0] = cout[0]
            cl[0] = cl[0]

        else:
            return

        v["rc"][3] = cout[0] ^ cl[1]
        v["rc"][2] = ~(v["operacion"][3] | v["operacion"][2]
                       | v["operacion"][1] | v["operacion"][0])
        v["rc"][1] = v["operacion"][3]
        v["rc"][0] = cout[0]

        rc = v["rc"].to01()
        operacion = v["operacion"].to01()

        if negative:
            operacion = '-' + operacion
        print("operacion <= {}".format(v["operacion"]))
        print("rc <= {}".format(v["rc"]))
        return rc, operacion
