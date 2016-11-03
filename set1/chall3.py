from itertools import cycle

FREQ = {' ':18.28846265,'e':10.26665037,'t':7.51699827,'a':6.53216702,'o':6.15957725,'n':5.71201113,'i':5.66844326,'s':5.31700534,'r':4.98790855,'h':4.97856396,'l':3.31754796,\
		'd':3.28292310,'u':2.27579536,'c':2.23367596,'m':2.02656783,'f':1.98306716,'w':1.70389377,'g':1.62490441,'p':1.50432428,'y':1.42766662,'b':1.25888074,'v':0.79611644,\
		'k':0.56096272,'x':0.14092016,'j':0.09752181,'q':0.08367550,'z':0.05128469}


ALPHA = [' ','e','t','a','o','i','n','s','r','h','d','l','u','c','m','f','y','w','g','p','b','v','k','x','q','j','z',\
		 'E','T','A','O','I','N','S','R','H','D','L','U','C','M','F','Y','W','G','P','B','V','K','X','Q','J','Z']

def is_nonprintable(c):
	if ord(c)==10 or (ord(c)>=32 and ord(c)<127):
		return False
	else:
		return True


def score(s):
	d = {}

	for c in ALPHA[:27]:
		d[c] = 0

	tot = 0
	for c in s:
		if c in ALPHA:
			x = c.lower()
			d[x]+=1
			tot+=1
		if is_nonprintable(c):
			return 1e9
	sc = 0
	if tot==0:
		return 1e9
	for x in ALPHA[:27]:
		obs = float(d[x])/tot
		exp = FREQ[x]/100
		sc+=((obs-exp)**2)/exp
	return sc

def single_xor(s, k):
	s1 = ''
	for i, j in zip(s, cycle(k)):
		s1+=chr(ord(i)^ord(j))
	return s1

def decrypt(cipher):
	min_score = 1e9
	dec_txt = ''
	KEY = ''
	for k in xrange(256):
		s = single_xor(cipher, chr(k))
		sc = score(s)
		if sc<=min_score:
			min_score = sc
			dec_txt = s
			KEY = k
	return (dec_txt, chr(KEY), min_score)

if __name__=="__main__":
	cipher = "1b37373331363f78151b7f2b783431333d78397828372d363c78373e783a393b3736"
	msg = decrypt(cipher.decode("hex"))
	print "[*] The decrypted message is:", msg[0]
	print "[*] The key is", msg[1].encode("hex")