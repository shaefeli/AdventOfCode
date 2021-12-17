#Board abstraction
class Board:
    def __init__(self, lines):
        self.lines=lines
        self.columns = []
        for i in range(len(lines[0])):
            self.columns.append([line[i] for line in lines])
            
    def update_and_notify(self,new_nr):
        isBingo=False
        for line in self.lines:
            if new_nr in line:
                line.remove(new_nr) 
                if len(line)==0:
                    isBingo=True
        for column in self.columns:
            if new_nr in column:
                column.remove(new_nr)
                if len(column)==0:
                    isBingo=True
        return isBingo
        
    def get_unmarked(self):
        unmarked_nrs=[]
        for line in self.lines:
            unmarked_nrs.extend(line)
        return unmarked_nrs


if __name__ == "__main__":
    #Read the input and parse into boards and drawn numbers
    drawn_numbers=[]
    boards=[]
    with open("input_day_4","r") as fp:
        lines = fp.readlines()
        currentBoard=[] #Lines of the board
        for i,line in enumerate(lines):
            if i==0:
                drawn_numbers.extend([int(x) for x in line.split(",")])
            else:
                if line!="\n":
                    currentBoard.append([int(x) for x in list(filter(lambda x: x!="",line.split(" ")))])
                
                if line=="\n" or i==len(lines)-1: 
                    if i!=1:
                        boards.append(Board(currentBoard))
                        currentBoard=[]
    
    #For part 1:
    found=False      
    for nr in drawn_numbers:
        if not found:
            for board in boards: 
                if board.update_and_notify(nr):
                    print("Solution of part 1:")
                    print(sum(board.get_unmarked())*nr)
                    boards.remove(board) #For consistency of part 2
                    found=True
                    break
    
    #For part 2:   
    #Here we remove a board once it wins
    #Note that it is possible to just do the 2 parts one after the other since the drawn numbers is the same order
    #And that the already drawn numbers have no influence on the result since we already removed the winning board of part 1
    lastResult=0
    remainingBoards = boards.copy()
    for nr in drawn_numbers:
        for board in boards:
            if board.update_and_notify(nr):
                lastResult = sum(board.get_unmarked())*nr
                remainingBoards.remove(board)
        boards=remainingBoards.copy()
    print("Solution of part 2:")
    print(lastResult)
             