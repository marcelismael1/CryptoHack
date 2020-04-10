import codecs
import Crypto

def ascii_to_chr(a):
	b = [chr(i) for i in a]
	return ''.join(b)

def hex_to_chr(h):
	b = []
	for i in range(0,len(h),2):
		b.append(chr(int(h[i:i+2],16)))
	return ''.join(b)		

def encode_base64(h):
	b64 = codecs.encode(codecs.decode(h, 'hex'), 'base64').decode()
	return b64

def big_int(i):
	i = hex(int(i))[2:]
	b = hex_to_chr(i)
	return b


if __name__ == '__main__':
	# ASCII TASK
	'''
	a = [99, 114, 121, 112, 116, 111, 123, 65, 83, 67, 73, 73, 95, 112, 114, 49, 110, 116, 52, 98, 108, 51, 125] 
	print(ascii_to_chr(a))
	
	#HEX TASK
	
	h = '63727970746f7b596f755f77696c6c5f62655f776f726b696e675f776974685f6865785f737472696e67735f615f6c6f747d'
	print(hex_to_chr(h))
	
	#h = '72bca9b68fc16ac7beeb8f849dca1d8a783e8acf9679bf9269f7bf'
	#print(encode_base64(h))

	
	h = '72bca9b68fc16ac7beeb8f849dca1d8a783e8acf9679bf9269f7bf'
	print(encode_base64(h))
	

	i = 11515195063862318899931685488813747395775516287289682636499965282714637259206269
	print(big_int(i))
	'''
	i = 11515195063862318899931685488813747395775516287289682636499965282714637259206269

	#Crypto.Util.number.bytes_to_long 
	print(Crypto.Util.number.long_to_bytes(i))