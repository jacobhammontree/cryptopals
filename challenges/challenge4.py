import challenge3, challenge2
import sys

f = open("/Users/jacobhammontree/Projects/cryptopals/set1/challenge4.data", "r")
lines = []
for l in f:
    lines.append((l[0:len(l)-1]))


lowest_score = sys.maxsize
results = {}
for l in lines:
    analysis = challenge3.freq_analysis_get_key(l)
    key = analysis[0]*(len(l)//2)
    pt_candidate = challenge2.fixed_xor(l, key)
    pt_chunked = [pt_candidate[i:i+2] for i in range(0, len(pt_candidate),2)]
    stringed = ""
    for c in pt_chunked:
        stringed+=chr(int(c,16))
    results[analysis[1]] = stringed

print(results[min(results.keys())], min(results.keys()))
print(sorted(results.keys()))