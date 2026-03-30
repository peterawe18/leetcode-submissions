class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        res = {}
        ans = []
        
        # Count frequencies
        for i in nums:
            if i in res:
                res[i] += 1
            else:
                res[i] = 1
        
        # Sort items by frequency in descending order
        sorted_items = sorted(res.items(), key=lambda x: x[1], reverse=True)
        
        # Extract the top K elements
        for i in range(k):
            ans.append(sorted_items[i][0])
        
        return ans



        