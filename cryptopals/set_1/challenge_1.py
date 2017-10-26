#
#	By:		dpetrov
#	Usage:	Convert Hex to Base64
#

from binascii import unhexlify, b2a_base64

def		hexToBase64(value, show=True):
	byte = unhexlify(value)
	base64 = b2a_base64(byte)[:-1] # deleting new line
	if show:
		print("In byte: " + byte)
		print("In base64" + base64)
	return base64

# Example ->
sample = "49276d206b696c6c696e6720796f757220627261696e206c696b65206120706f69736f6e6f7573206d757368726f6f6d"
verify = "SSdtIGtpbGxpbmcgeW91ciBicmFpbiBsaWtlIGEgcG9pc29ub3VzIG11c2hyb29t"

result = hexToBase64(sample)
if result == verify:
	print("[ OK ]")
