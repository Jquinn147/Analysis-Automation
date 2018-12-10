import binascii
import struct
import re
binstr = input(b"Please enter the IP encrypted string: ") 
print list(binstr)
#s1 = input("Please enter the XOR value(DEC): ")
#s2 = input("Please enter the add/sub value (DEC): ")
s1 = 19
s2 = "6D"
s3 = 256
i2 = int(s2, 16)
#print(i2)
encoded=binstr.decode("base64")
hexEn=encoded.encode("hex")

ba=bytearray(binstr)
#print list(ba)
enba = bytearray(encoded)
hexstring = bytearray.fromhex(''.join('{:02x}'.format(x) for x in enba))

#print list(hexstring)

#print list(enba)
#print len(hexstring)
output = ''
for x in hexstring:
	o1 = x+i2
	o2 = o1 ^ s1
	#print(o1)
	#print(o2)

	if o2 >= 123:
		oFormat = o2 ^ s3
	#char = chr(o2)
	#print(char)
		#print(oFormat)
		char = chr(oFormat)
		#print(char)
		output += char
	else:
		#print(o2)
		char = chr(o2)
		#print(char)
		output += char
	

print(output)
check=hexEn.decode("hex").encode("base64")
#print list(check)
