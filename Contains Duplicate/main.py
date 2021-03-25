class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        checkList = set()
        for num in nums:
            if num in checkList:
                return True
            else:
                checkList.add(num)
        return False