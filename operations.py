# def bit_and(bit_one, bit_two):
    

def bits(bits_string):
    try:
        return int(bits_string, 2)

    except:
        return None

def bit_and(bits_one, bits_two):
    try:
        A = bits(bits_one)
        B = bits(bits_two)
        res = A & B
        return "{0:b}".format(res)
    except:
        return None 

def bit_or(bits_one, bits_two):
    try:
        A = bits(bits_one)
        B = bits(bits_two)
        res =A | B
        return "{0:b}".format(res)
    except:
        return None 

def bit_xor(bits_one, bits_two):
    try:
        A = bits(bits_one)
        B = bits(bits_two)
        res = A ^ B
        return "{0:b}".format(res)
    except:
        return None 

def bit_not(bits_one):
    try:
        A = bits(bits_one)
        res = ~A 
        return "{0:b}".format(res)
    except:
        return None 

def bit_sum(bits_one, bits_two):
    try:
        A = bits(bits_one)
        B = bits(bits_two)
        res = A + B
        return "{0:b}".format(res)
    except:
        return None 

def bit_resta(bits_one, bits_two):
    try:
        A = bits(bits_one)
        B = bits(bits_two)
        res = A - B
        return "{0:b}".format(res)
    except:
        return None 