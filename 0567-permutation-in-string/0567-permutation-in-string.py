class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        def per( a1,a2):
            for i in a1:
                if i not in a2:
                    return False
                else:
                    a2= a2.replace(i,"",1)
            return True
    
        l = 0
        r = len(s1)-1
        while r <= len(s2) - 1:
            if per(s1, s2[l:r+1]):
                return True
            l+=1
            r+=1
        return False
        
        
        