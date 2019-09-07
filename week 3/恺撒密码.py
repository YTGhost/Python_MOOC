Str = input("")
for i in Str:
    if 'a' <= i <= 'z':
        print("{:}".format(chr(ord('a') + ((ord(i) - ord('a')) + 3) % 26)), end='')
    elif 'A' <= i <= 'Z':
        print("{:}".format(chr(ord('A') + ((ord(i) - ord('A')) + 3) % 26)), end='')
    else:
        print("{:}".format(i), end='')
'''
s = input()
t = ""
for c in s:
    if 'a' <= c <= 'z': 
        t += chr( ord('a') + ((ord(c)-ord('a')) + 3 )%26 )
    elif 'A' <= c <= 'Z':
        t += chr( ord('A') + ((ord(c)-ord('A')) + 3 )%26 )
    else:
        t += c
print(t)
'''
