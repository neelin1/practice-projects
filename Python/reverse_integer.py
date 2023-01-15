def reverse(x: int) -> int:
    strInt = str(x)[::-1]
    neg = ""
    if (strInt[len(strInt)-1] == '-'):
        strInt = strInt[0:len(strInt)-1]
        neg = "-"
    if len(strInt) < 10 or (len(strInt) == 10 and strInt[0] == "2" and (neg == '' and int(strInt[1:len(strInt)]) < 147483647) or (neg == '-' and int(strInt[1:len(strInt)]) <= 147483648)):
        return int(neg + strInt)
    else:
        return 0


print(reverse(123), 321)
print(reverse(-123), -321)
print(reverse(120), 21)
print(reverse(7463847412))
# outside range
2147483648
