from base64 import b64encode as be, b64decode as bd
from chall3 import decrypt
from chall5 import xor

def set_bits(n):
	ct = 0
	while n>0:
		n&=n-1
		ct+=1
	return ct


def hamming_distance(s1, s2):
	hd = 0
	for i, j in zip(s1, s2):
		hd+=set_bits(ord(i)^ord(j))
	return hd

def normalized_hamming_distance(ss):
	BLOCKS = len(ss)
	hd = 0
	for i in xrange(1, BLOCKS-1):
		hd+=hamming_distance(ss[i], ss[i-1])
	hd = float(hd)/BLOCKS/len(ss[0])
	return hd

def get_keysize(cipher):
	min_hd = 1e9
	for k in xrange(2, 40):
		ss = [cipher[i:i+k] for i in xrange(0, len(cipher), k)]
		hd = normalized_hamming_distance(ss)
		if hd<min_hd:
			min_hd = hd
			KEYSIZE = k
	return KEYSIZE


if __name__=="__main__":
	s1 = "this is a test"
	s2 = "wokka wokka!!!"

	if hamming_distance(s1, s2)==37:
		print "[+] Hamming distance calculated correctly!"
	else:
		print "[-] Hamming distance calculated incorrectly!"

	f = open("6.txt", "r")
	cipher = f.read()
	cipher = bd(cipher)
	f.close()
	KEYSIZE = get_keysize(cipher)

	ciphers = [cipher[i::KEYSIZE] for i in xrange(KEYSIZE)]
	key = ''

	for c in ciphers:
		key+=decrypt(c)[1]

	dec_txt = xor(cipher, key)
	print "[*] The keylen is", KEYSIZE
	print "[*] The decrypted text is"
	print dec_txt
	print "[*] The key is", key