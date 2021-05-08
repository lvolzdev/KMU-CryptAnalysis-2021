# -*- coding: utf-8 -*-
"""
암호분석 2021 - 고전암호 구현

"""

'''
idx = upAlphabet.find('Z')
cipher = upAlphabet[(idx + 3) % 26] # %26 = 0~25의 값만 나오도록.
print(cipher)
'''

'''
plaintext_msg = 'This is a plaintext message.'
key = 3
ciphertext_msg = ''

# 한 글자씩 plaintext 가져오기
for ch in plaintext_msg:
    if ch in upAlphabet:
        idx = upAlphabet.find(ch)
        new_idx = (idx + key) % 26
        cipher_ch = upAlphabet[new_idx]
        ciphertext_msg = ciphertext_msg + cipher_ch
    elif ch in lowAlphabet:
        idx = lowAlphabet.find(ch)
        new_idx = (idx + key) % 26
        cipher_ch = lowAlphabet[new_idx]
        ciphertext_msg = ciphertext_msg + cipher_ch
    else:
        ciphertext_msg = ciphertext_msg + ch # ?

print('Plaintext = ', plaintext_msg)
print('Ciphertext = ', ciphertext_msg)
'''



## 함수로 구현된 시저암호
def ceasar_encrypt(msg, key):
    upAlphabet = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    lowAlphabet = 'abcdefghijklmnopqrstuvwxyz'
    ciphertext_msg = ''
    for ch in msg:
        if ch in upAlphabet:
            idx = upAlphabet.find(ch)
            new_idx = (idx + key) % 26
            cipher_ch = upAlphabet[new_idx]
            ciphertext_msg = ciphertext_msg + cipher_ch
        elif ch in lowAlphabet:
            idx = lowAlphabet.find(ch)
            new_idx = (idx + key) % 26
            cipher_ch = lowAlphabet[new_idx]
            ciphertext_msg = ciphertext_msg + cipher_ch
        else:
            ciphertext_msg = ciphertext_msg + ch # ?

    return ciphertext_msg

def ceasar_decrypt(msg, key):
    upAlphabet = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    lowAlphabet = 'abcdefghijklmnopqrstuvwxyz'
    ciphertext_msg = ''
    for ch in msg:
        if ch in upAlphabet:
            idx = upAlphabet.find(ch)
            new_idx = (idx - key) % 26
            cipher_ch = upAlphabet[new_idx]
            ciphertext_msg = ciphertext_msg + cipher_ch
        elif ch in lowAlphabet:
            idx = lowAlphabet.find(ch)
            new_idx = (idx - key) % 26
            cipher_ch = lowAlphabet[new_idx]
            ciphertext_msg = ciphertext_msg + cipher_ch
        else:
            ciphertext_msg = ciphertext_msg + ch # ? -> 대문자 소문자 다 아니면 그대로.

    return ciphertext_msg

#---- 함수 활용
plaintext_msg = 'This is a plaintext message.'
key = 3

ciphertext = ceasar_encrypt(plaintext_msg, key)
print('Plaintext = ', plaintext_msg)
print('Ciphertext = ', ciphertext)


recovered_msg = ceasar_decrypt(ciphertext, key)
print('Ciphertext = ', ciphertext)
print('Recovered text = ', recovered_msg)


#--- 시저암호의 공격(해독)

for key_guess in range(0,26):
    recovered_guess = ceasar_decrypt(ciphertext, key_guess)
    print('key = ', key_guess, ' : ', recovered_guess)


# --- 컴퓨터가 생각하기에 말이 되는 문장을 추천해주도록 코딩하려면?! 
# 답인지 아닌지 판정을 컴퓨터가 하도록
# 영어 사전 데이터를 지니고 있어서, 영어 사전에 들어있는 단어가 많으면 점수를 많이 주고
# 적으면 점수를 적게 줘서 가장 많은 점수를 가진 문장을 해독된 결과라고 출력.

'''
코딩
1. 영어 사전 가져오기 (dictionary 사전 타입으로)
2. 문장을 단어들로 쪼개기 (공백이나 점 기준으로 split)
3. 단어들의 집합을 만들기
4. 각 단어를 하나 하나 비교해서 있다 없다 확인하고 몇 퍼센트의 단어가 사전에 있는지 확인.
5. 그걸로 점수매김.
'''

# 이 수업을 통해 나는 어떤 걸 얻어갈까 생각해봐..
# 수업들으면서 손으로 타이핑 ~


