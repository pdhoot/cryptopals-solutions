import sys
sys.path.append('../set1')

from chall7 import AES_ECB
from chall9 import pad
from chall2 import xor
from Crypto.Random import get_random_bytes
from base64 import b64encode as be, b64decode as bd

class AES_CBC():
	def __init__(self, key, IV=None, output_IV=True):
		self.ecb = AES_ECB(key, False)
		self.output_IV = output_IV
		if IV is not None:
			self.IV = IV
		else:
			self.IV = get_random_bytes(16)

	def encrypt(self,message):
		message = pad(message)
		blocks = [self.IV] + [message[i:i+16] for i in xrange(0, len(message), 16)]
		cipher = [self.IV]
		prev = self.IV
		for i in xrange(1, len(blocks)):
			msg = xor(blocks[i], prev)
			prev = self.ecb.encrypt(msg)
			cipher+=[prev]

		if self.output_IV:
			return ''.join(cipher)
		else:
			return ''.join([cipher[i] for i in xrange(1, len(cipher))])

	def decrypt(self, cipher, IV=False):
		if IV:
			cipher = cipher[16:]
		message = []
		blocks = [self.IV] + [cipher[i:i+16] for i in xrange(0, len(cipher), 16)]
		for i in xrange(1,len(blocks)):
			msg = self.ecb.decrypt(blocks[i])
			message+=[xor(msg, blocks[i-1])]

		return ''.join(message)


if __name__=="__main__":
	f = open("10.txt", "r")
	cipher = f.read()
	f.close()

	cipher = bd(cipher)

	cbc = AES_CBC("YELLOW SUBMARINE", '\x00'*16)
	message = cbc.decrypt(cipher)

	print message