from bitstring import BitArray, BitString
import binascii
# returns an list of lists, with each list consisting of `n` successive elements of `lst`
# if a list cannot be populated with n elements, it will be padded with `\0` 
b64_map = {
    64:"=",0:"A",1:"B",2:"C",3:"D",4:"E",5:"F",6:"G",7:"H",8:"I",9:"J",10:"K",11:"L",12:"M",13:"N",14:"O",15:"P",16:"Q",17:"R",18:"S",19:"T",20:"U",21:"V",22:"W",23:"X",24:"Y",25:"Z",26:"a",27:"b",28:"c",29:"d",30:"e",31:"f",32:"g",33:"h",34:"i",35:"j",36:"k",37:"l",38:"m",39:"n",40:"o",41:"p",42:"q",43:"r",44:"s",45:"t",46:"u",47:"v",48:"w",49:"x",50:"y",51:"z",52:"0",53:"1",54:"2",55:"3",56:"4",57:"5",58:"6",59:"7",60:"8",61:"9",62:"+",63:"/"
}
def chunk_list(lst, n):
    ret_lst = []
    construction_lst = []
    for i in range(len(lst)):
        if(i % n == 0 and i != 0):
            ret_lst.append(construction_lst)
            construction_lst = []
        construction_lst.append(lst[i])
    ret_lst.append(construction_lst)
    if(len(ret_lst[-1])<n):
        for i in range(n-len(ret_lst[-1])):
            ret_lst[-1].append(0)
    return ret_lst

def hexToBase64(hexString):
    byte_string = bytes.fromhex(hexString)
    num_bytes = len(byte_string)
    ba = BitArray(byte_string)
    chunked_byte_string = chunk_list(ba, 6)
    s = []
    for i in range(len(chunked_byte_string)):
        s.append(b64_map[BitString([int(i) for i in chunked_byte_string[i]]).uint])
    encoded_wo_padding = ''.join(s)
    ret_val = encoded_wo_padding
    if(num_bytes%3!=0):
        for i in range(3-(num_bytes%3)):
            ret_val+=('=')
    return ret_val


