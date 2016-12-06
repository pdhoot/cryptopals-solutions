import sys
sys.path.append('../set1')

from chall7 import AES_ECB
from chall10 import AES_CBC
from random import randint
from Crypto.Random import get_random_bytes

def encryption_oracle(oracle, plaintext):
	plaintext = get_random_bytes(randint(5, 10))+plaintext+get_random_bytes(randint(5, 10))
	return oracle.encrypt(plaintext)

r = randint(0,1)
key = get_random_bytes(16)

if r==0:
	oracle = AES_ECB(key)
else:
	oracle = AES_CBC(key, '\x00'*16, False)

plaintext = 'B'*48

cipher = encryption_oracle(oracle, plaintext)
# print len(cipher)
cipher = [cipher[i:i+16] for i in xrange(0, len(cipher), 16)]

occur = {}

guessed_oracle = 1
for c in cipher:
	if c not in occur:
		occur[c] = 1
	else:
		occur[c]+=1
		guessed_oracle = 0

print "[*] Guessed Oracle",
if guessed_oracle==0:
	print "ECB"
else:
	print "CBC"

if r==guessed_oracle:
	print "[+] Succesfully guessed the oracle!"
else:
	print '[-] Incorrect guess!'
