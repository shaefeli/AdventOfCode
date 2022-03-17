def print_board(board):
    for line in board:
        print("".join(line))
    print()

def move_board(board):
    board, nr_moves_east = move(board,">")
    board, nr_moves_south = move(board,"v")
    return board,nr_moves_east+nr_moves_south

def move(board,direction):
    new_board=[["."]*len(board[0]) for i in range(len(board))]
    indices_that_stay=set()
    indices_that_stay_other=set()
    new_indices=set()
    for j in range(len(board)):
        for i in range(len(board[0])):
            if direction==">":
                if board[j][i]==">":
                    if board[j][(i+1)%len(board[0])]==".":
                        new_indices.add((j,(i+1)%len(board[0])))
                    else:
                        indices_that_stay.add((j,i))
                elif board[j][i]=="v":
                    indices_that_stay_other.add((j,i))

            elif direction=="v":
                if board[j][i]=="v":
                    if board[(j+1)%len(board)][i]==".":
                        new_indices.add(((j+1)%len(board),i))
                    else:
                        indices_that_stay.add((j,i))
                elif board[j][i]==">":
                    indices_that_stay_other.add((j,i))

    for (j,i) in indices_that_stay:
        new_board[j][i]=direction

    for (j,i) in new_indices:
        new_board[j][i]=direction

    for (j,i) in indices_that_stay_other:
        if direction==">":
            new_board[j][i]="v"
        elif direction=="v":
            new_board[j][i]=">"

    return new_board, len(new_indices)

#Read the input
board=[]
with open("input_day_25","r") as fp:
    lines = fp.readlines()
    for line in lines:
        board.append(list(line.strip()))

total_nr_moves=-1
nr_rounds=0
while total_nr_moves!=0:
    board,total_nr_moves=move_board(board)
    nr_rounds+=1

print("Solution part 1: (and 2 :-))")
print(nr_rounds)






