class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """

        len_list = list(range(len(nums)))

        d = dict(zip(len_list, nums))

        first_value = 0
        second_value = 0

        for key,value in d.items():

            if target - value in nums and target - value != value: #9

                first_value = (target-value) # first occurance

                d[key] = None

                break
            
        second_value = (target - first_value)

        values = (nums.index(first_value), nums.index(second_value))

        return [min(values), max(values)]

            

a = Solution()
print(a.twoSum([3,2,4], 6))