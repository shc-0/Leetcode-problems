class Solution:
    def findIndices(self, nums: List[int], indexDifference: int, valueDifference: int) -> List[int]:
        answer = [-1, -1] # if indices doesnot exists

        # for every i check whether such j exists which fulfilles 2 conditions
        for i in range(len(nums)):
            for j in range(len(nums)):
                condition1 = (abs(i - j) >= indexDifference)
                condition2 = (abs(nums[i] - nums[j]) >= valueDifference)

                if (condition1 and condition2):
                    answer = [i, j]

        return answer

        