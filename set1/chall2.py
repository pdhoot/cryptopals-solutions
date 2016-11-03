from base64 import b64encode as be, b64decode as bd

def xor(s1, s2):
	s3 = ''
	for i, j in zip(s1, s2):
		s3+=chr(ord(i)^ord(j))
	return s3

if __name__=="__main__":
	s1 = '1c0111001f010100061a024b53535009181c'
	s2 = '686974207468652062756c6c277320657965'
	s3 = xor(s1.decode("hex"), s2.decode("hex"))

	ANS = '746865206b696420646f6e277420706c6179'
	if s3.encode("hex")==ANS:
		print "[+] Correct!"
	else:
		print "[-] Incorrect!"