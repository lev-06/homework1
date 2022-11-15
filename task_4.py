def turb(x):
    a = ""
    b = x[0]
    for i in range(1, len(x)):
        if x[i] == x[i-1]:
            b += x[i]
        else:
            b = x[i]
        if len(b) > len(a):
           a = b
    return a
assert(l_substr("")) == ''
assert(l_substr("a")) == 'a'
assert(l_substr("aa")) == 'aa'
assert(l_substr("abb")) == 'bb'
assert(l_substr("hellloo worldd")) == 'lll'
assert(l_substr("aaabbbbbaabbccaaaaaaaaa")) == 'aaaaaaaaa'
assert(l_substr("4512451111111111111111111111111111111111111111111122222222222223333")) == '11111111111111111111111111111111111111111111'
