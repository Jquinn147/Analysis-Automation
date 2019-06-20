import socket
import subprocess
import sys
import os.path

remoteIP = "121.41.39.145"
remotePort = 7443
logPath = input("Please enter path to save logfile: ")
logName = input("Please enter log filename: ")

logFile = os.path.join(logPath, logName+".txt")
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
result = sock.connect_ex((remoteIP, remotePort))

try:
  if result == 0:
    print("Connected")
    b = bytearray.fromhex("160000000100000047683073747d944e050000660066")
    sock.send(b)

    while 1:
      out = open(logFile, "a+b")
      pkt = sock.recv(20000)
      print(pkt)
      out.write(pkt)
      out.close()

except KeyboardInterrupt:
  print("You pressed Ctrl+C")
  sys.exit()
