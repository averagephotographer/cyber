# converts text from a file to numbers

# takes in a file name
# returns a list of numbers

# opens file
while True:
    try:
        file_name = input("Enter file name: ")
        file_handle = open(file_name)
        alist = ""
        for char in file_handle:
            if char == "Z":
                alist += "0"
            if char == "O":
                alist += "1"

        print(alist)
        break
    except:
        print("File not found")

