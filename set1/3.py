expected_frequencies = {
    'a':8.497,'b':1.492,'c':2.202,'d':4.253,'e':11.162,'f':2.228,'g':2.015,'h':6.094,'i':7.546,'j':0.153,'k':1.292,'l':4.025,'m':2.406,'n':6.749,'o':7.507,'p':1.929,'q':0.095,'r':7.587,'s':6.327,'t':9.356,'u':2.758,'v':0.978,'w':2.56,'x':0.15,'y':1.994,'z':0.077
}

def freq_of_letter(sent, letter):
    return sent.count(letter)/len(sent)

print(freq_of_letter("abcabcabcabcaaaaaa", 'a'))