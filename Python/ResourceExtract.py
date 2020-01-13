import pefile
import argparse
import os
from loguru import logger
try:
  os.mkdir("Extracted")
except Exception as e:
    print(e)

parser = argparse.ArgumentParser(description = 'Resource Extraction')
parser.add_argument('--File', help = "Upload a file", required =True)
args = parser.parse_args()

pe = pefile.PE(args.File)

Data = ""
offset = 0x0
size = 0x0
counter = 0
rsrcList = []

for rsrc in pe.DIRECTORY_ENTRY_RESOURCE.entries:
  for entry in rsrc.directory.entries:
    if entry.name is not None:
      offset = entry.directory.entries[0].data.struct.OffsetToData
      size = entry.directory.entries[0].data.struct.Size
      Data = pe.get_memory_mapped_image()[offset:offset+size]
      file = open(f"Extracted/{entry.name.__str__()}","w+b")
      file.write(Data)
      file.close()
      logger.info(f"Extracted {entry.name.__str__()}")
      rsrcList.append(f"Extracted/{entry.name.__str__()}")
    else:
      offset = entry.directory.entries[0].data.struct.OffsetToData
      size = entry.directory.entries[0].data.struct.Size
      Data = pe.get_memory_mapped_image()[offset:offset+size]
      file = open(f"Extracted/rsrc{counter}","w+b")
      file.write(Data)
      file.close()
      logger.info(f"Extracted rsrc{counter}")
      rsrcList.append(f"Extracted/rsrc{counter}")
      counter += 1

print(rsrcList)
