class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:

        l = 1

        # range(1, len(nums)) -> compare with previous and include last element
        # range(len(nums)) -> touch all elements from start to end (no prev)
        
        for r in range(1, len(nums)):
            if nums[r] != nums[r-1]:
                nums[l] = nums[r]
                l += 1
        return l
