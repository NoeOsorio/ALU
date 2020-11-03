from bitarray import bitarray


class Alu4:
    def __init__(self, clk, a, b, cs):
        self.clk = bitarray(clk) # 1 bit
        self.a = bitarray(a) # 4 bits
        self.b = bitarray(b) # 4 bits
        self.cs = bitarray(cs) # 5 bits
        self.operacion = bitarray('0000')
        self.rc = bitarray('0000')


    def sumar(self):
        cout = bitarray('0')
        cl = bitarray('00')
        negative = False

        if self.clk.to01() == '1':
            if self.cs.to01() == '00001':
                a = int(self.a.to01(), 2)
                b = int(self.b.to01(), 2)
                self.operacion = bitarray(format((a + b), 'b'))

                cl[0] = (self.a[1] & self.b[1]) | (self.a[0] & self.b[0]) & (self.a[1] ^ self.b[1] )
                cl[1] = (self.a[2] & self.b[2]) | (cl[0] & (self.a[2] ^ self.b[2]))
                cout[0] = (self.a[3] & self.b[3]) | (cl[1] & (self.a[3] ^ self.b[3]))

            elif self.cs.to01() == '00010':
                a = int(self.a.to01(), 2)
                b = int(self.b.to01(), 2)
                f = format((a - b), '05b')

                if f.startswith('-'):
                    f = f.replace('-', '')
                    negative = True

                print(f)
                self.operacion = bitarray(f)
                if (self.a > self.b):
                    cout[0] = '1'
                    cl[0] = '1'
                else:
                    cout[0] = '0'
                    cl[0] = '0'

            elif self.cs.to01() == '00011':
                self.operacion = (self.a & self.b)
                cout[0] = '0'
                cl[0] = '0'

            elif self.cs.to01() == '00100':
                self.operacion = (self.a | self.b)
                cout[0] = '0'
                cl[0] = '0'

            elif self.cs.to01() == '00101':
                self.operacion = (~self.a)
                cout[0] = '0'
                cl[0] = '0'

            elif self.cs.to01() == '00110':
                self.operacion = (self.a ^ self.b)
                cout[0] = '0'
                cl[0] = '0'

            elif self.cs.to01() == '00111':
                self.operacion = (self.a & bitarray('1111'))
                cout[0] = cout[0]
                cl[0] = cl[0]

        self.rc[3] = cout[0] ^ cl[1]
        self.rc[2] = ~(self.operacion[3] | self.operacion[2] | self.operacion[1] | self.operacion[0])
        self.rc[1] = self.operacion[3]
        self.rc[0] = cout[0]

        rc = self.rc.to01()
        operacion = self.operacion.to01()

        if negative:
            operacion = '-' + operacion

        return rc, operacion
