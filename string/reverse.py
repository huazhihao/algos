# reverse a string in place
def reverse(s):
    s = list(s)
    l = len(s)
    for i in xrange(l/2):
        s[i], s[l-1-i] = s[l-1-i], s[i]
    return "".join(s)


assert(reverse("") == "")
assert(reverse("a") == "a")
assert(reverse("ab") == "ba")
assert(reverse("abc") == "cba")
assert(reverse("abcd") == "dcba")
