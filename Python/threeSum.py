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

        # create a set of all possible positive pairs as tuples
        pos_pairs = set()

        for num_x, duplicates_x in pos.items():
            if duplicates_x > 1:
                pos_pairs.add((num_x, num_x))
            if zeros > 0:
                pos_pairs.add((num_x, 0))
            for num_y, duplicates_y in pos.items():
                if num_y != num_x and (not (num_y, num_x) in pos_pairs):
                    pos_pairs.add((num_x, num_y))

        # create a list of all possible negative pairs
        neg_pairs = set()

        for num_x, duplicates_x in neg.items():
            if duplicates_x > 1:
                neg_pairs.add((num_x, num_x))
            if zeros > 0:
                neg_pairs.add((num_x, 0))
            for num_y, duplicates_y in neg.items():
                if num_y != num_x and (not (num_y, num_x) in neg_pairs):
                    neg_pairs.add((num_x, num_y))

        # create empty list for triplets
        triplet_list = []

        # if 3 or more 0s, add 0,0,0 to set of negative numbers
        if zeros >= 3:
            triplet_list.append([0, 0, 0])

        # check if each pair of positive numbers has a corresponding negative (including a pair of the same number if it occurs more than once)
        for p_1, p_2 in pos_pairs:
            if -(p_1 + p_2) in neg:
                triplet_list.append([p_1, p_2, -(p_1 + p_2)])

        # check if each pair negative numbers has a corresponding positive (including a pair of the same number if it occurs more than once)
        for n_1, n_2 in neg_pairs:
            if -(n_1 + n_2) in pos and (n_1 != 0) and (n_2 != 0):
                triplet_list.append([n_1, n_2, -(n_1 + n_2)])

        return triplet_list
