import sys
sys.path.append('../set1')

from chall7 import AES_ECB
from Crypto.Random import get_random_bytes
from random import randint
from base64 import b64encode as be, b64decode as bd

BLOCKSIZE = 16

def unpad(msg, BLOCKS=16):
	l = ord(msg[-1])
	if msg[-l:]==chr(l)*l:
		return msg[:-l]
	else:
		return -1

def oracle(ecb, random_prefix, your_string, unknown_string):
	return ecb.encrypt(random_prefix+your_string+unknown_string)

def get_block_size(ecb, random_prefix, unknown_string):
	cphr = oracle(ecb,random_prefix, 'a', unknown_string)

	i = 2
	while True:
		c = oracle(ecb,random_prefix, 'a'*i, unknown_string)
		if len(c)!=len(cphr):
			cphr = c
			break
		i+=1

	j = i
	while True:
		c = oracle(ecb,random_prefix, 'a'*j, unknown_string)
		if len(cphr)!=len(c):
			return j-i
		j+=1

def get_len(ecb, random_prefix, unknown_string):
	cphr = oracle(ecb, random_prefix, '', unknown_string)

	c2 = oracle(ecb, random_prefix, 'a', unknown_string)

	ct = 0
	for x, y in zip(cphr, c2):
		if x==y:
			ct+=1
		else:
			break
	ct/=16

	i = 1
	while True:
		c = oracle(ecb,random_prefix, 'a'*i, unknown_string)
		if c[:16*(ct+1)]==cphr[:16*(ct+1)]:
			return i-1
		cphr = c
		i+=1

def byte_at_a_time(ecb,random_prefix, unknown_string, BS, pref):
	BLOCKS = len(oracle(ecb,random_prefix, '', unknown_string))

	message = ''
	cond = True
	while cond:
		for i in xrange(BS-1, -1, -1):
			cipher = oracle(ecb,random_prefix, 'a'*(i+pref), unknown_string)
			mlen = 0
			for g in xrange(256):
				payload = 'a'*(i+pref) + message + chr(g)
				c = oracle(ecb,random_prefix, payload, unknown_string)
				ct = 0
				for x, y in zip(c, cipher):
					if x==y:
						ct+=1
					else:
						break
				if ct>mlen:
					mlen = ct
					G = g
			message+=chr(G)
			print '[*] Message so far:', message + '\n'
			if mlen==len(cipher):
				cond = False
				break
				
	return message




key = get_random_bytes(BLOCKSIZE)
ecb = AES_ECB(key)

random_prefix = get_random_bytes(randint(0,100))

print len(random_prefix)

message = '''Um9sbGluJyBpbiBteSA1LjAKV2l0aCBteSByYWctdG9wIGRvd24gc28gbXkg
aGFpciBjYW4gYmxvdwpUaGUgZ2lybGllcyBvbiBzdGFuZGJ5IHdhdmluZyBq
dXN0IHRvIHNheSBoaQpEaWQgeW91IHN0b3A/IE5vLCBJIGp1c3QgZHJvdmUg
YnkK'''

rand_pref_len = get_len(ecb,random_prefix, bd(message))
print rand_pref_len
BS =  get_block_size(ecb,random_prefix, bd(message))
msg =  unpad(byte_at_a_time(ecb,random_prefix, bd(message), BS, rand_pref_len), BS)

print '-'*50 + '\n\n'

if msg==bd(message):
	print "[+] Succesfully decrypted the message!"
else:
	print "[-] Error in decrypting the message!"