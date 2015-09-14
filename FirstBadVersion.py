__author__ = 'shokoufeh'

# The isBadVersion API is already defined for you.
# @param version, an integer
# @return a bool
# def isBadVersion(version):

class Solution(object):
    def firstBadVersion(self, n):
        """
        :type n: int
        :rtype: int
        """
        result = False
        low = 1
        high = n
        checking = (low + high) /2
        while(low != high):
            if(isBadVersion(checking)):
                high = checking
            else:
                low = checking + 1
            checking = (low + high) / 2
        return low

