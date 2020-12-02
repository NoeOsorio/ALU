from bitarray import bitarray
import re
from Alu4 import suma, resta


class Unit_Control:
    def __init__(self):
        print("init: {}".format(self.__class__))

    # def q_0(self, v):
    def run(self, v):
        if v["q"] == 0:
            if v["irq"] == bitarray('10'):
                v["cs"] = bitarray('11100')
                print("cs <= {}".format(v["cs"]))
                v["q"] = 1
                print("q <= {}".format(v["q"]))

            elif v["irq"] == bitarray('01'):
                v["cs"] = bitarray('11100')
                print("cs <= {}".format(v["cs"]))
                v["q"] = 1
                print("q <= {}".format(v["q"]))

            else:
                v["cs"] = bitarray('11111')
                print("cs <= {}".format(v["cs"]))
                v["q"] = 3
                print("q <= {}".format(v["q"]))

            pass
        elif v["q"] == 1:
            if v["irq"] == bitarray('10'):
                v["pcontrol"] = bitarray('01000000')
                print("pcontrol <= {}".format(v["pcontrol"]))
                v["q"] = 1
                print("q <= {}".format(v["q"]))
            elif v["irq"] == bitarray('01'):
                v["pcontrol"] = bitarray('10000000')
                print("pcontrol <= {}".format(v["pcontrol"]))
                v["q"] = 1
                print("q <= {}".format(v["q"]))
            else:
                v["cs"] = bitarray('11110')
                print("cs <= {}".format(v["cs"]))
                v["q"] = 3
                print("q <= {}".format(v["q"]))
            pass
        elif v["q"] == 2:
            v["cs"] = v["cs"]
            print("cs <= {}".format(v["cs"]))
            v["q"] = 5
            print("q <= {}".format(v["q"]))
            pass
        elif v["q"] == 3:
            v["cs"] = bitarray('10110')
            print("cs <= {}".format(v["cs"]))
            v["rw"] = bitarray('1')
            print("rw <= {}".format(v["rw"]))
            v["q"] = 4
            print("q <= {}".format(v["q"]))
            pass
        elif v["q"] == 4:
            v["rw"] = bitarray('0')
            print("rw <= {}".format(v["rw"]))
            if v["datoin"] == bitarray('0000'):
                v["cs"] = bitarray('00001')
                print("cs <= {}".format(v["cs"]))
                v["q"] = 2
                print("q <= {}".format(v["q"]))
            elif v["datoin"] == bitarray('0001'):
                v["cs"] = bitarray('00010')
                print("cs <= {}".format(v["cs"]))
                v["q"] = 5
                print("q <= {}".format(v["q"]))
            elif v["datoin"] == bitarray('0010'):
                v["cs"] = bitarray('00011')
                print("cs <= {}".format(v["cs"]))
                v["q"] = 5
                print("q <= {}".format(v["q"]))
            elif v["datoin"] == bitarray('0011'):
                v["cs"] = bitarray('00100')
                print("cs <= {}".format(v["cs"]))
                v["q"] = 5
                print("q <= {}".format(v["q"]))
            elif v["datoin"] == bitarray('0100'):
                v["cs"] = bitarray('00101')
                print("cs <= {}".format(v["cs"]))
                v["q"] = 5
                print("q <= {}".format(v["q"]))
            elif v["datoin"] == bitarray('0101'):
                v["cs"] = bitarray('00110')
                print("cs <= {}".format(v["cs"]))
                v["q"] = 5
                print("q <= {}".format(v["q"]))
            elif v["datoin"] == bitarray('0110'):
                v["cs"] = bitarray('11111')
                print("cs <= {}".format(v["cs"]))
                v["q"] = 6
                print("q <= {}".format(v["q"]))
            elif v["datoin"] == bitarray('0111'):
                v["cs"] = bitarray('11111')
                print("cs <= {}".format(v["cs"]))
                v["q"] = 7
                print("q <= {}".format(v["q"]))
            elif v["datoin"] == bitarray('1000'):
                v["cs"] = bitarray('11111')
                print("cs <= {}".format(v["cs"]))
                v["q"] = 8
                print("q <= {}".format(v["q"]))
            elif v["datoin"] == bitarray('1001'):
                v["cs"] = bitarray('00111')
                print("cs <= {}".format(v["cs"]))
                v["q"] = 9
                print("q <= {}".format(v["q"]))
            elif v["datoin"] == bitarray('1010'):
                v["cs"] = bitarray('11011')
                print("cs <= {}".format(v["cs"]))
                v["q"] = 0
                print("q <= {}".format(v["q"]))

            elif v["datoin"] == bitarray('1011'):
                v["cs"] = bitarray('11111')
                print("cs <= {}".format(v["cs"]))
                if v["re"][0]:
                    v["q"] = 10
                    print("q <= {}".format(v["q"]))
                else:
                    v["q"] = 0
                    print("q <= {}".format(v["q"]))
            elif v["datoin"] == bitarray('1100'):
                v["cs"] = bitarray('11111')
                print("cs <= {}".format(v["cs"]))
                if v["re"][2]:
                    v["q"] = 10
                    print("q <= {}".format(v["q"]))
                else:
                    v["q"] = 0
                    print("q <= {}".format(v["q"]))
            elif v["datoin"] == bitarray('1101'):
                v["cs"] = bitarray('11111')
                print("cs <= {}".format(v["cs"]))
                if v["re"][1]:
                    v["q"] = 10
                    print("q <= {}".format(v["q"]))
                else:
                    v["q"] = 0
                    print("q <= {}".format(v["q"]))
            elif v["datoin"] == bitarray('1110'):
                v["cs"] = bitarray('11111')
                print("cs <= {}".format(v["cs"]))
                if v["re"][0]:
                    v["q"] = 10
                    print("q <= {}".format(v["q"]))
                else:
                    v["q"] = 0
                    print("q <= {}".format(v["q"]))
            else:
                v["cs"] = bitarray('11101')
                print("cs <= {}".format(v["cs"]))
                v["q"] = 0
                print("q <= {}".format(v["q"]))
            pass
        elif v["q"] == 5:
            v["cs"] = bitarray('10101')
            print("cs <= {}".format(v["cs"]))
            v["q"] = 11
            print("q <= {}".format(v["q"]))
            pass
        elif v["q"] == 6:
            v["cs"] = bitarray('10110')
            print("cs <= {}".format(v["cs"]))
            v["rw"] = bitarray('1')
            print("rw <= {}".format(v["rw"]))
            v["q"] = 12
            print("q <= {}".format(v["q"]))
            pass
        elif v["q"] == 7:
            v["cs"] = bitarray('10110')
            print("cs <= {}".format(v["cs"]))
            v["rw"] = bitarray('1')
            print("rw <= {}".format(v["rw"]))
            v["q"] = 11
            print("q <= {}".format(v["q"]))
            pass
        elif v["q"] == 8:
            v["cs"] = bitarray('10110')
            print("cs <= {}".format(v["cs"]))
            v["rw"] = bitarray('1')
            print("rw <= {}".format(v["rw"]))
            v["q"] = 15
            print("q <= {}".format(v["q"]))
            pass
        elif v["q"] == 9:
            v["cs"] = bitarray('11000')
            print("cs <= {}".format(v["cs"]))
            v["q"] = 0
            print("q <= {}".format(v["q"]))
            pass
        elif v["q"] == 10:
            v["cs"] = bitarray('10110')
            print("cs <= {}".format(v["cs"]))
            v["rw"] = bitarray('1')
            print("rw <= {}".format(v["rw"]))
            v["q"] = 16
            print("q <= {}".format(v["q"]))
            pass
        elif v["q"] == 11:
            v["cs"] = bitarray('10001')
            print("cs <= {}".format(v["cs"]))
            v["rw"] = bitarray('0')
            print("rw <= {}".format(v["rw"]))
            v["q"] = 0
            print("q <= {}".format(v["q"]))
            pass
        elif v["q"] == 12:
            v["cs"] = bitarray('11111')
            print("cs <= {}".format(v["cs"]))
            v["rw"] = bitarray('0')
            print("rw <= {}".format(v["rw"]))
            v["pcontrol"][0] = v["datoin"][0]
            v["pcontrol"][1] = v["datoin"][1]
            v["pcontrol"][2] = v["datoin"][2]
            v["pcontrol"][3] = v["datoin"][3]
            v["pcontrol"][4] = v["pcontrol"][4]
            v["pcontrol"][5] = v["pcontrol"][5]
            v["pcontrol"][6] = v["pcontrol"][6]
            v["pcontrol"][7] = v["pcontrol"][7]
            print("pcontrol <= {}".format(v["pcontrol"]))
            v["q"] = 13
            print("q <= {}".format(v["q"]))
            pass
        elif v["q"] == 13:
            v["cs"] = bitarray('10110')
            print("cs <= {}".format(v["cs"]))
            v["rw"] = bitarray('1')
            print("rw <= {}".format(v["rw"]))
            v["q"] = 14
            print("q <= {}".format(v["q"]))
            pass
        elif v["q"] == 14:
            v["cs"] = bitarray('11010')
            print("cs <= {}".format(v["cs"]))
            v["rw"] = bitarray('0')
            print("rw <= {}".format(v["rw"]))
            v["pcontrol"][0] = v["pcontrol"][0]
            v["pcontrol"][1] = v["pcontrol"][1]
            v["pcontrol"][2] = v["pcontrol"][2]
            v["pcontrol"][3] = v["pcontrol"][3]
            v["pcontrol"][4] = v["datoin"][0]
            v["pcontrol"][5] = v["datoin"][1]
            v["pcontrol"][6] = v["datoin"][2]
            v["pcontrol"][7] = v["datoin"][3]
            print("pcontrol <= {}".format(v["pcontrol"]))
            v["q"] = 0
            print("q <= {}".format(v["q"]))
            pass
        elif v["q"] == 15:
            v["cs"] = bitarray('10010')
            print("cs <= {}".format(v["cs"]))
            v["rw"] = bitarray('0')
            print("rw <= {}".format(v["rw"]))
            v["q"] = 0
            print("q <= {}".format(v["q"]))
            pass
        elif v["q"] == 16:
            v["cs"] = bitarray('10000')
            print("cs <= {}".format(v["cs"]))
            v["f"][0] = v["datoin"][0]
            v["f"][1] = v["datoin"][1]
            v["f"][2] = v["datoin"][2]
            v["f"][3] = False
            v["f"][4] = False
            v["f"][5] = False
            v["f"][6] = False
            v["f"][7] = False
            print("f <= {}".format(v["f"]))
            if not (v["datoin"][3]):
                v["pcontrol"] = suma(v["pcout"], v["f"])
                print("pcontrol <= {}".format(v["pcontrol"]))
                v["q"] = 17
                print("q <= {}".format(v["q"]))
            else:
                v["pcontrol"] = resta(v["pcout"], v["f"])
                print("pcontrol <= {}".format(v["pcontrol"]))
                v["q"] = 17
                print("q <= {}".format(v["q"]))
            pass
        elif v["q"] == 17:
            v["cs"] = bitarray('11110')
            print("cs <= {}".format(v["cs"]))
            v["q"] = 0
            print("q <= {}".format(v["q"]))
            pass
