def fold(board,direction,axis):
    #Note that in our input, right side is always smaller than the left side if fold is x
    #Also, top is always bigger than bottom side if fold is y
    if direction=="x":
        #Step1: calculate new dimensions of board
        height=len(board)
        left=axis
        right=len(board[0])-(axis+1)
        width=max(left,right)
        #Step2: Create the new board
        new_board=[["."]*(width) for i in range(height)] 
        #Step3: fill in the board
        if left>=right:
            #We fold from right to left. The left just stays as it is
            for i in range(width):
                for j in range(height):
                    new_board[j][i]=board[j][i]
            #Get the right to the left
            for i in range(axis+1,len(board[0])):
                for j in range(height):
                    diff_with_axis=i-axis
                    new_x=axis-diff_with_axis
                    if board[j][i]=="#":
                        new_board[j][new_x]=board[j][i]
        return new_board
        
    else:
        #Step1: calculate new dimensions of board
        width=len(board[0])
        top=axis
        bottom=len(board)-(axis+1)
        height=max(top,bottom)
        #Step2: Create the new board
        new_board=[["."]*(width) for i in range(height)] 
        #Step3: fill in the board
        if top>=bottom:
            #We fold from bottom to top. The top just stays as it is
            for i in range(width):
                for j in range(height):
                    new_board[j][i]=board[j][i]
            #Get the bottom to the top
            for i in range(width):
                for j in range(axis+1,len(board)):
                    diff_with_axis=j-axis
                    new_y=axis-diff_with_axis
                    if board[j][i]=="#":
                        new_board[new_y][i]=board[j][i]
        return new_board  
      

coordinates=[]
folds=[]
if __name__ == "__main__":
    with open("input_day_13","r") as fp:
        #for line in test_input:
        for line in fp.readlines():
            if line.startswith("fold"):
                split = line.strip().split("=")
                folds.append((split[0][-1],int(split[1])))
            elif "," in line:
                split = line.strip().split(",")
                coordinates.append((int(split[0]),int(split[1])))
    
#Preparation work to create initial array
max_x=max([x[0] for x in coordinates])
max_y=max([x[1] for x in coordinates])
board=[["."]*(max_x+1) for i in range(max_y+1)] 
for coord in coordinates:
    board[coord[1]][coord[0]]="#"
         
#Part 1  
#Note that we don't fold in the middle...
#0-1-....-1306-1307
#0-1-..-654-[655]-656-...-1307
#Left: 655
#Right: 652
new_board=fold(board,folds[0][0],folds[0][1])
dots_count=0
for i in range(len(new_board[0])):
    for j in range(len(new_board)):
        if new_board[j][i]=="#":
            dots_count+=1          
print("Solution part 1:")
print(dots_count)

#Part 2
new_board=board.copy()
for folding in folds:
    new_board=fold(new_board,folding[0],folding[1])
print("Solution part 2:")
for line in new_board:
    print(line)
print("JPZCUAUR")



        



