import socket
from threading import *
import zlib
import time

serversocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
host = "192.168.1.108"
port = 7721
print (host)
print (port)
serversocket.bind((host, port))
#serversocket.settimeout(30)
#filename = input("Please enter in the output filename: --> ")
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
            output = open("output", "a+b")   
            	
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
            Reply = input("Would you like to send a Command? (Y/N) --> ")
            if (Reply == "Y" or Reply == "y"):
                print("[+] Command List:\n [o] 1. Session\n \t[-] Session_Shutdown - eaeeccd3b87890909080909090d8fcbff4a4909090f890bf\n \t[-] Session_Reboot - eaeeccd3b87890909080909090d8fcbff49e909090F690c4\n \t[-] Session_logoff - eaeeccd3b87890909080909090d8fcbff4a09090900290be\n")
                strR = input("Command: ")
                Command = strR
                if (Command == "1"):
                    option = input("[+] Would you like to \n 1. Shutdown\n 2. Reboot\n 3. Logoff\n")
                    if (option == "1"):
                        print("[+] Shutting Down")
                        b = bytearray.fromhex("eaeeccd3b87890909080909090d8fcbff4a4909090f890bf")
                        print(b)
                        self.sock.send(b)
                    elif (option == "2"):
                        print("[+] Rebooting")
                        b = bytearray.fromhex("eaeeccd3b87890909080909090d8fcbff49e909090F690c4")
                        self.sock.send(b)
                    elif (option == "3"):      
                        print("[+] Logging off")
                        b = bytearray.fromhex("eaeeccd3b87890909080909090d8fcbff4a09090900290be")
                        self.sock.send(b)
                hexR = bytearray.fromhex(strR)
                self.sock.send(hexR)
            elif (Reply == "n" or Reply == "N"):
                print("Ok, no response.")
            else:
                print("You didn't enter Y/N")
            #self.sock.send(b'\xEA\xEE\xCC\xD3\xB8\xaa')
		#output.write(pkt)  
       
        time.sleep(10)     
    
serversocket.listen(5)
print ('server started and listening')
while 1:
    clientsocket, address = serversocket.accept()
    client(clientsocket, address)
