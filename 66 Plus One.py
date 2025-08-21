class Solution(object):
    def plusOne(self, digits):
        """
        :type digits: List[int]
        :rtype: List[int]
        """
        
        num_added = int("".join(map(str, digits))) + 1
        num_list = list(str(num_added))

        return (list(map(int, num_list)))


a = Solution()
a.plusOne([9])