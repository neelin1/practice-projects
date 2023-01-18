def isMatchBad(s: str, p: str) -> bool:
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


def isMatch(s: str, p: str) -> bool:
    # makes a table of false where number of rows equals len(p) + 1 and each rows is an array of len(s) + 1
    table = [[False] * (len(s) + 1) for _ in range(len(p) + 1)]
    table[0][0] = True  # p[:0] and s[:0], i.e. 2 empty strings match

    # p[:i], s[:0], i.e. all cases where s is empty and p is not (true if p is *)
    for i in range(2, len(p) + 1):
        table[i][0] = table[i - 2][0] and p[i - 1] == '*'

    # returns the bottom right index of the table, if this is true it means the strings match
    return table[-1][-1]


print(isMatch("", ""), True)  # empty strings
# print(isMatch("aa", "aa"), True)  # same strings
# print(isMatch("aa", "ab"), False)  # different strings of same length
# print(isMatch("aa", "a"), False)  # different strings of different length
# print(isMatch("a", "aa"), False)  # different strings of different length
# print(isMatch("aa", "a*"), True)  # same pattern with *
# print(isMatch("aaa", "a*"), True)  # ERROR same pattern with *
# print(isMatch("a", "a*"), True)  # same pattern with *
# print(isMatch("aa", "a*a"), True)  # ERROR same pattern with *
# print(isMatch("ab", "a*b"), True)  # same pattern with *
# print(isMatch("aa", "b*"), False)  # different preceding chracter
# print(isMatch("ab", ".*"), True)  # same pattern with .*
# print(isMatch("a", "."), True)  # same pattern with .
# print(isMatch("ab", ".b"), True)  # same pattern with .
# print(isMatch("ab", ".."), True)  # same pattern with .
