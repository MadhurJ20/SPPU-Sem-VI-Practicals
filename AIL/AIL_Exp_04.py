'''
Madhur Jaripatke
Roll No. 48
TE A Computer
RMDSSOE, Warje, Pune
'''
'''
Implement a solution for a Constraint Satisfaction Problem using Branch and Bound and
Backtracking for n-queens problem or a graph coloring problem.
'''

#Number of queens
print ("Enter the number of queens: ")
N = int(input())

#chessboard
#NxN matrix with all elements 0
board = [[0]*N for _ in range(N)]

def is_attack(i, j):
    #checking if there is a queen in row or column
    for k in range(0,N):
        if board[i][k]==1 or board[k][j]==1:
            return True
    #checking diagonals
    for k in range(0,N):
        for l in range(0,N):
            if (k+l==i+j) or (k-l==i-j):
                if board[k][l]==1:
                    return True
    return False

def N_queen(n):
    #if n is 0, solution found
    if n==0:
        return True
    for i in range(0,N):
        for j in range(0,N):
            if (not(is_attack(i,j))) and (board[i][j]!=1):
                board[i][j] = 1
                #recursion wether we can put the next queen with this arrangment or not
                if N_queen(n-1)==True:
                    return True
                board[i][j] = 0
    return False

N_queen(N)
print('Board:')
for i in board:
    print (i)