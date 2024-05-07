def xor(a, b):
    result = []
    for i in range(1, len(b)):
        if a[i] == b[i]:
            result.append('0')
        else:
            result.append('1')
    return ''.join(result)

crc8 = "10000111"
crc10 = "11000110101"
crc16 = "10001000000100001"
crc32 = "100000100110000010001110110110111"

data=""
data = input("Enter the data:")
print('''Choice 1- Crc8\nChoice 2- Crc10\nChoice 3- Crc16\nChoice 4- Crc32''')
choice = int(input("Enter which GP"))
key =""
if choice == 1:
    key = crc8
elif choice == 2:
    key = crc10
elif choice == 3:
    key = crc16
elif choice == 4:
    key = crc32
else:
    print("enter a valid choice between 1 to 4")

length = len(key)
append_data = data + '0' * (length - 1)
temp = append_data[0:length]
while length < len(append_data):
    if temp[0] == '1':
        temp = xor(key, temp) + append_data[length]
    else:
        temp = xor('0' * length, temp) + append_data[length]
    length += 1
if temp[0] == '1':
    temp = xor(key, temp)
else:
    temp = xor("0" * length, temp)
word = temp
#print(word)
codeword = data + word
print("Remainder:", word)
print("Encoded Data (Data + word):", codeword)

# Verification
receiver_data = input("Enter received data:")
len_rec = len(receiver_data)

len_rec = len(key)
temp = receiver_data[0:len_rec]
while len_rec < len(receiver_data):
    if temp[0] == '1':
        temp = xor(key, temp) + receiver_data[len_rec]
    else:
        temp = xor('0' * len_rec, temp) + receiver_data[len_rec]
    len_rec += 1
if temp[0] == '1':
    temp = xor(key, temp)
else:
    temp = xor("0" * len_rec, temp)
word = temp

print("Reminder after verification:", word)
for i in range(0, len(word)):
    if word[i] == '1':
        print("Data does not match, error in communication")
        break
else:
    print("No error")
