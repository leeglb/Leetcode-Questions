class Solution(object):
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """ 

        xy = (dict((x,nums.count(x)) for x in set(nums)))

        max_value = max(xy.values())

        for key, value in xy.items():

            if value == max_value:

                return key

a = Solution()
print(a.majorityElement([3,3,4]))