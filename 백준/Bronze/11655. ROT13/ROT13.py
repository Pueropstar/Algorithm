from sys import stdin

input = stdin.readline

S = input()

ans = ""

for i in S:
    if(i!=" " and i.isalpha()):
        asc_num = ord(i)+13
        if i.isupper():
            if asc_num>90:
                ans+=chr(64+(asc_num-90))
            else:
                ans+=chr(asc_num)
        elif i.islower():
            if asc_num>122:
                ans+=chr(96+(asc_num-122))
            else:
                ans+=chr(asc_num)
    elif(i!="\n"):
        ans+=i
                
print(ans)