import os
DropPath = "Dropped"
if not os.path.exists(DropPath):
   os.makedirs(DropPath)
def read_in_chunks(infile, chunk_size): #Chunking Function
    while True:
	chunk = infile.read(chunk_size)
	if chunk:
	    yield chunk
	else:
	    break



y = raw_input("Please enter in the file name: ")
z = y.rstrip()
infile = open(z) #input file
sizeOfFile = os.path.getsize(z) #Get Size of File
print (sizeOfFile)
SecondInput = open("output","rb") #Open output of Wrapper.py
theInts = []
for val in SecondInput.read().split():
    theInts.append(int(val))
SecondInput.close() #Obtain File offsets
s = infile.read()
print (theInts[2]) #debugging
for i in range(0,40):
	print i #debugging
	int0 = theInts[i]
	try:
	    int1 = int(theInts[i+1]) - 1 #Obtain size of file and start/end point
	
	    print "int0 = %d" % (int0)
	    print "int1 = %d" % (int1)
	
	    int3 = int1 - int0

	    t = buffer(s,int0,int3)
	    ofile = ("%s/%d.file" % (DropPath,i))
	    print (ofile)
	    outfile = open("%s.file" % ofile, 'wb' )
	    outfile.write(t)
	    outfile.close()
	    
	except ValueError: #End of file exception handler
	    int4 = sizeOfFile - int0
	    t = buffer(s,int0,int4)
	    ofile = ("%s/%d.file" % (DropPath,i))
	    print (ofile)
	    outfile = open("%s.file" % ofile, 'wb' )
	    outfile.write(t)
	    outfile.close()
	    
	except IndexError:
	   int4 = sizeOfFile - int0
	   t = buffer(s,int0,int4)
	   ofile = ("%s/%d.file" % (DropPath,i))
	   print (ofile)
	   outfile = open("%s.file" % ofile, 'wb' )
	   outfile.write(t)
	   outfile.close()
           

	i = i+1
	
	
