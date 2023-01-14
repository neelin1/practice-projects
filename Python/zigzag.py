def convert(s: str, numRows: int) -> str:
    if numRows == 1 or numRows >= len(s):
        return s
    L = [''] * numRows
    mod = numRows+numRows-2
    for i in range(len(s)):
        place = i % (mod)
        if place < numRows:
            L[place] = L[place] + s[i]
        else:
            place = abs(place - mod)
            L[place] = L[place] + s[i]
    return ''.join(L)


print(convert("PAYPALISHIRING", 3) + "\nPAHNAPLSIIGYIR")
print(convert("PAYPALISHIRING", 4), "\nPINALSIGYAHRPI")
print(convert("A", 1), "\nA")
