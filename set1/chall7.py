import sys
sys.path.append('../set2')

from base64 import b64encode as be, b64decode as bd
from Crypto.Cipher import AES
from chall9 import pad

class AES_ECB():
	def __init__(self, key, pad=True):
		self.ecb = AES.new(key, AES.MODE_ECB)
		self.pad = pad

	def encrypt(self, plaintext):
		if self.pad:
			plaintext = pad(plaintext)
		return self.ecb.encrypt(plaintext)

	def decrypt(self, cipher):
		return self.ecb.decrypt(cipher)


if __name__=="__main__":
	key = "YELLOW SUBMARINE"
	f = open("7.txt", "r")
	cipher = bd(f.read())
	f.close()

	ecb = AES_ECB(key)

	plaintext = ecb.decrypt(cipher)

	print "[*] The plaintext message"
	print "-"*50
	print plaintext