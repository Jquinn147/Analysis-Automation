import binascii
import struct

binstr=b"ChDz0Aj1ubS2tra20A/0B6Y="

encoded=binstr.decode("base64").encode("hex")

ba=bytearray(binstr)
print list(ba)
enba = bytearray(encoded)
print list(enba)


