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
	
				
		if counter == size: #If end of buffer is reached, set counted = counter
			counted = counter
			flag = 1
			return(d)
		if c == chr(0): #If Zero character is detected, set a flag to 1.  
			flag = 1
		if c != chr(0):
			out = "".join(chars) #Add chars to output
			chars.append(c)	#chars is the array that holds each individual string
		if c != chr(0) and flag == 1: #If a Zero character has been detected (Flag = 1), Clear chars array and set flag = 0.			
			out = ""			
			out = "".join(chars)			
			chars = []
			chars.append(c)
			flag = 0 
		d = list(outlist)
		#print("Hit") #Debugging
		if len(chars) > 0 and c == chr(0):
			str1 = ''.join(chars)
			outlist.append(str1)	
		#c1 += 1
		counter +=1
		x += 1
		
		

	
	
filename = raw_input("Please enter the filename: --> ")
with open(filename, 'rb') as f: #Find Config buffer in exe
	s = f.read()
	soffset= s.find(b'\x00\x00\x03\x00\x90\x5a\x4d') 
	sConfigBuffer=soffset+7 #Find Start of Config Buffer
	print (sConfigBuffer)	
	#0044617461
	eOffset = s.find(b'\x01\x00\x00\x00\x00\x00\x00\x00\x25')
	print(eOffset) 
	eConfigBuffer=eOffset+50 #Find End of Config Buffer
	tSize = eConfigBuffer - sConfigBuffer #Find Size of Config Buffer
	#print(tSize)
	buf = buffer(s,sConfigBuffer,tSize) #Create Buffer using File as import, start of config buffer, and size of config buffer
	#print(buf)
	of = open('outfile.txt', 'wb') #Write config buffer to file
	of.write(buf)
	of.close()
	f.close()

with open('outfile.txt', 'rb') as g: #Read Config Buffer
	it = 0
	notint = "0A"
	aint = int(notint, 16)
	out = ""
	#print(aint)
	a = readString(g, out, it) #Call ReadString Function to read each config value to a buffer, output is returned to a
	b = len(a) #obtain length of list holding all config values
        
	c =list(OrderedDict.fromkeys(a)) #Creates an orderedDict list of config values
	#print(c)
	deIp = (c[0]) # Call String Decryption function on encrypted values
	Port = bytearray(c[1])	
	Portrev = Port.reverse()
	#DA1 = decryptString(EA1)
	#DA2 = decryptString(EA2)
	SName = str(c[2])
	DName = str(c[3])
	extra = str(c[4])
	ID = str(c[5])
        unknown = bytearray(c[6])
        ELoc = str(c[7])
	of2 = open("config", "wb")
	of2.write('URL: ' + deIp + "\n")
	of2.write('Port(Little Endian): ' + Port + "\n")
	#of2.write('Encrypted Args(1): ' + EA1 + "\n")
	#of2.write('Decrypted Args(2): ' + DA2 + "\n")
	of2.write('Service Name: ' + SName + "\n")
	of2.write('Display Name: ' + DName + "\n")
	of2.write('Executable Location: ' + ELoc + "\n")
	of2.write('ID: ' + ID + "\n")
        of2.write('Unknown Int: ' + unknown + "\n")	
	of2.write('Extra Data: ' + extra + "\n")
	of2.close()
	print 'Decrypted Ip: ' + deIp	
	print 'Port(Little Endian): ' + Port 
	
	#print 'Decrypted Args(1): ' + DA1
	#print 'Decrypted Args(2): ' + DA2
	print 'Service Name: ' + SName
	print 'Display Name: ' + DName
	print 'Executable Location: ' + ELoc
	print 'ID: ' + ID
	print 'Unknown Int: ' + unknown	
	print 'Extra Data: ' + extra
	
