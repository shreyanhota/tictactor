"""
Tic Tac Toe Player
"""

import math
import copy

X = "X"
O = "O"
EMPTY = None


def initial_state():
    """
    Returns starting state of the board.
    """
    return [[EMPTY, EMPTY, EMPTY],
            [EMPTY, EMPTY, EMPTY],
            [EMPTY, EMPTY, EMPTY]]


def player(board): 
    """
    Returns player who has the next turn on a board.
    """
    x_count = sum(row.count(X) for row in board)
    o_count = sum(row.count(O) for row in board)
    # If X's count is equal to O's count, it's X's turn, otherwise O's turn
    return X if x_count == o_count else O
        
    

    # raise NotImplementedError


def actions(board):
    x=set()
    for i in range(3):
        for j in range(3):
            if board[i][j]==EMPTY:   
                x.add((i,j))
    return x
    """
    Returns set of all possible actions (i, j) available on the board.
    """
    # raise NotImplementedError


def result(board, action):
    """
    Returns the board that results from making move (i, j) on the board.
    """
    new_board=copy.deepcopy(board)
    if action not in actions(board):
        raise exception("Not Valid Action")
    i,j=action
    new_board[i][j]=player(board)
    return new_board
    # raise NotImplementedError


def winner(board):
    """
    Returns the winner of the game, if there is one.
    """
    for row in board:
        if row[0]==row[1]==row[2] and row[0] is not None:
                return row[0]
    for col in range(3):
        if board[0][col]==board[1][col]==board[2][col] and board[0][col] is not None:
                return board[0][col] 
    if board[0][0]==board[1][1]==board[2][2] and board[0][0] is not None:
        return board[0][0]
    if board[0][2] == board[1][1] == board[2][0] and board[0][2] is not None:
        return board[0][2] 
    else :
        return EMPTY
    # raise NotImplementedError


def terminal(board):
    """
    Returns True if game is over, False otherwise.
    """
    if winner(board)==EMPTY:
        x_count = sum(row.count(X) for row in board)
        o_count = sum(row.count(O) for row in board)
        if x_count+o_count==9:
            return True
        else :
            return False
    else: return True
    # raise NotImplementedError


def utility(board):
    """
    Returns 1 if X has won the game, -1 if O has won, 0 otherwise.
    """
    if winner(board)==X:
        return 1
    elif winner(board)==O:
        return -1
    else:
        return 0
    # raise NotImplementedError


def minimax1(board):
    """
    Returns the optimal action for the current player on the board.
    """
    if terminal(board)==True:
        return None
    else :
        if(player(board)==X):
            for action in actions(board):
                if utility(result(board,action))==1:
                    return action
                elif utility(result(board,action))==0:
                    return action
                else:
                    return action
        if(player(board)==O):
            for action in actions(board):
                if utility(result(board,action))==-1:
                    return action
                elif utility(result(board,action))==0:
                    return action
                else:
                    return action
        # raise NotImplementedError


def minimax(board):
    """
    Returns the best move for the current player using the Minimax algorithm.
    """
    def max_value(board):
        """
        Returns the maximum value of the board for the maximizing player.
        """
        if terminal(board)==True:
            return utility(board)
        v = -math.inf
        for action in actions(board):
            value=min_value(result(board,action))
            if (value>v):
                v=value
        return v
    def min_value(board):
        """
        Returns the minimum value of the board for the minimizing player.
        """
        if terminal(board)==True:
            return utility(board)
        v = math.inf
        for action in actions(board):
            value=max_value(result(board,action))
            if value < v:
                v = value
        return v
    if terminal(board)==True:
        return EMPTY
    else :
        if (player(board)==X):
            v=-math.inf
            best_move=EMPTY
            for action in actions(board):
                value=min_value(result(board,action))
                if (value>v):
                    v=value
                    # best_move=action
            for action in actions(board):
                value=min_value(result(board,action))
                if(value==v):
                    best_move=action
            return best_move
        # elif (player(board)==O):
        else:
            v=math.inf
            best_move=EMPTY
            for action in actions(board):
                value=max_value(result(board,action))
                if (value<v):
                    v=value
                    # best_move=action
            for action in actions(board):
                value=min_value(result(board,action))
                if(value==v):
                    best_move=action
            return best_move
    