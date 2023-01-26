
print(3)


def intToRoman(num: int) -> str:
    num_str = ""
    while (num > 0):
        if (num >= 1000):
            num -= 1000
            num_str += "M"
        elif (num >= 900):
            num -= 900
            num_str += "CM"
        elif (num >= 500):
            num -= 500
            num_str += "D"
        elif (num >= 400):
            num -= 400
            num_str += "CD"
        elif (num >= 100):
            num -= 100
            num_str += "C"
        elif (num >= 90):
            num -= 90
            num_str += "XC"
        elif (num >= 50):
            num -= 50
            num_str += "L"
        elif (num >= 40):
            num -= 40
            num_str += "XL"
        elif (num >= 10):
            num -= 10
            num_str += "X"
        elif (num >= 9):
            num -= 9
            num_str += "IX"
        elif (num >= 5):
            num -= 5
            num_str += "V"
        elif (num >= 4):
            num -= 4
            num_str += "IV"
        elif (num >= 1):
            num -= 1
            num_str += "I"
    return (num_str)


def intToRomanFast(num: int) -> str:
    dict1 = {1: 'I', 5: 'V', 10: 'X', 50: 'L', 100: 'C', 500: 'D',
             1000: 'M', 4: 'IV', 9: 'IX', 40: 'XL', 90: 'XC', 400: 'CD', 900: 'CM'}

    arr = [1000, 900, 500, 400, 100, 90, 50, 40, 10, 9, 5, 4, 1]
    result = ''
    for n in arr:
        while n <= num:
            result += dict1[n]
            num -= n
    return result


print(intToRoman(3), "III")
print(intToRoman(58), "LVIII")
print(intToRoman(1994), "MCMXCIV")
