# -*- coding: utf-8 -*-
# Author: Cynthia

"""
    多维数据集
"""

# 初始化
l1 = [0]*10  # 一维可以这么写, 因为int是不可变数据类型

l2 = [[0]*10]*10  # 二维不能这么写, 因为外层列表的元素类型是list, 可变, 这里外层10个元素指向同一个list

l22 = [[0]*10 for _ in range(10)]  # 二维初始化应该这么写, 这里会初始化10个内层list

print(l22[0][0], l22[3][3], l22[9][9])

"""
    利用二维数组实现一个二维位置型游戏-三连棋
    
    O X O
      X 
      O X
"""

class TicTacToe:
    """Management of a Tic-Tac-Toe game"""
    def __init__(self):

        self._board = [[' ']*3 for _ in range(3)]

        self._player = 'X'

    def __str__(self):
        # 内层join获得每一行的输出['X X X', 'X O X']
        # 外层join再把内层join获得的字符串list每一项拼接起来
        return '\n'.join(' '.join(e) for e in self._board)

    def start(self):
        """Put an X or O at position (i, j) for next player's turn"""
        while True:

            pin = input('请玩家{}选定下棋位置x,y: '.format(self._player))
            i, j = [int(e.strip()) for e in pin.split(',')]

            if not 0 <= i <= 2 and 0 <= i <= 2:
                raise ValueError('Invalid border position')

            if self._board[i][j] != ' ':
                raise ValueError('Border position occupied')

            self._board[i][j] = self._player

            print(str(self))
            print('=====')

            self._player = 'X' if self._player == 'O' else 'O'

            winner = self.check_winner()

            if winner in ['X', 'O']:
                print('{} wins'.format(winner))
                break
            elif winner == -1:
                print('Tie')
                break
            else:
                pass

    def check_winner(self):

        b = self._board

        if b[0][0] == b[0][1] == b[0][2] != ' ': return b[0][0]
        if b[1][0] == b[1][1] == b[1][2] != ' ': return b[1][0]
        if b[2][0] == b[2][1] == b[2][2] != ' ': return b[2][0]

        if b[0][0] == b[1][0] == b[2][0] != ' ': return b[0][0]
        if b[0][1] == b[1][1] == b[2][1] != ' ': return b[0][1]
        if b[0][2] == b[1][2] == b[2][2] != ' ': return b[0][2]

        if b[0][0] == b[1][1] == b[2][2] != ' ': return b[0][0]
        if b[0][2] == b[1][1] == b[2][0] != ' ': return b[0][2]

        for i in range(3):
            for j in range(3):
                if b[i][j] == ' ':
                    return 0
        return -1

m = TicTacToe()
m.start()