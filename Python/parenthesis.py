def isValid(s: str) -> bool:
    stack = []
    for st in s:
        if st == '(' or st == '{' or st == '[':
            stack.append(st)
        elif st == ')' and len(stack) > 0 and stack[len(stack) - 1] == '(':
            stack.pop()
        elif st == ']' and len(stack) > 0 and stack[len(stack) - 1] == '[':
            stack.pop()
        elif st == '}' and len(stack) > 0 and stack[len(stack) - 1] == '{':
            stack.pop()
        else:
            return False
    if len(stack) == 0:
        return True
    else:
        return False


print(isValid("()"), "True")
print(isValid("()[]{}"), "True")
print(isValid("(]"), "False")
print(isValid("("), "False")
print(isValid("]"), "False")
