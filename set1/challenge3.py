from challenge2 import fixed_xor as xor

expected_frequencies = {
    'a':8.497,'b':1.492,'c':2.202,'d':4.253,'e':11.162,'f':2.228,'g':2.015,'h':6.094,'i':7.546,'j':0.153,'k':1.292,'l':4.025,'m':2.406,'n':6.749,'o':7.507,'p':1.929,'q':0.095,'r':7.587,'s':6.327,'t':9.356,'u':2.758,'v':0.978,'w':2.56,'x':0.15,'y':1.994,'z':0.077
}

def freq(arr, chr):
    return arr.count(chr)*1.0/len(arr)

print(freq("abcabcabcabcaaaaaab", 'a'))


ciphertext = "1b37373331363f78151b7f2b783431333d78397828372d363c78373e783a393b3736"

ct_chunked = [ciphertext[i:i+2] for i in range(0, len(ciphertext), 2)]
zero_to_f = [chr(c) for c in range(48, 58)] + [chr(c) for c in range(97, 103)]
all_possible_keys = [a+b for a in zero_to_f for b in zero_to_f]
