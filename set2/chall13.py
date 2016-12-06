import sys
sys.path.append('../set1')

from chall7 import AES_ECB
from chall9 import pad
from Crypto.Random import get_random_bytes
from base64 import b64encode as be, b64decode as bd

key = get_random_bytes(16)
ECB = AES_ECB(key)

def parse(profile):
	vals = profile.split("&")
	d = {}
	print vals
	for v in vals:
		x = v.split('=')
		if len(x)==2:
			d[x[0]] = x[1]
	return d

def profile_for(email):
	global ECB
	email = email.replace("&", '').replace("=", '')
	profile = "email=" + email + "&uid=10&role=user"
	return ECB.encrypt(profile)

def decrypt_profile(profile):
	global ECB
	profile = parse(ECB.decrypt(profile))
	if profile["role"]=="admin":
		return True
	else:
		return False


m1 = profile_for("a"*10 + 'admin')
m2 = profile_for("a"*13)

profile = m2[:-16]+m1[16:32]

if decrypt_profile(profile):
	print "[+] Success!"
else:
	print "[-] Failure!"