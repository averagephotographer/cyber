DEBUG = True
password = input()
timings = input()

if (DEBUG):
    print(f"{password = }")
    print(f"{timings = }")

password = password.split(",")
timinsg = timings.split(",")