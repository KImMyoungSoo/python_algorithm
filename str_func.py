msg = "It is Time"
print(msg.upper())
print(msg.lower())
print(msg)

tmp = msg.upper()
print(tmp)
print(tmp.find("T"))
print(tmp[1])
print(tmp.count("T"))
# 0~1번 까지 추출
print(msg[:2])
print(msg[3:5])

print(len(msg))

for i in range(len(msg)):
    print(msg[i],end=" ")
print()

for x in msg :
    print(x,end=" ")
print()

for x in msg :
    if x.isupper():
        print(x, end=' ')
print()

for x in msg : 
    if x.islower():
        print(x, end=' ')
print()

for x in msg:
    if x.isalpha():
        print(x,end=' ')
print()

temp = 'AZ'
for x in temp :
    print(ord(x))

temp = 65
print(chr(temp))