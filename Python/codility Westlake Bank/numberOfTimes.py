
def solution(A: list):
    # dictionary representing each number and how many times it appears
    numCounts = {}

    # iterate through A to count how many times each number appears
    for i in A:
        numCounts[i] = numCounts.get(i, 0) + 1

    # iterate through numCounts to find the largest number that equals the number of times it appears
    max = 0
    for k, v in numCounts.items():
        if (k == v and k > max):
            max = k
    return max


def test_solution():
    assert solution([3, 8, 2, 3, 3, 2]) == 3
    assert solution([7, 1, 2, 8, 2]) == 2
    assert solution([3, 1, 4, 1, 5]) == 0
    assert solution([5, 5, 5, 5, 5]) == 5
    assert solution([2]) == 0
    assert solution([1]) == 1

    print("All tests passed.")


if __name__ == "__main__":
    test_solution()
