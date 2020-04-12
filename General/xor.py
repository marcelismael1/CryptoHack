def xor2string(string,key=13):
    new_st = [chr(key^ord(i)) for i in string]
    return ''.join(new_st)

def xor_block(a,k):
    a= [a[i:i+2] for i in range(0,len(a),2)]
    result = ''
    #result += ''.join([chr(int(i,16)^ord(j)) for i,j in list(zip(a[0:len(k)*2],k))])
    for i in range(0,len(a),len(k)):
        #print (a[i:i+len(k)], 'XOR',k)
        result += ''.join([chr(int(i,16)^ord(j)) for i,j in list(zip(a[i:i+len(k)],k))])
    return result

