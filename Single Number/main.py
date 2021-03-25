class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        checkList = set()
        for num in nums:
            if num in checkList:
                checkList.remove(num)
            else:
                checkList.add(num)
        return list(checkList)[0]
        