import binascii
from bitstring import BitArray, BitString

def fixed_xor(h1,h2):
    bs1 = bytes.fromhex(h1)
    bs2 = bytes.fromhex(h2)
    xord_ints = []
    for i in range(len(bs1)):
        xord_ints.append(bs1[i]^bs2[i])
    xord_bytes = bytes(xord_ints)
    print(__name__)
    return xord_bytes.hex()

if __name__ == "__main__":
        print(fixed_xor("1c0111001f010100061a024b53535009181c","686974207468652062756c6c277320657965"))

