from collections import defaultdict

def detect_ecb(list_ciphertexts):
    block_stats = {}
    for l in lines:
        l_blocks = [l[i:i+32] for i in range(0, len(l), 32)]
        block_stats[l] = defaultdict(lambda: 0)
        for b in l_blocks:
            block_stats[l][b] += 1
    avgs = {}
    for k,v in block_stats.items():
        avgs[k] = sum([k2 for _,k2 in v.items()])/len(v.items())
    max_avg_key = None
    max_avg_value = -1
    for k,v in avgs.items():
        if avgs[k] > max_avg_value:
            max_avg_value = avgs[k]
            max_avg_key = k
    return max_avg_key

f = open("/Users/jacobhammontree/Projects/cryptopals/set1/challenge8.data")
lines = []
for l in f:
    l_no_nl = l.replace("\n", "")
    lines.append(l_no_nl)

print(detect_ecb(l_no_nl))



