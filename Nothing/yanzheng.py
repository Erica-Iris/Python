
def ToT(m):
    s = ""
    while m > 1:
        s = str(m % 3)+s
        m = m // 3
    return s


def ToLenSix(m):
    for i in range(1, 7-len(m)):
        m = "0"+m
    return m


def IfOrNot(a, s):
    counta = 0
    for i in range(len(s)):
        if s[i] == str(a):
            counta = counta + 1


for i in range(1, 729):
    # print(ToLenSix(ToT(i)))
    
