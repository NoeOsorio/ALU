from bitarray import bitarray


class DirVal:
    # def __init__(self, vma, cs):
    #     self.cs = bitarray(cs)  # 5 bits
    #     self.vma = bitarray('00000')
    def __init__(self):
        print("init: {}".format(self.__class__))

    def run(self, v):
        v["vma"] = bitarray('0')
        vma = (~(v["cs"][3]) & v["cs"][2] & v["cs"][1] & ~(v["cs"][0])) | (
            v["cs"][3] & ~(v["cs"][2]) & ~(v["cs"][1]) & ~(v["cs"][0]))
        v["vma"] = vma
        print("vma <= {}".format(v["vma"]))
        return vma.to01()
