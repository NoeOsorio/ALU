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

    def run(self, variables):
        cout = bitarray('0')
        cl = bitarray('00')
        negative = False

        if variables.clk == '1':
            if variables.cs == '00001':
                a = int(variables.a.to01(), 2)
                b = int(variables.b.to01(), 2)

                variables.operacion = bitarray(format((a + b), '04b'))

                cl[0] = (variables.a[1] & variables.b[1]) | (
                    variables.a[0] & variables.b[0]) & (variables.a[1] ^ variables.b[1])
                cl[1] = (variables.a[2] & variables.b[2]) | (
                    cl[0] & (variables.a[2] ^ variables.b[2]))
                cout[0] = (variables.a[3] & variables.b[3]) | (
                    cl[1] & (variables.a[3] ^ variables.b[3]))

            elif variables.cs == '00010':
                a = int(variables.a.to01(), 2)
                b = int(variables.b.to01(), 2)
                f = format((a - b), '05b')

                if f.startswith('-'):
                    f = f.replace('-', '')
                    negative = True

                print(f)
                variables.operacion = bitarray(f)
                if (variables.a > variables.b):
                    cout[0] = '1'
                    cl[0] = '1'
                else:
                    cout[0] = '0'
                    cl[0] = '0'

            elif variables.cs == '00011':
                variables.operacion = (variables.a & variables.b)
                cout[0] = '0'
                cl[0] = '0'

            elif variables.cs == '00100':
                variables.operacion = (variables.a | variables.b)
                cout[0] = '0'
                cl[0] = '0'

            elif variables.cs == '00101':
                variables.operacion = (~variables.a)
                cout[0] = '0'
                cl[0] = '0'

            elif variables.cs == '00110':
                variables.operacion = (variables.a ^ variables.b)
                cout[0] = '0'
                cl[0] = '0'

            elif variables.cs == '00111':
                variables.operacion = (variables.a & bitarray('1111'))
                cout[0] = cout[0]
                cl[0] = cl[0]

        variables.rc[3] = cout[0] ^ cl[1]
        variables.rc[2] = ~(variables.operacion[3] | variables.operacion[2]
                            | variables.operacion[1] | variables.operacion[0])
        variables.rc[1] = variables.operacion[3]
        variables.rc[0] = cout[0]

        rc = variables.rc.to01()
        operacion = variables.operacion.to01()

        if negative:
            operacion = '-' + operacion

        return rc, operacion
