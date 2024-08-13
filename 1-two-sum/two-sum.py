class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        num_map = {}  # Dictionary to store the number and its index
        
        for i, num in enumerate(nums):
            complement = target - num
            
            if complement in num_map:
                return [num_map[complement], i]  # Return the indices of the two numbers
            
            num_map[num] = i  # Add the number and its index to the dictionary

        return None  # Return None if no solution is found
        