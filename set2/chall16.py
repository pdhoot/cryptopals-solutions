import sys
sys.path.append('../set1')

from chall2 import xor
from chall10 import AES_CBC
from Crypto.Random import get_random_bytes

key = get_random_bytes(16)
CBC = AES_CBC(key)
C1 = "comment1=cooking%20MCs;userdata="
C2 = ";comment2=%20like%20a%20pound%20of%20bacon"

def parse(profile):
	vals = profile.split(";")
	d = {}
	for v in vals:
		x = v.split('=')
		if len(x)==2:
			d[x[0]] = x[1]
	return d

def oracle(payload):
	global CBC , C1, C2
	payload = payload.replace(";", '').replace("=", '')
	message = C1 + payload + C2
	return CBC.encrypt(message)

def decrypt_oracle(cipher):
	global CBC
	profile = CBC.decrypt(cipher, True)
	profile = parse(profile)
	print profile
	if profile["admin"]=="true":
		return True
	else:
		return False

cipher = oracle('a'*16)
target = ";admin=true;abc="

final_cipher = cipher[:48] + xor(cipher[48:64], xor(target, C2[:16])) + cipher[64:]

if decrypt_oracle(final_cipher):
	print "[+] Success!"
else:
	print "[-] Failure"