def rvs(s):
    if s == "":
        return s
    else:
        return rvs(s[1:]) + s[0]


print(rvs("hello"))
