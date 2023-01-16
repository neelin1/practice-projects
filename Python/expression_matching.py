def isMatch(s: str, p: str) -> bool:
    sI = 0
    pI = 0
    lenS = len(s)
    lenP = len(p)
    while (sI < lenS):
        if (pI >= lenP):
            return False
        elif (s[sI] == p[pI]):
            sI += 1
            pI += 1
        elif (p[pI] == "."):
            sI += 1
            pI += 1
        elif (p[pI] == "*" and (s[sI] == p[pI-1] or p[pI-1] == ".")):
            sI += 1
            pI += 1
        elif (p[pI] == "*"):
            pI += 1
        elif (s[sI] != p[pI]):
            return False
    if (pI == lenP or (p[pI] == "*" and pI + 1 == lenP)):
        return True
    else:
        return False


# print(isMatch("aa", "aa"), True)  # same strings
# print(isMatch("aa", "ab"), False)  # different strings of same length
# print(isMatch("aa", "a"), False)  # different strings of different length
# print(isMatch("a", "aa"), False)  # different strings of different length
# print(isMatch("aa", "a*"), True)  # same pattern with *
print(isMatch("aaa", "a*"), True)  # ERROR same pattern with *
# print(isMatch("a", "a*"), True)  # same pattern with *
print(isMatch("aa", "a*a"), True)  # ERROR same pattern with *
print(isMatch("ab", "a*b"), True)  # same pattern with *
# print(isMatch("aa", "b*"), False)  # different preceding chracter
# print(isMatch("ab", ".*"), True)  # same pattern with .*
# print(isMatch("a", "."), True)  # same pattern with .
# print(isMatch("ab", ".b"), True)  # same pattern with .
# print(isMatch("ab", ".."), True)  # same pattern with .
