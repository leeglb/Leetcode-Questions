class Solution(object):
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        index = 0
        for num in nums: 
            index ^= num
            
        return index 
    

        "We use this cause of the XOR operation"
        "think binary between all values in the list"
        "we initialise an index and then for each num"
        "we will xor all of them until we return the "
        "index at the very end"
    
a = Solution()
print(a.singleNumber([3,3,4]))