import os
try: #Check for output file and remove or create if found
    os.remove("output")
    print("File Removed")
except:
    u = open('output', 'a')
    u.close()	

def read_in_chunks(infile, chunk_size):
    chunk = infile.read(chunk_size)
    while chunk:
	    yield chunk
	    chunk = infile.read(chunk_size)

def findnth(haystack, needle, n):
   
    parts = haystack.split(needle, n+1)
    if len(parts)<=n+1:
	return -1
    return len(haystack)-len(parts[-1])-len(needle) - 77 #Since we're searching for the string inside a DOS file, we need to find start of exe



y = raw_input("Please enter in the file name: ")
z = y.rstrip()
infile = open(z) #Ask for file name
chunk_size = os.path.getsize(z)

g = open('output', 'a')	
needle = '!This'

for chunk in read_in_chunks(infile,chunk_size):
	
	for i in range(0,100):	
		a = findnth(chunk,needle,i)
		if a == -1:
		    break
		print a
		g.write(str(findnth(chunk,needle,i)) + '\n')
	
		i = i + 1
		
		
	g.close();
