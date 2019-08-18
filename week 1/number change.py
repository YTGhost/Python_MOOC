NumberStr = "零一二三四五六七八九"
s = input("")
for c in s:
    print(NumberStr[eval(c)], end="")
