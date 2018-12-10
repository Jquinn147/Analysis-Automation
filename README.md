# Analysis-Automation
These are some of the scripts I use to automate my analysis of malware.

# BASH SCRIPTS

BasicOrg: I get a lot of WannaCry on my honeypot, and I have limited space on my analysis machine.  Therefore, in order to save space, this is a script that renames the malware to numerical names and then separates out WannaCry from the rest of the malware.  WannaCry is saved in its own folder called "WannaCry", while everything else is saved in a folder called "Other".  This script is typically run first on my honeypot.

Dirmaker: This script is a 2 parter. It creates folders and moves all of the individual files into their own folder.  In addition, this script searches through the files while it is sorting them and locates and unpacks any UPX encrypted files.  It saves the path to these files in the txt file UPXFiles.txt.  This script is typically the second bash script to be run.

BasicInfo: Recursively steps through folders performing the following commands on any ".file"s found.  It saves the outputs in text files that it saves in the .file's folder.  This script is typically run last.
  Commands:
     strings *.file;
     file *.file;
     md5sum *.file;
     
# Python Scripts
These 2 python scripts work together to scrape any dropped 'exe' files from a sample.  The order of run-through is Wrapper.py - Chunking.py

Wrapper.py - Identifies the file offset of all exe's in the sample, using the DOS file header.  Saves these offsets into a file called 'output'.

Chunking.py - Steps through the file and scrapes out each exe.  Saves into "Dropped".

# Config Dumper / Encrypted String Decryptor
This is a python script that dumps the worm ZombieBoy's config file.  There's also a script to decrypt the Encrypted strings, however, that script is in its early stages and requires manually copy and pasting any encrypted data.


