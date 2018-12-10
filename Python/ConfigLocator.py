filename = input("Please enter the filename: --> ")

with open(filename, 'rb') as f:
	s = f.read()
	soffset= s.find(b'\xFE\xFE\xFE\xFE\xFE\xFE\xFE\xFE\xFE\x43')
	sConfigBuffer=soffset+9
	#0044617461
	eOffset = s.find(b'\x00\x44\x61\x74\x61')
	eConfigBuffer=eOffset+5
	print(sConfigBuffer)
	print(eConfigBuffer)
	tSize = eConfigBuffer - sConfigBuffer
	print(tSize)
	buf = buffer(s,sConfigBuffer,tSize)
	#print(buf)
	of = open('outfile.txt', 'wb')
	of.write(buf)
	of.close()
