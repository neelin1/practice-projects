# get volume of widest container, which is height of smaller side
# another container can only contain more volume if its smallest side is larger than the smallest side of the current max container
# compare smallest side to adjacent side, if adjacent side is taller, compare that volume to max_volume
# if greater replace the max volume
# reduce smallest side again and compare

def maxArea(height) -> int:
    left = (0, height[0])
    right = (len(height)-1, height[-1])
    c_min = min(left[1], right[1])
    maxVolume = 0
    while (left[0] != right[0]):
        if (left[1] > right[1]):
            c_min = right[1]
            maxVolume = max(c_min * (right[0] - left[0]), maxVolume)
            right = (right[0]-1, height[right[0]-1])
        else:
            c_min = left[1]
            maxVolume = max(c_min * (right[0] - left[0]), maxVolume)
            left = (left[0]+1, height[left[0]+1])
    return maxVolume


print(maxArea([1, 8, 6, 2, 5, 4, 8, 3, 7]), 49)
print(maxArea([8, 8, 6, 2, 5, 4, 8, 3, 7]), 56)
print(maxArea([1, 1]), 1)
print(maxArea([1, 3, 1]), 2)
print(maxArea([1, 2]), 1)
