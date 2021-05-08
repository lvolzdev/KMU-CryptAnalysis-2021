# -*- coding: utf-8 -*-
"""
==============================
Caesar Cipher Usage
==============================
"""

import Caesar_Lib as caesar
import EngDic_Lib as EngDic
import os, sys


#=== Write Ciphertext Message to a file...
cipher_file_name = 'my_cipher.txt'
if not os.path.exists(cipher_file_name):
    print("File %s does not exist." %(cipher_file_name))
    sys.exit()
inFileObj = open(cipher_file_name)
cipher_msg = inFileObj.read()
inFileObj.close()

#-------
# Exhaustive Key search (Brute force attack)

final_key = -1
for key in range(0,26):
    current_text = caesar.decrypt(cipher_msg, key)
    curr_word_percent = EngDic.PercentEnglishWords(current_text)*100
    print('key = %2d: %s (English: %5.2f %%)' 
        %(key, current_text[:30], curr_word_percent)) # 전체 5글잔데 소수점 이하 2자리로 찍어라
    if EngDic.IsEnglish(current_text):
        final_key = key

# 찍는걸 다 찍지 말고 Percent가 높은 상위 5개 이런 식으로 찍을 수 있나?

if final_key >= 0:
    print('Key = ', final_key)
