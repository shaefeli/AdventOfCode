class Line:
    def __init__(self,line_str):
        coord_str = [x.strip() for x in line_str.split("->")]
        self.x1 = int(coord_str[0].split(",")[0])
        self.y1 = int(coord_str[0].split(",")[1])
        self.x2 = int(coord_str[1].split(",")[0])
        self.y2 = int(coord_str[1].split(",")[1])
        self.is_straight_line = (self.x1==self.x2 or self.y1==self.y2)
        self.filled_squares = self.generate_filled(self.x1,self.y1,self.x2,self.y2)

    def generate_filled(self,x1,y1,x2,y2):
        coordinates = set()
        #Vertical
        if x1==x2:
            start_y = y1 if y1<y2 else y2
            end_y = y1 if y1>y2 else y2
            for y in range(start_y,end_y+1):
                coordinates.add((x1,y))
            return coordinates
        #Horizontal
        elif y1==y2:
            start_x = x1 if x1<x2 else x2
            end_x = x1 if x1>x2 else x2
            for x in range(start_x,end_x+1):
                coordinates.add((x,y1))
            return coordinates
        #45 degrees diagonal
        else:
            diff_x = x2-x1
            diff_y = y2-y1
            sign_x = 1 if diff_x>0 else -1
            sign_y = 1 if diff_y>0 else -1
            for i in range(abs(diff_x)+1):
                coordinates.add((x1+i*sign_x,y1+i*sign_y))
            return coordinates
 
class Square:
    def __init__(self,lines):
        self.square=dict()
        for line in lines:
            for coord in line.filled_squares:
                if coord in self.square:
                    self.square[coord]+=1
                else:
                    self.square[coord]=1
    
    def get_nr_overlaps(self):
        return len(list(filter(lambda x: x>=2, self.square.values())))
        
#Parse input
#Note that all lines are either 45 degrees diagonal or straight
lines=[]
with open("input_day_5","r") as fp:
    for i,line in enumerate(fp.readlines()):
        lines.append(Line(line))

square_straight = Square(list(filter(lambda x: x.is_straight_line,lines)))
print("Solution part 1:")
print(square_straight.get_nr_overlaps()) 

square_all = Square(lines)
print("Solution part 2:")
print(square_all.get_nr_overlaps())