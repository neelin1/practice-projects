

def solution(S: str, T: str) -> int:

    # convert A and B to tuples of strings
    s = S.split(":")
    t = T.split(":")

    # time being currently considered
    currentTime = s

    # number of instances of interesting times
    totalIntTimes = 0

    while (currentTime != t):
        # Check if time is interesting
        if (numDigits(currentTime) <= 2):
            totalIntTimes += 1

        # Increment Time
        # Skip certain times
        if (numDigits([currentTime[0], currentTime[1]]) > 2):
            if (currentTime[0] != t[0] and currentTime[1] != t[1]):
                currentTime[2] = "59"
            else:
                break

        # Standard Time Increment
        if (currentTime[2] != "59"):
            currentTime[2] = str(int(currentTime[2]) + 1)
        elif (currentTime[1] != "59"):
            currentTime[2] = "00"
            currentTime[1] = str(int(currentTime[1]) + 1)
        elif (currentTime[0] != "23"):
            currentTime[2] = "00"
            currentTime[1] = "00"
            currentTime[0] = str(int(currentTime[0]) + 1)
        else:
            currentTime[2] = "00"
            currentTime[1] = "00"
            currentTime[0] = "00"

        # Fix Times with Leading 0s
        if (len(currentTime[0]) == 1):
            currentTime[0] = "0" + currentTime[0]
        if (len(currentTime[1]) == 1):
            currentTime[1] = "0" + currentTime[1]
        if (len(currentTime[2]) == 1):
            currentTime[2] = "0" + currentTime[2]

    # Check if end time is interesting
    if (numDigits(t) <= 2):
        totalIntTimes += 1

    # Return number of interesting times
    return totalIntTimes


def numDigits(times: list):
    digits = set()

    for time in times:
        for digit in time:
            digits.add(digit)

    return (len(digits))


def test_solution():
    assert solution("15:15:00", "15:15:12") == 1
    # print(solution("15:15:00", "15:15:12"))
    assert solution("22:22:21", "22:22:23") == 3
    assert solution("00:00:00", "00:00:00") == 1
    assert solution("23:59:55", "00:00:12") == 12
    assert solution("23:59:00", "00:00:12") == 12
    # print(solution("23:59:55", "00:00:12"))
    # assert isInteresting((11, 22, 33)) == False
    # assert isInteresting((11, 22, 12)) == True
    # assert isInteresting((01, 10, 00)) == True

    print("All tests passed.")


if __name__ == "__main__":
    test_solution()
