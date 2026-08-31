class Solution:
    def hasDuplicate(self, nums):
        duplist = []
        for i in nums:
            if i in duplist:
                return True 
            duplist.append(i)
        return False
        