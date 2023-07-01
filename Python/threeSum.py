class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        # divide into a dictionary of positive numbers and how many times they occur and a set of negative numbers and how many times they occur
        pos = {}
        neg = {}
        zeros = 0

        for num in nums:
            if num == 0:
                zeros += 1
            elif num > 0:
                if num in pos:
                    pos.update({num: pos[num] + 1})
                else:
                    pos.update({num: 1})
            elif num < 0:
                if num in neg:
                    neg.update({num: neg[num] + 1})
                else:
                    neg.update({num: 1})

        # create empty list
        triplet_list = []

        # create a list of all possible positive pairs
        for num_x, duplicates_x in pos.items():
            if duplicates_x > 1:
                if (-num_x * 2) in neg:
                    triplet_list.append([num_x, num_x, (-num_x * 2)])
            if zeros > 0 and -(num_x) in neg:
                triplet_list.append([num_x, 0, -(num_x)])
            for num_y, duplicates_y in pos.items():
                if num_y != num_x and -(num_x + num_y) in neg:
                    triplet_list.append([num_x, num_y, -(num_x + num_y)])

        # create a list of all possible negative pairs

        # if 3 or more 0s, add 0,0,0 to set of negative numbers
        if zeros >= 3:
            triplet_list.append([0, 0, 0])

        # check if each pair of positive numbers has a corresponding negative (including a pair of the same number if it occurs more than once)
        for num_x, duplicates_x in pos.items():
            if duplicates_x > 1:
                if (-num_x * 2) in neg:
                    triplet_list.append([num_x, num_x, (-num_x * 2)])
            if zeros > 0 and -(num_x) in neg:
                triplet_list.append([num_x, 0, -(num_x)])
            for num_y, duplicates_y in pos.items():
                if num_y != num_x and -(num_x + num_y) in neg:
                    triplet_list.append([num_x, num_y, -(num_x + num_y)])

        # check if each pair negative numbers has a corresponding positive (including a pair of the same number if it occurs more than once)
        for num_x, duplicates_x in neg.items():
            if duplicates_x > 1:
                if -(num_x * 2) in pos:
                    triplet_list.append([num_x, num_x, -(num_x * 2)])
            for num_y, duplicates_y in neg.items():
                if num_y != num_x and -(num_x + num_y) in pos:
                    triplet_list.append([num_x, num_y, -(num_x + num_y)])

        return triplet_list
