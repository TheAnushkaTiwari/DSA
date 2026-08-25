class Solution:
    def missingMultiple(self, nums: List[int], k: int) -> int:
        hash_set=dict.fromkeys(nums,0)
        result=0
        for i in range(1,len(nums)+2):
            if k*i not in hash_set:
                result=k*i
                break
        return result
        