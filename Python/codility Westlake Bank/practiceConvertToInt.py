
def convertToInt(s):
    result = []
    for char in s.lower():
        if char.isalpha():
            result.append(ord(char) - ord('a') + 1)
    return result


def test_convertToInt():
    assert convertToInt("abc") == [1, 2, 3]
    assert convertToInt("z") == [26]
    assert convertToInt("A") == [1]
    assert convertToInt("AbCd") == [1, 2, 3, 4]
    assert convertToInt("4$@#%") == []
    assert convertToInt("") == []

    print("All tests passed.")


if __name__ == "__main__":
    test_convertToInt()
