class Solution:
    def isPalindrome(self, s: str) -> bool:
        
        st = ''.join(c.lower() for c in s if c.isalnum())
        rev = st[::-1]
        print( s, " : ", rev)
        return st == rev