
def atoi(s):
    l = len(s)
    return sum([int(c)*(10**(l-i-1)) for (i, c) in enumerate(s)])


assert(atoi("0") == 0)
assert(atoi("1") == 1)
assert(atoi("12") == 12)
assert(atoi("01") == 1)
assert(atoi("00") == 0)