board = [
    [7,8,0,4,0,0,1,2,0],
    [6,0,0,0,7,5,0,0,9],
    [0,0,0,6,0,1,0,7,8],
    [0,0,7,0,4,0,2,6,0],
    [0,0,1,0,5,0,9,3,0],
    [9,0,4,0,6,0,0,0,5],
    [0,7,0,3,0,0,0,1,2],
    [1,2,0,0,0,7,4,0,0],
    [0,4,9,2,0,6,0,0,7]
]

#algorithm
def solve(bo):
    find = find_empty(bo)
    if not find:
        return True
# means all the empty elements are now predicted
    else:
        row, col = find
# now looping form 1-9 to check and predfict values in order to get the solution
    for i in range(1,10):
        if valid(bo, i, (row,col)):
            bo[row][col] = i
            
            if solve(bo):
                return True
# if the predict number solves print it, else check number
            
            bo[row][col]=0
            
    return False
# if no number is correct check the peviously predict value again

    
def valid(bo, num, pos):
    #checking for row
    for i in range (len(bo[0])):
        if bo[pos[0]][i] == num and pos[1] != i:
            return False
# we are checking each column, like each element in the row, i != i is for the time when we check for a number and the number is at where we just predicted the number so it'll be ignored
# but if that number is anywhere else it'll print false

    #checking for column
    for i in range(len(bo)):
        if bo[i][pos[1]] == num and pos[0] != i:
            return False
# after printing the number in the we'll check in the column for the same number '!= i' is for the number we just predicted , it should be ignored

    #checking for the box
    #each sudoku game consists of 9 such equally divided boxes
    box_x = pos [1] // 3
    box_y = pos [0] // 3
    # dividing to check in which box does  the element is, it'll help to check weather the number is in tht box or not
    
    for i in range ( box_y * 3, box_y * 3 + 3):
         for j in range (box_x * 3, box_x * 3 + 3):
            if bo [i][j] == num and (i,j) != pos:
    # this is to make sure we don't check the position we just predicted
                return False
            
    return True
# after all the checks and the value predicted is correct then it can be the correct answer
def print_board(bo):
    
    for i in range(len(bo)):
        if i % 3 == 0 and i != 0:
            print("- - - - - - - - - - - - - - - - - - - - - ")

        for j in range(len(bo[0])):
            if j % 3 == 0 and j != 0:
# j!= 0 means that the left side first row won't print "|"
                print(" | " , end = " ")

            if j == 8:
                print(bo[i][j])
            else:
                print(str(bo[i][j]) + "  ", end= " ")



print_board(board)
# it'll find the empty square in the board
# in this code we are using "0" as the empty square

def find_empty(bo):
    for i in range(len(bo)):
        for j in range (len(bo[0])):
            if bo [i][j]== 0:
                return (i, j)
            
    return None


solve (board)
print ("_______________________________________")
print ("_______________________________________")
print_board(board)

