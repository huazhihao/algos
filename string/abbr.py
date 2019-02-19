def abbr(ss, n):
    ss = ss.split(".")
    # segments
    l = len(ss)
    # budget
    k = n - (l - 1) * 2 - len(ss[-1])
    out = ss[-1]
    for s in ss[-2::-1]:
        k -= (len(s) - 1)
        if k < 0:
            out = s[0] + "." + out
        else:
            out = s + "." + out
    return out

x = "abc.pqr.xyz"
for i in range(13)[6:]:
    a = abbr(x, i)
    # print("%d:%s" % (i, a))
    s = x.split(".")
    a = a.split(".")
    assert(len(a)==len(s))
    assert(a[-1]==s[-1])
    for i in range(len(a)-1):
        assert(a[i][0]==s[i][0])