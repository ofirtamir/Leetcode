class Solution:
    def isPalindrome(self, s: str) -> bool:
        s= s.lower()
        l =[]
        for i in s:
            if i.isalpha() or i.isdigit():
                l.append(i)
        for x in range(len(l)//2):
            if l[x] != l[len(l)-1-x] :
                return False
        return True
        
        