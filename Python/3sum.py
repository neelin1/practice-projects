# Brute Force: try all combinations of triplets
# divide into negative, positive, zero, try all combinations of
#    --+, ++-, -+0, 000

def threeSum(nums):
    triplets = []
    neg = []
    zero = 0
    pos = []
    for n in nums:
        if (n < 0):
            neg.append(n)
        elif (n == 0):
            zero += 1
        else:
            pos.append(n)
    if (zero >= 3):
        for i in range(zero/3):
            triplets.append([0, 0, 0])
    if (zero > 0):
        for i in range(len(pos)):
            try:
                neg.index(-pos[i])
                triplets.add(pos[i], -pos[i], 0)
            except:
                pass
            else:
                triplets.add(pos[i], -pos[i], 0)
    return (triplets)


print(threeSum([0, 0, 0, 1, -1]))
