# print("Hello, World!")

# if 5 > 2:
#     print(5)
#     # print (2) error, need same number of spaces
#     # no syntax for multiline comments
# x = 6

# print(x)

# x = 7
# print(x)

# # python ignore string literals
# """
# jngeprjg
# oafvvz
# """  # can use them like a comment

# x = "5"  # can change type

# print(x)

# x = str(3)

# print(type(x))
# # " and ' are equivalent

# # variable names can not start with a number, 2var is illegal, have a - or a space. Variable names are case sensitive
# # generaly use camelcase for variable
# myVar = x

# print(x)
# print(myVar)
# x = 4
# print(x)
# print(myVar)  # myVar is set to the primitve that x was at

# # can assign multiple variable in 1 line
# x, y, z = 1, 2, 3
# print(x)
# print(y)
# print(z)

# # list
# nums = [1, 2, 3]
# x, y, z = nums  # can assign to a list through unpacking, the list and number of variable must be the same
# # u, i = nums this throw an error
# # can print a number of items in a row, adds a space between different elements
# print(x, y, z)
# print(x + y + z)
# z = "5"
# # print(x + y + z) can't add int to str
# print(y, z)  # can print them next to eachother
# print(y + int(z))  # can convert the type


# # FUNCTIONS
# x = 1


# def myFunc():
#     print(x)


# myFunc()


# def myFunc():
#     y = 5
#     print(y)


# myFunc()
# print(y)  # y's scope is only inside that function (y is local in the function)

# global r  # global makes the variable have global scope
# r = 5

# string = "hello"
# string += "world"
# print(string)


# def compareChars(i, strs, iStr) -> bool:
#     for s in strs:
#         if i >= len(s) or s[i] != iStr[i]:
#             return False
#     return True


# def longestCommonPrefix(strs: list[str]) -> str:
#     pre = ""
#     if len(strs) == 0:
#         return pre
#     iStr = strs[0]
#     if len(strs) == 1:
#         return iStr
#     for i in range(len(iStr)):
#         if compareChars(i, strs, iStr):
#             pre = pre + iStr[i]
#         else:
#             break
#     return pre


# strList = ["flower", "flow", "flight"]
# strList = ["flower"]
# strList = ["dog", "racecar", "car"]

# print(longestCommonPrefix(strList))


# for i in range(6 - 1, -1, -1):
#     print(i)


# thisTuple = ("string", 1)

# print(thisTuple)

# for i in range(3):
#     print(i)

# print("\n")
# for i in range(int(7 / 2)):
#     print(i)

# print("\n")

# for i in range(4, -1, -1):
#     print(i)

# print("\n")

# for i in range(3):
#     print(i)

# print("\n")

# i = 2 * 2 + 1
# bottom = int((i - 1) / 2)
# top = int((i - 1) / 2) + 1
# print(bottom, top)

for i in range(1, 2*3):
    print(i)
