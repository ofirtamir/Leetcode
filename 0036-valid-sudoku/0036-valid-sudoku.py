class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        # def checkIsValid(l):
        #     dic = Counter(l)
        #     dic.pop(".")
        #     lis = dic.values()
        #     for x in lis:
        #         if x != 1:
        #             return False
        #     return True
        # new= [[]*3]
        # col = []
        # for i in range(9):
        #     if not checkIsValid(board[i]):
        #         return False
        # return True

        row = defaultdict(set)
        col = defaultdict(set)
        sqwr = defaultdict(set)
        
        for r in range(9):
            for c in range(9):
                if board[r][c] == ".":
                    continue
                if (board[r][c] in row[r] or 
                    board[r][c] in col[c] or
                    board[r][c] in sqwr[(r//3 , c //3)] ):
                    return False
                row[r].add(board[r][c])
                col[c].add(board[r][c])
                sqwr[(r//3, c//3)].add(board[r][c])
        return True
        
        







        