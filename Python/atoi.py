def testForInt(char: str) -> bool:
    try:
        int(char)
        return True
    except:
        return False


def myAtoi(s: str) -> int:
    s = s.strip()
    start = 0
    end = 0
    neg = 1
    length = len(s)
    if (length == 0):
        return (0)
    elif (s[0] == "-"):
        neg = -1
        start = 1
        end = 1
        if (length == 1):
            return (0)
    elif (s[0] == "+"):
        start = 1
        end = 1
        if (length == 1):
            return (0)
    if (not testForInt(s[end])):
        return (0)
    while (end < length and (testForInt(s[end]))):
        end += 1
    integer = neg * int(s[start:end])

    if (integer < -1 * (2**31)):
        return (-1 * (2**31))
    if (integer > (2**31) - 1):
        return ((2**31) - 1)
    return integer


print(myAtoi("42"), 42)
print(myAtoi("   -42"), -42)
print(myAtoi("4193 with words"), 4193)
print(myAtoi("words and 987"), 0)
print(myAtoi("+-12"), 0)
print(myAtoi("-+12"), 0)
print(myAtoi("-1+2"), -1)
print(myAtoi("4193+ with words"), 4193)
print(myAtoi("+words and 987"), 0)
