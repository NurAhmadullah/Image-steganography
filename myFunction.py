def set1(n,pos):
    return n|(1 << (pos-1))


def set0(n,pos):
    return n& ~(1 << (pos-1))

def get_bit(n,pos):
    if n & (1 << (pos-1)):
        return 1
    else:
        return 0

def get_xor(a,b):
    if (a and not b) or (not a and b):
        return True
    else:
        return False





def txt_to_bin(txt):
    txt_bit = ""
    for x in txt:
        b = format(ord(x),'b')
        dst = 8 - len(b)
        b = '0'*dst + b
        txt_bit += b
    return txt_bit





def bin_to_txt(txt_bit):
    cntr = 0
    ascii_val = 0
    txt = ""
    for c in txt_bit:
        x = ord(c) - ord('0')
        cntr += 1
        p = 8 - cntr
        this_chr = x * (2**p)
        ascii_val += this_chr
        
        
        if cntr == 8:
            txt += chr(ascii_val)
            cntr = 0
            ascii_val = 0
    return txt






def get_pos_array(txt):
    txt_bit = txt_to_bin(txt)
    
    pos_array = []
    cntr = 0
    pos = 0
    for c in txt_bit:
        x = ord(c) - ord('0')
        cntr += 1
        p = 3 - cntr
        pos += x * (2**p)
        if cntr == 3:
            if pos == 0:
                pos = 7
            pos_array.append(pos)
            cntr = 0
            pos = 0
    return pos_array







