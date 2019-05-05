import binascii
import argparse
import base64
from urllib.parse import unquote

parser = argparse.ArgumentParser()
parser.add_argument("-Hex", help = "Convert Hex to ascii", required=False)
parser.add_argument("-Binary", help="Convert binary to ascii", required=False)
parser.add_argument("-Url", help="Convert url encoding to ascii", required=False)
parser.add_argument("-B64", help="Convert base64 to ascii", required=False)
args, leftovers = parser.parse_known_args()
if args.Binary is not None:
  BinArgs = args.Binary.replace(" ","")
  n = int(BinArgs, 2)
  out = binascii.unhexlify('%x' % n)
  print("String Decoded = %s" % out)

if args.Hex is not None:
  out = bytearray.fromhex(args.Hex).decode()
  print("String Decoded = %s" % out)

if args.Url is not None:
  out = unquote(args.Url)
  print("String Decoded = %s" % out)

if args.B64 is not None:
  out = base64.b64decode(args.B64)
  print("String Decoded = %s" % out)
