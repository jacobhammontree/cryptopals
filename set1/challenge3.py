from challenge2 import fixed_xor as xor
import sys
import math

expected_frequencies = {
    'a':8.497,'b':1.492,'c':2.202,'d':4.253,'e':11.162,'f':2.228,'g':2.015,'h':6.094,'i':7.546,'j':0.153,'k':1.292,'l':4.025,'m':2.406,'n':6.749,'o':7.507,'p':1.929,'q':0.095,'r':7.587,'s':6.327,'t':9.356,'u':2.758,'v':0.978,'w':2.56,'x':0.15,'y':1.994,'z':0.077
}
_legal_characters = [str(hex(i))[2:4] for i in range(65, 91)] + [str(hex(i))[2:4] for i in range (97,123)] + ["32"]
zero_to_f = [chr(c) for c in range(48, 58)] + [chr(c) for c in range(97, 103)]
all_possible_keys = [a+b for a in zero_to_f for b in zero_to_f]

def has_illegal_characters(chunk):
    return any([c not in _legal_characters for c in chunk]), [c not in _legal_characters for c in chunk].count(True)

def freq(arr, chr):
    return arr.count(chr)*1.0/len(arr)

def score_chunk(chunk):
    score = 0

    # check if chunk contains illegal characters
    illegal_character_stats = has_illegal_characters(chunk)
    score += illegal_character_stats[1]

    for k,v in expected_frequencies.items():
        freq_diff = abs(expected_frequencies[k] - (freq(chunk,hex(ord(k.upper()))[2:4]) + freq(chunk,hex(ord(k.lower()))[2:4])))
        score+=freq_diff

    return score
        

def freq_analysis_get_key(ciphertext):
    scores = {}
    for k in all_possible_keys:
        kstr = k*(len(ciphertext)//2)
        plaintext_candidate = xor(kstr, ciphertext)
        pc_chunked = [plaintext_candidate[i:i+2] for i in range(0, len(plaintext_candidate), 2)]
        score = score_chunk(pc_chunked)
        scores[k] = score
    lowest_score = sys.maxsize
    lowest_key = ""
    for k,v in scores.items():
        if float(v) < lowest_score:
            lowest_key = k
            lowest_score = v
    return lowest_key

ciphertext = "1b37373331363f78151b7f2b783431333d78397828372d363c78373e783a393b3736"

print(freq_analysis_get_key(ciphertext))

