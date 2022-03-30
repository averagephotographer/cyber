# E -> 69   -> 001 000 101
            #   1   0   5
            #  --x --- r-x
# g -> 103  -> 001 100 111
            #  1   4   7

# y -> 121  -> 001 111 001
            #  1   7   1
# p -> 112  -> 001 110 000
            #  1   6   0
# t -> 116  -> 001 110 100
            #  1   6   4

            

astring = "Egypt"

# convert astring to bytes 
for c in astring:
    print(bin(ord(c))[2:])

print(chr(int(0b011)))


# d---r--rwx
# 1000100111

# -r-xrw--w-
# 0101110010 

# -rw--w-r-x
# 0110010101 

# -rw---x---
# 0110001000
# --wxr-xrwx
# 0011101111

# d-w---xr--
# 0100001100

# d-wxrw--w-


# dr--r-x-w-

# -rwxrwx--x

# d-w-----wx

# -rw-rwxrw-

# -r-x-----x

# d---rwxr--

# --wxrw--w-

# -rwxrwx-w-

# ---x------
