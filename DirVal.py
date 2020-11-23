from bitarray import bitarray


class DirVal:
    def __init__(self, vma, cs):
        self.cs = bitarray(cs)  # 5 bits
        self.vma = bitarray('00000')

    def arq_dir_val(self):
        vma = (~(cs[3]) & cs[2] & cs[1] & ~(cs[0])) |
        (cs[3] & ~(cs[2]) & ~(cs[1]) & ~(cs[0]))

        return self.vma.to01()
