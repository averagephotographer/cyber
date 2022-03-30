from ftplib import FTP

IP = "138.47.99.64" # localhost also works
PORT = 21
USER = "anonymous"
PASSWORD = ""
FOLDER = "/"
USE_PASSIVE = True

ftp = FTP()
ftp.connect(IP, PORT)
ftp.login(USER, PASSWORD)
ftp.set_pasv(USE_PASSIVE)

ftp.cwd(FOLDER)
files = []
ftp.dir(files.append)

ftp.quit

for f in files:
    # print(f[:10])

    # does the line start with three dashes
    if f[:3] == "---":
        # get the characters
        first_ten = (f[3:10])
        
        binary = ""
        # iterate over each character
        for c in first_ten:
            # if - then append a zero to binary
            if c == "-":
                binary += "0"
            # otherwise, append a one
            else:
                binary += "1"
                
        # convert the binary to an ascii character
        ascii_char = chr(int(binary, 2))
        print(ascii_char)
