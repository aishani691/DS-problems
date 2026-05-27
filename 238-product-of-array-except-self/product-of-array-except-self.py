class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        # # Brute
        # res_list = []
        # for i in nums:
        #     res = 1
        #     for j in nums :
        #         if j != i : 
        #             res *= j
            
        #     res_list.append(res)

        # return res_list

        # Ref:  https://leetcode.com/problems/product-of-array-except-self/solutions/7909671/best-optimal-solution-easy-solution-java-u953/
        n = len(nums)
        
        # Initialize an array
        res = [0] * n

        # Initialize the variable
        pre = 1
        for i in range(n):

            # In each iteration iteratively keep mulitplying the previous index value for current index : 
            # Eg. nums = [1,2,3] ; Iter1 : [1,0,0] Nothing is multiplied at index 0  ; Iter2 : [1,1,0] ; Iter3 : [1,1,2]   
            # Note : Last index has the correct value 
            res[i] = pre
            pre *= nums[i]
            # print('pre', res)

        suf = 1
        for i in range(n - 1, -1, -1):

            # In each iteration iteratively keep mulitplying the next index value for current index : 
            # Eg. res = [1,1,2] ; Iter1 : [1,1,2] Nothing is multiplied at index  2 ; Iter2 : [1,3,2] ; Iter3 : [6,3,2]   
            res[i] *= suf
            suf *= nums[i]
            # print('suf' , res)

        return res




        