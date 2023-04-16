class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        for i in range(len(nums)):  # Loop through each number in the input array
            for j in range(i+1, len(nums)):  # Loop through each subsequent number in the input array
                if nums[i] + nums[j] == target:  # Check if the sum of the current pair of numbers equals the target
                    return [i, j]  # If a pair is found, return their indices as a list
