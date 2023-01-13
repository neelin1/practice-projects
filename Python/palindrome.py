def isPalindrome(x: int) -> bool:
    strX = str(x)
    for i in range(int(len(strX)/2)):
        if strX[i] != strX[len(strX)-(i+1)]:
            return False
    return True


print(isPalindrome(121), "true")
print(isPalindrome(-121), "false")
print(isPalindrome(10), "false")
