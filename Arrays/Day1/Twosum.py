class Solution(object):
    def twoSum(self, nums, target):
        hashmap = {}  # Use = to assign a dictionary, not {}
        for i, n in enumerate(nums):  # Add comma between i and n
            diff = target - n
            if diff in hashmap:
                return [hashmap[diff], i]
            hashmap[n] = i  # This should be outside the if block