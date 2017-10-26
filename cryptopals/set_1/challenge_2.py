#
#	By:		dpetrov
#	Usage:	Fixed XOR
#

from binascii import unhexlify
from numpy import logical_xor

def		fixedXOR(str1, str2, show=True):
	byte = unhexlify(str1)
	xor = int(byte,base=16) ^ int(str2,base=16)
	if show:
		print("In byte: " + byte)
		print("In base64" + xor)
	return xor

# Example ->
one = "1c0111001f010100061a024b53535009181c"
two = "746865206b696420646f6e277420706c6179"
verify = "746865206b696420646f6e277420706c6179"

result = fixedXOR(one, two)
if result == verify:
	print("[ OK ]")
