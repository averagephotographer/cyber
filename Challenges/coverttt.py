#####################################################################################################################
#                                                                                                                   #
#       Challenge 1 - Getting Permissions                                                                                	#
#       Group Name: Seth                                                                                            #
#       Group Members:  Ethan Clapp, Cameron Thomas, Dylan Weaver, Ghufran Aldawood,                                #
#                       Chris Tullier, David Mains, Will Shepherd                                                   #
#                                                                                                                   #
#####################################################################################################################

# ---------------------------- #
# imports and global variables
# ---------------------------- #

# imports
import os
from ftplib import FTP

# declaration of global variables
IP = "138.47.99.64"
PORT = 21
USER = "anonymous"
PASSWORD = ""
FOLDER = "7"
USE_PASSIVE = True
METHOD = 7 # use '7' or '10' to specify number of bits
RUN_TYPE = 'decode' # use 'encode' or 'decode' to specify how to run

# ---------------------------- #
# methods
# ---------------------------- #

# ripped from binary decoder, could maybe import for easier reading
def decode_bin(bin_size, text):

	# initializes needed variables
	counter = 0
	bin_char = ""
	ascii_word = ""

	# goes through all 1's and 0's
	for char in text:

		if char == "1" or char == "0":

			# concatenates the bits until it reaches the binary length we set
			if counter < bin_size:
				bin_char = bin_char + char
				counter += 1

		# once the length is hit, convert the binary character into an ASCII character,
		# then append to the ASCII text, also set counters to 0
		if counter == bin_size:

		    ascii_char = chr(int(bin_char, 2))
		    ascii_word = ascii_word + ascii_char
		    bin_char = ""
		    counter = 0

	# output the final word or phrase
	print(f"Decoded text: {ascii_word}")


# decodes ftp convert channel based on specified METHOD
def decode_ftp():

	# initialize variables
	perms = ''
	perms_bin = ''

	# check if METHOD is 7 bits
	if METHOD == 7:

		# iterate through lines in files
		for f in files:

			# slice permisions to only include 7 bits
			perms = f[3:10]

			# check if the first 3 chars are 0's (throw out anything that isn't as noise)
			if (f[:3] == '---'):

				# iterate through charcters and append 1's for letters and 0's for dashes
				for char in perms:

					if char == 'r' or char == 'w' or char == 'x':

						perms_bin += '1'

					elif char == '-':

						perms_bin += '0'

		# call binary decoder to print results in ASCII
		decode_bin(7, perms_bin)
	
	# check if METHOD is 10 bits and if so, run similar method but skip the slicing part and don't worry about noise
	elif METHOD == 10:

		for f in files:

			perms = f[:10]

			for char in perms:

				if char == 'r' or char == 'w' or char == 'x' or char == 'd':

					perms_bin += '1'

				elif char == '-':

					perms_bin += '0'

		decode_bin(7, perms_bin)
	
	# if METHOD is invalid, throw error to user
	else:
		print("Invalid method! Try \'7\' or \'10\'.")

# ---------------------------- #
# main program
# ---------------------------- #

# creates FTP instance, connects via IP, and logs in using credentials
ftp = FTP()
ftp.connect(IP, PORT)
ftp.login(USER, PASSWORD)
ftp.set_pasv(USE_PASSIVE)

# copies contents of FOLDER location to files list (with permissions)
ftp.cwd(FOLDER)
files = []
ftp.dir(files.append)

# quits the FTP instance
ftp.quit()

# check RUN_TYPE and run appropriate type
if RUN_TYPE == "decode":
	decode_ftp()
elif RUN_TYPE == "encode":
	encode_ftp()
# if RUN_TYPE is invalid, throw error to user
else:
	print("Invalid run type! Try \'encode\' or \'decode\'.")

