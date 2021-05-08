"""
==============================
Caesar Cipher Usage
==============================
"""

import Caesar_Lib as caesar
import os, sys

#msg = "This is a message."
#=== Read Message from a file...
in_file_name = 'my_text.txt'
print('Current Working Directory: ', os.getcwd())
#--- changing working directory: os.chdir()
if not os.path.exists(in_file_name):
    print("File %s does not exist." %(in_file_name))
    sys.exit()
inFileObj = open(in_file_name)
msg = inFileObj.read()
inFileObj.close()

key = 3
cipher_msg = caesar.encrypt(msg, key)

#=== Write Ciphertext Message to a file...
out_file_name = 'my_cipher.txt'
if os.path.exists(out_file_name):
    print('Overwrite %s? (Y)es or (N)o' %(out_file_name))
    response = input('===>')
    if not response.lower().startswith('y'):
        sys.exit()

outFileObj = open(out_file_name, 'w')
outFileObj.write(cipher_msg)
outFileObj.close()

print("PT = %s..." %(msg[0:30]))
print("CT = %s..." %(cipher_msg[0:30]))

recovered = caesar.decrypt(cipher_msg, key)
print("DT = %s..." %(recovered[0:30]))