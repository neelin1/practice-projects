def isPalindrome(s: str) -> bool:
    for i in range(int(len(s) / 2)):
        if s[i] != s[len(s)-(i+1)]:
            return False
    return True


# efficient for short strings, inefficient for long strings
def longestPalindromeBad(s: str) -> str:
    if len(s) == 1:
        return s
    for i in range(len(s)-1, -1, -1):
        for i2 in range(len(s)-i):
            if isPalindrome(s[i2:i2+i+1]):
                return s[i2:i2+i+1]
    return (s[0])


def expand(s: str, i: int) -> str:
    if i % 2 == 0:  # starts in space between characters
        t = ""
        bottom = int((i - 1) / 2)
        top = int((i - 1) / 2) + 1
    else:
        t = s[int((i - 1) / 2)]
        bottom = int((i - 1) / 2) - 1
        top = int((i - 1) / 2) + 1
    while bottom >= 0 and top < len(s):
        if s[bottom] == s[top]:
            t = s[bottom] + t + s[top]
            bottom -= 1
            top += 1
        else:
            return t
    return t


# print(expand("babad", 0), "Empty")
# print(expand("babad", 1), "b")
# print(expand("babad", 2), "Empty")
# print(expand("babad", 3), "bab")
# print(expand("babad", 4), "Empty")
# print(expand("xxxxx", 1), "x")
# print(expand("xxxxx", 2), "xx")
# print(expand("xxxxx", 3), "xxx")
# print(expand("xxxxx", 4), "xxxx")
# print(expand("xxxxx", 5), "xxxxx")
# print(expand("xxxxx", 6), "xxxx")
# print(expand("xxxxx", 7), "xxx")
# print(expand("xxxxx", 8), "xx")
# print(expand("xxxxx", 9), "x")
# print(expand("cbbc", 0), "Empty")
# print(expand("cbbc", 1), "c")
# print(expand("cbbc", 2), "Empty")
# print(expand("cbbc", 4), "bb")
# print(expand("bbbb", 0))
# print(expand("bbbb", 1))
# print(expand("bbbb", 2))
# print(expand("bbbb", 3))
# print(expand("ccc", 1), "c")
# print(expand("ccc", 2), "cc")
# print(expand("ccc", 3), "ccc")
# print(expand("ccc", 4), "cc")
# print(expand("ccc", 5), "c")


def longestPalindrome(s: str) -> str:
    if len(s) == 1:
        return s
    max = ""
    for i in range(1, 2*len(s)):
        exp = expand(s, i)
        if len(exp) > len(max):
            max = exp
    return max


print(longestPalindrome("babad"), "bab")
print(longestPalindrome("cbbd"), "bb")
print(longestPalindrome("cbbc"), "cbbc")
print(longestPalindrome("a"), "a")
print(longestPalindrome("ab"), "a")
print(longestPalindrome("glwhcebdjbdroiurzfxxrbhzibilmcfasshhtyngwrsnbdpzgjphujzuawbebyhvxfhtoozcitaqibvvowyluvdbvoqikgojxcefzpdgahujuxpiclrrmalncdrotsgkpnfyujgvmhydrzdpiudkfchtklsaprptkzhwxsgafsvkahkbsighlyhjvbburdfjdfvjbaiivqxdqwivsjzztzkzygcsyxlvvwlckbsmvwjvrhvqfewjxgefeowfhrcturolvfgxilqdqvitbcebuooclugypurlsbdfquzsqngbscqwlrdpxeahricvtfqpnrfwbyjvahrtosovsbzhxtutyfjwjbpkfujeoueykmbcjtluuxvmffwgqjgrtsxtdimsescgahnudmsmyfijtfrcbkibbypenxnpiozzrnljazjgrftitldcueswqitrcvjzvlhionutppppzxoepvtzhkzjetpfqsuirdcyqfjsqhdewswldawhdyijhpqtrwgyfmmyhhkrafisicstqxokdmynnnqxaekzcgygsuzfiguujyxowqdfylesbzhnpznayzlinerzdqjrylyfzndgqokovabhzuskwozuxcsmyclvfwkbimhkdmjacesnvorrrvdwcgfewchbsyzrkktsjxgyybgwbvktvxyurufsrdufcunnfswqddukqrxyrueienhccpeuqbkbumlpxnudmwqdkzvsqsozkifpznwapxaxdclxjxuciyulsbxvwdoiolgxkhlrytiwrpvtjdwsssahupoyyjveedgqsthefdyxvjweaimadykubntfqcpbjyqbtnunuxzyytxfedrycsdhkfymaykeubowvkszzwmbbjezrphqildkmllskfawmcohdqalgccffxursvbyikjoglnillapcbcjuhaxukfhalcslemluvornmijbeawxzokgnlzugxkshrpojrwaasgfmjvkghpdyxt"), "idk")
print(longestPalindrome("ccc"), "ccc")
