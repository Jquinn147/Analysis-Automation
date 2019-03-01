# Python Version: python3
# Socket Program for encrypted Gh0stRAT Variant
# Works for sample hash: 9364494b0e7882982d15c7e1c970833c54b3b9f95cf24a952257d47b99fc9c3e
# https://www.virustotal.com/#/file/9364494b0e7882982d15c7e1c970833c54b3b9f95cf24a952257d47b99fc9c3e
# In order for you to receive communications, you must change the Host/Port fields and redirect the sample to those ports.

import socket
from threading import *
import zlib

serversocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
host = "192.168.1.108"
port = 7721
print (host)
print (port)
serversocket.bind((host, port))
filename = input("Please enter in the output filename: --> ")
#output = open('PacketCapture', 'a+b')

def Decrypt(packet):
   # print(packet)
    s1 = 0x8A
    s2 = 0x1A
    count = 0
    maxCount = (len(packet) - 1)
    #print maxCount
    output = ""
    var = 0
    x = packet
    
   
    for x in packet:
        try: 	
           
            var = x
		
            varH1 = var + s1
            varH2 = varH1 ^ s2
		
            if (varH2 >= 256):
                varH2 = varH2 ^ 256
            output += hex(varH2).split('x')[-1].zfill(2)
         
        except IndexError:
            print(count)
            print(x[1])
            print("Index Error")
            return output

    return output		


def OpcodeParse(Opcode):
    if (Opcode == "0x65"):
        print("Implant_Heartbeat")
        return 1
    elif (Opcode == "0x66"):
        print("Implant_Login")
        return 1
    else:
        print("Unknown Opcode")
        return 0
class client(Thread):
    def __init__(self, socket, address):
        Thread.__init__(self)
        self.sock = socket
        self.addr = address
        self.start()

    def run(self):
        pkt =''
        divider = "\n~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~\n"
        while 1:
            pkt = self.sock.recv(1024)
            output = open(filename, "a+b")   
            	
            if (pkt.find(b'\xEA\xEE\xCC\xD3\xB8') != -1):
                print ("[+] Received Gh0stRAT variant communications")
			
                buf = list(pkt)
                    #print(buf)
                test = Decrypt(buf)
                print("[+] Decrypted Gh0stRAT packet(compressed) ")
                print(test)
                bStart = test.find('789c')
                #print(bStart)
                bSize = len(test) - bStart
                   
                b2 = bytearray.fromhex(test[bStart:])
                    
                decompress = zlib.decompress(b2)
                output.write(decompress)
                output.write(bytes(divider, "UTF-8"))		
                output.close()
                print("[+] Zlib decompressed buffer")
                print(decompress)
                b3 = decompress[0]
                print("[+] Extracted Opcode")
                print(hex(b3))
                print("[+] Parsing Opcode")
                OpcodeParse(hex(b3))
                 
            else:
                print (pkt)
                #self.sock.send(b'\xEA\xEE\xCC\xD3\xB8\xaa')
		#output.write(pkt)  
        
serversocket.listen(5)
print ('server started and listening')
while 1:
    clientsocket, address = serversocket.accept()
    client(clientsocket, address)
