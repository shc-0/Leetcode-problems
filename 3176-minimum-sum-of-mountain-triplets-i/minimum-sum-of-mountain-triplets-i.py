class Solution:
    def minimumSum(self, nums: List[int]) -> int:
        if (len(nums) < 3):
            return -1 # mountain not posible if no. of elements in nums are less than 3

        min_sum = float('inf') # so that in first iteration, min_sum will be declared with sum of first mountain found

        for i in range(1, len(nums) - 1):
            # slice the left side of nums from 0 to 1, then store the min element in it
            min_in_left_side = min(nums[:i])

            # do same for the right side
            min_in_right_side = min(nums[i+1:])

            # compare the sum of current mountian with the previous mountain
            # set sum with the mountain whose sum is least
            if ((nums[i] > min_in_left_side) and (nums[i] > min_in_right_side)):
                min_sum = min(min_sum, nums[i] + min_in_left_side + min_in_right_side)

        # if min_sum is still infinity that means we have not found any mountain in out input
        return min_sum if (min_sum != float('inf')) else -1




            
            
        