class Solution(object):
    def strStr(self, haystack, needle):
        """
        :type haystack: str
        :type needle: str
        :rtype: int
        """
        k=0
        for i in range(len(haystack)):
            if needle == haystack[i:i+len(needle)]: 
                return i
        return -1 

            

 
           