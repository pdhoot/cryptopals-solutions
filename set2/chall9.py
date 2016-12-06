def pad(msg, BLOCK=16):
	pad_len = BLOCK-(len(msg)%BLOCK)
	msg+=chr(pad_len)*pad_len
	return msg

if __name__=="__main__":
	M1 = "YELLOW SUBMARINE"
	M2 = pad(M1, 20)
	print "[*]" , repr(M2)
	if M2=="YELLOW SUBMARINE\x04\x04\x04\x04":
		print "[+] Correct!"
	else:
		print "[-] Incorrect!"