from typing import List


class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        def work9(a) -> bool : #输入9个格子的值，判断是否是有效数独，a是一个长度为9的list
            #print(a)
            for i in range(8):
                if a[i] != '.':
                    for j in range(i+1,9):
                        if a[j] != '.' and a[i] == a[j] :
                            return False
            return True

        for i in range(9):
            if not work9(board[i]):  #行判断
                return False
        
        for i in range(9):
            a = []
            for j in range(9):
                a.append(board[j][i])
            if not work9(a):  #列判断
                return False
        
        for i in range(0,9,3):
            for j in range(0,9,3):
                if not work9([board[i][j], board[i][j+1], board[i][j+2],board[i+1][j], board[i+1][j+1], board[i+1][j+2],board[i+2][j], board[i+2][j+1], board[i+2][j+2]]):
                    return False  #方块判断
        
        return True


board = [["5","3",".",".","7",".",".",".","."]
        ,["6",".",".","1","9","5",".",".","."]
        ,[".","9","8",".",".",".",".","6","."]
        ,["8",".",".",".","6",".",".",".","3"]
        ,["4",".",".","8",".","3",".",".","1"]
        ,["7",".",".",".","2",".",".",".","6"]
        ,[".","6",".",".",".",".","2","8","."]
        ,[".",".",".","4","1","9",".",".","5"]
        ,[".",".",".",".","8",".",".","7","5"]]

print(Solution().isValidSudoku(board))