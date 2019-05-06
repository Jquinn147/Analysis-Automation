import os
import struct
from collections import OrderedDict

def parseconf(conf):
    sec = conf.split(b'\0')
    secout1 = list(OrderedDict.fromkeys(sec))
    secout = list(filter(None,secout1))
    return(secout)

filename = input("Please Enter the filename: --> ")
with open(filename, 'rb') as f:
    s = f.read()
    sOffset = s.find(b'\x53\x68\x65\x6C\x6C\x65\x78\x00\x4B')
    sStart = sOffset+128
    sEnd = sStart+1264 
    out = s[sStart:sEnd]
    #$strings = out.decode('ascii').strip()
    #print(strings)
    #print(type(out))
    buf = ""
    it = 0
    a = parseconf(out)
    #print(a)
    C2 = a[0]
    Portplc = bytearray(a[1])
    Port = int.from_bytes(Portplc, "little")
    Group = a[2]
    UnknownString = a[3]
    SN = a[4]
    DN = a[5]
    EN = a[9]
    DropPath = ("{0}/{1}").format(a[7].decode('UTF-8'),a[8].decode('UTF-8'))
    ExtraData = a[6]
    C2Out = ("C2: %s" % C2.decode('UTF-8'))
    print(C2Out)
    PortStr = ("Port: {0}").format(Port)
    print(PortStr)
    GStr = ("Group: {0}").format(Group)
    print(GStr)
    UString = ("Unknown String: {0}").format(UnknownString.decode('UTF-8'))
    Serv = ("Service Name: {0}").format(SN.decode('UTF-8'))
    Disp = ("Display Name: {0}").format(DN.decode('UTF-8'))
    Even = ("Event Name: {0}").format(EN.decode('UTF-8'))
    DPath = ("Dropped Path: {0}").format(DropPath)
    ExData = ("ExtraData: {0}").format(ExtraData)
    print(UString)
    print(Serv)
    print(Disp)
    print(Even)
    print(DPath)
    print(ExData)
    out2 = open("config","w+")
    out2.write(C2Out +"\n")
    out2.write(PortStr +"\n")
    out2.write(GStr +"\n")
    out2.write(UString +"\n")
    out2.write(Serv +"\n")
    out2.write(Even +"\n")
    out2.write(DPath +"\n")
    out2.write(ExData +"\n")
    out2.close()
    
    
        
