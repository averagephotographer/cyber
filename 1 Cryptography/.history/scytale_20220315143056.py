message = "some random message"
jump = 4
new = ""
i = 0

msg_len = len(message)

while i < msg_len*4:
    new += message[i%msg_len]
    i += jump

print(new)

# Anky's cipher 
# echo "worklaptop" | tr a-z n-za-m
