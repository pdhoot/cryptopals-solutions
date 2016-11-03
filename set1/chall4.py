from chall3 import decrypt

f = open("4.txt", "r")
msgs = f.read().split('\n')
f.close()

min_score = 1e9
single_xored = ''
orig = ''
for cphrs in msgs:
	(s, k, sc) = decrypt(cphrs.decode("hex"))
	# print sc, repr(s)
	if sc<min_score:
		single_xored = s
		min_score = sc
		KEY = k
		orig = cphrs

print "[*] The string which is single-byte xored is:", orig
print "[*] The decrypted string is:", single_xored
print "[*] The key is:", k, min_score