class Solution(object):
    def isPalindrome(self, x):
        '''
        Compare the original string with the reversed string using the equality operator
        If they are the same, it means x is a palindrome, so return True
        Otherwise, return False 
        '''
        return str(x)==str(x)[::-1] 