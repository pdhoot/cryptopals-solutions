import sys
sys.path.append('../set1')

from chall7 import AES_ECB
from Crypto.Random import get_random_bytes
from base64 import b64encode as be, b64decode as bd

BLOCKSIZE = 16

def unpad(msg, BLOCKS=16):
	l = ord(msg[-1])
	if msg[-l:]==chr(l)*l:
		return msg[:-l]
	else:
		return -1

def oracle(ecb, your_string, unknown_string):
	return ecb.encrypt(your_string+unknown_string)

def get_block_size(ecb, unknown_string):
	cphr = oracle(ecb, 'a', unknown_string)

	i = 2
	while True:
		c = oracle(ecb, 'a'*i, unknown_string)
		if len(c)!=len(cphr):
			cphr = c
			break
		i+=1

	j = i
	while True:
		c = oracle(ecb, 'a'*j, unknown_string)
		if len(cphr)!=len(c):
			return j-i
		j+=1

def byte_at_a_time(ecb, unknown_string, BS):
	BLOCKS = len(oracle(ecb, '', unknown_string))/BS

	message = ''
	for B in xrange(BLOCKS):
		for i in xrange(BS-1, -1, -1):
			cipher = oracle(ecb, 'a'*i, unknown_string)
			for g in xrange(256):
				payload = 'a'*i + message + chr(g)
				c = oracle(ecb, payload, unknown_string)
				if c[BS*B:BS*(B+1)]==cipher[BS*B:BS*(B+1)]:
					message+=chr(g)
					print '[*] Message so far:', message + '\n'
					break
	return message




key = get_random_bytes(BLOCKSIZE)
ecb = AES_ECB(key)

message = '''Um9sbGluJyBpbiBteSA1LjAKV2l0aCBteSByYWctdG9wIGRvd24gc28gbXkg
aGFpciBjYW4gYmxvdwpUaGUgZ2lybGllcyBvbiBzdGFuZGJ5IHdhdmluZyBq
dXN0IHRvIHNheSBoaQpEaWQgeW91IHN0b3A/IE5vLCBJIGp1c3QgZHJvdmUg
YnkK'''

BS =  get_block_size(ecb, bd(message))
msg =  unpad(byte_at_a_time(ecb, bd(message), BS), BS)

print '-'*50 + '\n\n'

if msg==bd(message):
	print "[+] Succesfully decrypted the message!"
else:
	print "[-] Error in decrypting the message!"