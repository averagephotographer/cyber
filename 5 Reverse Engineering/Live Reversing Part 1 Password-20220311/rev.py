# Takes the long hex string from the disassembly of the binary executable and "decodes" it.
# Inspecting the executable seemed to indicate a NOT operation on each bit.
# Let's try that and see if we get good ASCII.

from sys import stdout

DEBUG = False

# the "password"
password = "ffffffbcffffffb7ffffffbaffffffbaffffffa5ffffffd2ffffffb6ffffffabffffffdfffffffb8ffffffadffffffb0ffffffb0ffffffa9ffffffbaffffffacffffffdfffffff9cffffff8dffffff96ffffff8cffffff8fffffff86ffffffdfffffff9cffffff8dffffff9effffff9cffffff94ffffff9affffff8dffffffdfffffff9cffffff97ffffff96ffffff8fffffff8c"

# step through each hex word
i = 0
while (i < len(password)):
	# grab 8 nibbles (4 bytes)
	word = password[i:i+8]
	if (DEBUG):
		print word
	# convert to an int (source base is 16)
	word = int(word, 16)
	if (DEBUG):
		print word
	# invert the bits by XORing with 1's
	word ^= 0xffffffff
	if (DEBUG):
		print word
	# convert to ASCII
	word = chr(word)
	stdout.write(word)

	# go to the next word
	i += 8
print
