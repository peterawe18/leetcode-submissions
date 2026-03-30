class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if not nums:
            return 0
        nums.sort()
        counter = 1
        maxCounter = 1
        print(nums)
        for i in range(len(nums)-1):
            if nums[i+1] - nums[i] == 1:
                counter+=1
                maxCounter = max(maxCounter,counter)
            elif nums[i+1] != nums[i]:
                counter = 1
        return maxCounter
            
        