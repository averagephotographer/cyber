from socket import socket, AF_INET, SOCK_STREAM
from time import sleep

port = 1337
ZERO = 0.025
ONE = 1

s = socket(AF_INET, SOCK_STREAM)
s.bind(('', port))

s.listen(0)
print("Server listening on port {}...".format(port))

c, addr = s.accept()

# covert message
msg = "Hello, world!\n"

""" HOMEWORK """
# covert_message = "scecret code" + "EOF"
# covert_message_binary = ""
# for c in covert_message:
#    covert_message_binary += zeroes_ones(c) # function to convert

# bin(ord('s'))[2:].zfill(8) = "01010101"
# zfill adds zeroes to the left of the string until it is 8 characters long



for i in msg:
    c.send(i.encode())
    sleep(0.1)

    # covert_message_binary[n] == 0:
    #    sleep(ZERO)
    # else:
    #   sleep(ONE)
    # n = (n + 1) % len(covert_message_binary)

c.send("EOF")
print("Message sent!")
c.close()
