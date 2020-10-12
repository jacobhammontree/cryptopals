from bitstring import BitArray, BitString
import base64, math

# Clipped from https://stackoverflow.com/a/49942785, credit to https://stackoverflow.com/users/1701600/boern
def get_bit(value, n):
    return ((value >> n & 1) != 0)
# End clipped code

def count_bits(num):
    count = 0
    for i in range(0, 8):
        if get_bit(num, i):
            count+=1
    return count

def hamming_distance(s1, s2):
    # Convert both to byte strings
    # s1_arr = [ord(c) for c in s1]
    # s2_arr = [ord(c) for c in s2]
    sum = 0
    for i in range(0, len(s1)):
        sum+=count_bits(s1[i]^s2[i])
    return sum

def solve_multi_xor(b64encoded_ciphertext):

    # get ciphertext in byte form
    b64_bytestring = b64encoded_ciphertext.encode("ascii")
    b64bytes = base64.b64decode(b64_bytestring)
    hamming_distances = {}
    for keysize in range(2,40):
        #hamming_distances[hamming_distance(b64bytes[0:keysize], b64bytes[keysize:keysize+keysize])*1.0/keysize] = keysize
        hamming_distances[sum([hamming_distance(b64bytes[keysize*i:keysize*(i+1)],b64bytes[keysize*(i+1):keysize*(i+2)]) for i in range(0,60)])/(60.0*keysize)] = keysize
    
    likely_key_size = hamming_distances[min(hamming_distances.keys())]

    #chunk the ciphertext into `likely_key_size` blocks with parity
    chunks = []
    for i in range(0,likely_key_size):
        chunks.append([])
        for j in range(0+i, len(b64bytes), likely_key_size):
            chunks[i].append(b64bytes[j])
    
    for i in range(0, len(chunks)):
        print("".join([hex(chunks[i][j])[2:4] if len(hex(chunks[i][j])) == 4 else "0"+hex(chunks[i][j])[2:3] for j in range(0, len(chunks[i]))]))
    return None
    

f = open("/Users/jacobhammontree/Projects/cryptopals/set1//challenge6.data", "r")
b64 = f.read().replace("\n","")
solve_multi_xor(b64)


f.close()