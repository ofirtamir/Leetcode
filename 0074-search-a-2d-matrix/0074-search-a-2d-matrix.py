class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        l, r =0 , len(matrix[0])-1
        ll , rr = 0 ,len(matrix) -1
        while ll<= rr:
            mm = (ll + rr)//2
            if matrix[mm][0] == target:
                return True
            elif matrix[mm][0] < target:
                ll = mm + 1  
            else:
                rr =mm -1

        while l <= r:
            m = (r + l) // 2
            if matrix[rr][m] == target:
                return True
            elif matrix[rr][m] < target:
                l = m +1
            else:
                r = m-1
        return False

