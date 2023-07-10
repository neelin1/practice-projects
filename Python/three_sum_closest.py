from typing import List


def threeSumClosest(nums: List[int], target: int) -> int:
    """
    Given an integer array nums of length n and an integer target, find three integers in nums such that the sum is closest to target.
    Return the sum of the three integers.
    You may assume that each input would have exactly one solution.
    """

    # Naive Solution:all possible combinations of 3, see which difference from target is smallest, O(n^3)

    # Dynammic Programming Solution:
    # Recurrence Relation: OPT(i, t) -> optimal solution items 0 through i and target t
    # Base Case: if only 3 items, those 3 items are the closest

    rows = len(nums)
    columns = 4
    default_value = 0

    # Using a list comprehension
    matrix = [[default_value for _ in range(columns)] for _ in range(rows)]

    def opt(i: int, k: int) -> int:
        """
        Recurrence Relation: OPT(i, t) -> cloest sum of k items 0 through i to t
        """
        if matrix[i][k] != 0:
            return matrix[i][k]
        elif k == 0:
            return 0
        elif k > i + 1 or i == -1:
            return 10000000000
        else:
            option1 = opt(i - 1, k)
            option2 = nums[i] + opt(i - 1, k - 1)
            if abs(target - option1) < abs(target - option2):
                return option1
            else:
                return option2

    for i in range(len(nums)):
        for k in range(4):
            matrix[i][k] = opt(i, k)

    print(matrix)
    return matrix[len(nums) - 1][3]


def run_test(nums: List[int], target: int, expected: int):
    """
    Run the test case on nums and target
    """
    string = (
        "The input list is "
        + str(nums)
        + ". The target is "
        + str(target)
        + ". The result is "
        + str(threeSumClosest(nums, target))
        + ". The expected result is "
        + str(expected)
    )
    return string


print(run_test([-1, 2, 1, -4], 1, 2))

print(run_test([0, 0, 0], 1, 0))

print(run_test([1, 1, 1, 1], 100, 3))

print(run_test([1, 1, 1, 1, 3], 100, 5))

print(run_test([1, 1, 1, 1000, 3], 100, 5))

print(run_test([-100, -98, -2, -1], -101, -101))
