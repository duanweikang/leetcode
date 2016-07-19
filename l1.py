#1. two sum
### two sum ###

# so we are interested in index and we want to measure if number in array sums to a element.
# Thus use number as key, and index as value, and implement dictionary, iterate each element in array
# check if the existing element is the dictionary, if it does, return it, if it not, then keep processing.
# thus for each element, for elements that can sum with it equals to a target, the one appears before it will be returned,
# and those appears after it will be returned when the iteration steps locates at the corresponding one.
class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        d = {}
        for i in range(len(nums)):
            x = nums[i]
            if target - x in d:
                return (d[target-x],i)
            d[x] = i

