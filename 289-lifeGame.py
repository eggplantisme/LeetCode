import copy

class Solution:
    def gameOfLife(self, board):
        """
        return next state of life game
        Do not return anything, modify board in-place instead.
        """
        new_board = copy.deepcopy(board)
        row = len(new_board)
        col = len(new_board[0])
        dir = [(0, -1), (-1, -1), (-1, 0), (-1, 1), (0, 1), (1, 1), (1, 0), (1, -1)]
        for i in range(row):
            for j in range(col):
                live_neighbor = 0
                for d in dir:
                    if row > i + d[0] >=0 and col > j + d[1] >= 0 and board[i + d[0]][j + d[1]] == 1:
                        live_neighbor += 1
                if live_neighbor < 2:
                    new_board[i][j] = 0
                elif live_neighbor == 2:
                    new_board[i][j] = board[i][j]
                elif live_neighbor == 3:
                    new_board[i][j] = 1
                else:
                    new_board[i][j] = 0
        for i in range(row):
            for j in range(col):
                board[i][j] = new_board[i][j]

import os
import time
def main():
    # init
    m = 10
    n = 10
    board = [[0 for i in range(m)] for j in range(n)]
    print(m, "rows")
    print(n, "cols")
    line = input("Please set a live node (row col), 0 <= row < " + str(m) + " and 0 <= col < " + str(n) + ", input play to start:")
    while line:
        if line == "play":
            break
        i = int(line.split(" ")[0])
        j = int(line.split(" ")[1])
        if 0 <= i < m and 0 <= j < n:
            board[i][j] = 1
        else:
            print("Overflow")
        line = input("(row col), 0 <= row < " + str(m) + " and 0 <= col < " + str(n) + ":")
    # play
    while True:
        output_s = ""
        for i in range(m):
            for j in range(n):
                output_s += str(board[i][j]) + " "
            output_s += "\n"
        os.system("cls")
        print(output_s)
        Solution().gameOfLife(board)
        time.sleep(2)


import tkinter as tk
from tkinter import ttk
def tk_main():
    window = tk.Tk()
    window.title("Life Game")
    window.resizable(0, 0)  # 禁止改变大小
    window.geometry('500x550')
    row = 20
    col = 20
    game_zone = tk.LabelFrame(window, text='GameZone')
    game_zone.grid(column=0, row=0, columnspan=col)
    board = [[0 for i in range(col)] for j in range(row)]
    buttons = [[None for i in range(col)] for j in range(row)]
    def click(i, j):
        def _click(event):
            print("Canvas", i, " ", j, "click.")
            if board[i][j] == 0:
                board[i][j] = 1
                buttons[i][j]['background'] = 'white'
            else:
                board[i][j] = 0
                buttons[i][j]['background'] = 'black'
        return _click
    for i in range(row):
        for j in range(col):
            b = tk.Canvas(game_zone)
            b.grid(column=i, row=j)
            b['background']='black'
            b['highlightthickness'] = 0.5
            b['height'] = 20
            b['width'] = 20
            b.bind('<Button-1>', click(i, j))
            buttons[i][j] = b
    
    def next_state():
        s = Solution()
        s.gameOfLife(board)
        for i in range(row):
            for j in range(col):
                if board[i][j] == 0:
                    buttons[i][j]['background'] = 'black'
                else:
                    buttons[i][j]['background'] = 'white'
    tk.Button(window, text='Next', command=next_state).grid(column=0, row=1)
    window.mainloop()



if __name__ == "__main__":
    # main()
    tk_main()
