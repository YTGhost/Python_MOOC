TempStr = input("")
if TempStr[0] in ['F', 'f']:
    C = (eval(TempStr[1:]) - 32) / 1.8
    print("C{:.2f}".format(C))
elif TempStr[0] in ['C', 'c']:
    F = eval(TempStr[1:]) * 1.8 + 32
    print("F{:.2f}".format(F))
