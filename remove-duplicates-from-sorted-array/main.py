class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        n = len(nums)
        
        j=0
        for i in range(n):
           if(nums[j] != nums[i]):
                j = j+1
                nums[j] = nums[i]
        
        nums = nums[:j+1]
        return j+1