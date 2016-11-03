from itertools import cycle

def xor(s1, k):
	s2 = ''
	for i, j in zip(s1, cycle(k)):
		s2+=chr(ord(i)^ord(j))
	return s2


if __name__=="__main__":
	s1 = '''Burning 'em, if you ain't quick and nimble
I go crazy when I hear a cymbal'''
	k = "ICE"
	s2 = xor(s1, k)
	ANS = '''0b3637272a2b2e63622c2e69692a23693a2a3c6324202d623d63343c2a26226324272765272a282b2f20430a652e2c652a3124333a653e2b2027630c692b20283165286326302e27282f'''

	if s2.encode("hex")==ANS:
		print "[+] Correct!"
	else:
		print "[-] Incorrect!"