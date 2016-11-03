from base64 import b64encode as be, b64decode as bd
from Crypto.Cipher import AES

class AES_ECB():
	def __init__(self, key):
		self.ecb = AES.new(key, AES.MODE_ECB)

	def encrypt(self, plaintext):
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