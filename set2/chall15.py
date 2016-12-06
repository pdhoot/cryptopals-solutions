def pkcs7_validation(message):
	l = ord(message[-1])

	if message[-l:]==l*chr(l):
		return True
	else:
		return False


if __name__=="__main__":
	c1 = pkcs7_validation("ICE ICE BABY\x04\x04\x04\x04")
	c2 = pkcs7_validation("ICE ICE BABY\x05\x05\x05\x05")
	c3 = pkcs7_validation("ICE ICE BABY\x01\x02\x03\x04")

	if c1 and not c2 and not c3:
		print "[+] Correct!"
	else:
		print "[-] Incorrect!"