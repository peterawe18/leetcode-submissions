class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        there = {}
        for i in nums:
            if i in there:
                there[i]+=1
            else:
                there[i]=1
        for i in there.values():
            if i >= 2:
                return True
        return False
         