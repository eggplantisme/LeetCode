import sys
# 编写一个程序，通过已填充的空格来解决数独问题。

# 一个数独的解法需遵循如下规则：

# 数字 1-9 在每一行只能出现一次。
# 数字 1-9 在每一列只能出现一次。
# 数字 1-9 在每一个以粗实线分隔的 3x3 宫内只能出现一次。

class Solution:
    def solveSudoku(self, board):
        """
        Do not return anything, modify board in-place instead.
        """
        # 找到所有的空白位置
        space_pos = []
        for i in range(9):
            for j in range(9):
                if board[i][j] == '.':
                    space_pos.append((i, j))
                else:
                    board[i][j] = int(board[i][j])
        if space_pos == []:
            return
        self.recursiveSolve(board, space_pos)
        for i in range(9):
            for j in range(9):
                board[i][j] = str(board[i][j])
    
    def recursiveSolve(self, board, space_pos):
        if space_pos == []:
            return True
        cur_pos = space_pos[0]
        row = [board[cur_pos[0]][i] for i in range(9) if board[cur_pos[0]][i] != '.']
        col = [board[i][cur_pos[1]] for i in range(9) if board[i][cur_pos[1]] != '.']
        # 找到该位置所在的方块
        i = cur_pos[0]
        j = cur_pos[1]
        squre_list = []
        for p in range(i//3*3, i//3*3+3):
            for q in range(j//3*3, j//3*3+3):
                if board[p][q] != '.':
                    squre_list.append(board[p][q])
        # 获得该位置可以放的数字
        num_to_put = []
        for n in range(1, 10):
            if n not in row and n not in col and n not in squre_list:
                num_to_put.append(n)
        if num_to_put == []:
            return False
        
        for num in num_to_put:
            board[i][j] = num
            result = self.recursiveSolve(board, space_pos[1:])
            if result:
                return True
            board[i][j] = '.'
        return False


if __name__ == '__main__':
    # 输入
    # 输入格式，每行{1,2,.,.,.,6,7,8,9}这样, 9行
    sudo = []
    for i in range(9):
        line = sys.stdin.readline().strip()
        line = line[1:-1].split(',')
        cur_row = []
        for num in line:
            if num != '.':
                cur_row.append(num)
            else:
                cur_row.append('.')
        sudo.append(cur_row)
    print("Origin is :")
    for row in sudo:
        print(row)
    Solution().solveSudoku(sudo)
    print("Answar is :")
    for row in sudo:
        print(row)
    """
        输入样例
{5,3,.,.,7,.,.,.,.}
{6,.,.,1,9,5,.,.,.}
{.,9,8,.,.,.,.,6,.}
{8,.,.,.,6,.,.,.,3}
{4,.,.,8,.,3,.,.,1}
{7,.,.,.,2,.,.,.,6}
{.,6,.,.,.,.,2,8,.}
{.,.,.,4,1,9,.,.,5}
{.,.,.,.,8,.,.,7,9}
    """