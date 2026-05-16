# # Treid O(n) ; Did not pass all test cases esp duplicates in the data
# import collections

# class Solution:
#     def twoSum(self, nums: List[int], target: int) -> List[int]:

#         res = []
#         nums_dict = {value: nums.index(value) for value in nums}
#         nums_dict_sorted = collections.OrderedDict(sorted(nums_dict.items()))
#         print(nums_dict_sorted)

#         nums = list(nums_dict_sorted.keys() )
#         i = 0
#         j = len(nums) - 1
#         while i != j :
#             print(i,j, nums[i], nums[j])
#             if nums[i] + nums[j] == target:
#                 res = [ nums_dict_sorted[nums[i]], nums_dict_sorted[nums[j]] ]
#                 j -= 1
#             elif nums[i] + nums[j] > target :
#                 j -= 1
#             elif nums[i] + nums[j] < target :
#                 i += 1
                
#         return res



# Ref : https://leetcode.com/problems/two-sum/solutions/7266755/beats-100-beginner-friendly-hash-map-by-xr5kb/
from typing import List

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        num_map = {}
        for i, num in enumerate(nums):
            complement = target - num
            if complement in num_map:
                return [num_map[complement], i]
            num_map[num] = i

        
        