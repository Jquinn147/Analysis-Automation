import os
import struct
import re
from collections import OrderedDict

def readString(myFile,out,counted):
	chars = []
	counter = 0
	flag = 0
	c1 = 0
	x = 0
	outs = []
	outlist = []
	d = []
	ix = 0
	#o2f = open('stringsO.txt', 'wb')
	t = True
	
	size = os.path.getsize("outfile.txt")
	while True:
		c = myFile.read(1)
	
				
		if counter == size:
			#flag +=1
			
			counted = counter
			flag = 1
			#print(d)
			return(d)
		if c == chr(0):
			flag = 1
		
				
		#if (c == chr(0) and flag == 8):
		if c != chr(0):
			out = "".join(chars)
			#print(out)	
			chars.append(c)	
		if c != chr(0) and flag == 1: #Clears chars on each string
						
			out = ""			
			out = "".join(chars)			
			chars = []
			chars.append(c)
			#outs.append(out)
			
			#print(chars)
			
			
			flag = 0
				
			
					
			#return(chars)
			
		#print(chars)
		#outs.append(chars)
		#print(outs)
		
		#print(chars)
		#print(outlist)
		
			 
		d = list(outlist)
		#print(d)
		
		#print("Hit")
		if len(chars) > 0 and c == chr(0):
			str1 = ''.join(chars)
			#print(str1)			
			#print(str1)
			outlist.append(str1)
			
		c1 += 1
		counter +=1
		x += 1
	#return(out)
	#o2f.close()
def decryptString(myInput):
	binstr = myInput
	#print list(binstr)
#print("Config buffer located at index:", ConfigBuffer)
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
	

	#print(output)
	return output
	check=hexEn.decode("hex").encode("base64")
#print list(check)
#	a.rstrip(' \t\r\n\0')
#	print(a)
#	it += 1	
	
	
		
		
filename = input("Please enter the filename: --> ")

with open(filename, 'rb') as f: #Find Config buffer in exe
	s = f.read()
	soffset= s.find(b'\xFE\xFE\xFE\xFE\xFE\xFE\xFE\xFE\xFE\x43')
	sConfigBuffer=soffset+9
	#0044617461
	eOffset = s.find(b'\x00\x44\x61\x74\x61')
	eConfigBuffer=eOffset+5
	#print(sConfigBuffer)
	#print(eConfigBuffer)
	tSize = eConfigBuffer - sConfigBuffer
	#print(tSize)
	buf = buffer(s,sConfigBuffer,tSize)
	#print(buf)
	of = open('outfile.txt', 'wb')
	of.write(buf)
	of.close()
	f.close()

with open('outfile.txt', 'rb') as g: #Read Config Buffer
	it = 0
	notint = "0A"
	aint = int(notint, 16)
	out = ""
	#print(aint)
	a = readString(g, out, it)
	b = len(a)
	c =list(OrderedDict.fromkeys(a))
	#print(a)
	#print(c)
	#b = readString(g, out, it)
	#print(b)
	#print(it)
	#print(out)
	
	deIp = decryptString(c[0])
	Port = bytearray(c[1])	
	EA1 = str(c[2])
	DA1 = decryptString(EA1)
	EA2 = str(c[3])
	DA2 = decryptString(EA2)
	SName = str(c[4])
	DName = str(c[5])
	AFhash = str(c[7])
	ELoc = str(c[9])
	ExName = str(c[10])
	EName = str(c[12])
	extra = str(c[6])
	u1 = str(c[8])
	u2 = str(c[11])
	u3 = str(c[13])
	u4 = str(c[14])
	of2 = open("config", "wb")
	of2.write('Encrypted Ip: ' + str(c[0]) + "\n")
	of2.write('Decrypted Ip: ' + deIp + "\n")
	of2.write('Port(Reverse hex): ' + Port + "\n")
	of2.write('Encrypted Args(1): ' + EA1 + "\n")
	of2.write('Decrypted Args(1): ' + DA1 + "\n")
	of2.write('Encrypted Args(2): ' + EA2 + "\n")
	of2.write('Decrypted Args(2): ' + DA2 + "\n")
	of2.write('Service Name: ' + SName + "\n")
	of2.write('Display Name: ' + DName + "\n")
	of2.write('Affiliate Hash: ' + AFhash + "\n")
	of2.write('Executable Location: ' + ELoc + "\n")
	of2.write('Executable Name: ' + ExName + "\n")
	of2.write('Event Name: ' + EName + "\n")
	of2.write('Extra Data: ' + extra + "\n")
	of2.write('Unknown int 1: ' + u1 + "\n")
	of2.write('Unknown int 2: ' + u2 + "\n")
	of2.write('Unknown int 3: ' + u3 + "\n")
	of2.write('Unknown int 4: ' + u4 + "\n") 
	of2.close()
	print 'Encrypted Ip: ' + str(c[0])
	print 'Decrypted Ip: ' + deIp	
	print 'Port(Reverse hex): ' + Port 
	print 'Encrypted Args(1): ' + EA1
	print 'Decrypted Args(1): ' + DA1
	print 'Encrypted Args(2): ' + EA2
	print 'Decrypted Args(2): ' + DA2
	print 'Service Name: ' + SName
	print 'Display Name: ' + DName
	print 'Affiliate Hash: ' + AFhash
	print 'Executable Location: ' + ELoc
	print 'Executable Name: ' + ExName
	print 'Event Name: ' + EName
	print 'Extra Data: ' + extra
	print 'Unknown int 1: ' + u1
	print 'Unknown int 2: ' + u2
	print 'Unknown int 3: ' + u3
	print 'Unknown int 4: ' + u4
	
	

