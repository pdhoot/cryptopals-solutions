BLOCKSIZE = 16

# naive coz it just looks for repition to conclude whether the given ciphertext is ecb
def naive_is_ecb(cipher):
	cipher = [cipher[i:i+BLOCKSIZE] for i in xrange(0, len(cipher), BLOCKSIZE)]
	d = {}
	for c in cipher:
		if c not in d:
			d[c] = 1
		else:
			return True
	return False


if __name__=="__main__":
	f = open("8.txt", "r")
	cipher = f.read().split('\n')
	f.close()

	for c in cipher:
		if naive_is_ecb(c.decode("hex")):
			print "[*] Found cipher", c, "in ecb mode"