class Solution(object):
    def strStr(self, haystack, needle):
        """
        :type haystack: str
        :type needle: str
        :rtype: int
        """
        first_occurance = ""

        if needle in haystack:
            first_occurance = haystack.index(needle)

            return first_occurance

        else:

            return -1
        