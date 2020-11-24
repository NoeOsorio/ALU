from bitarray import bitarray


class DirVal:
    # def __init__(self, vma, cs):
    #     self.cs = bitarray(cs)  # 5 bits
    #     self.vma = bitarray('00000')
    def __init__(self):
        print("init: {}".format(self.__class__))

    def run(self, variables):
        vma = (~(variables.cs[3]) & variables.cs[2] & variables.cs[1] & ~(variables.cs[0])) | (
            variables.cs[3] & ~(variables.cs[2]) & ~(variables.cs[1]) & ~(variables.cs[0]))
        variables["vma"] = vma
        return vma.to01()
