from socket import socket, AF_INET, SOCK_STREAM
from time import time
from sys import stdout

DEBUG = True

ip = "localhost"
port = 1337

s = socket(AF_INET, SOCK_STREAM)

s.connect((ip, port))

data = s.recv(4096).decode()

while (data.rstrip("\n") != "EOF"):
    stdout.write(data)
    stdout.flush()

    t0 = time()
    data = s.recv(4096).decode()
    t1 = time()

    delta = round(t1 - t0, 3)

    if (DEBUG):
        stdout.write(f" {delta}\n")
        stdout.flush()
    
    # if (delta > ONE):
    #     convert_bin += 1
    # else:
    #     convert_bin += 0

s.close()

# convert = ""
# i = 0
# while (i < len(convert_bin)):
#   b = convert_bin[i:i+8]
#   try:
#       convert += chr(int(b, 2)) # might need to f"0b{b}" instead of just b
#   except:
#       convert += "?"
