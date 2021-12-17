
def check_position(levels,i,j):
    if i==0 and j==0: #top left
        return levels[j][i]<levels[j][i+1] and \
                levels[j][i]<levels[j+1][i] 
    if i==0 and j==len(levels)-1: #bottom left
        return levels[j][i]<levels[j][i+1] and \
                levels[j][i]<levels[j-1][i]
    if i==len(levels[0])-1 and j==0: #top right
        return levels[j][i]<levels[j][i-1] and \
                levels[j][i]<levels[j+1][i]
    if i==len(levels[0])-1 and j==len(levels)-1: #bottom right
        return levels[j][i]<levels[j][i-1] and \
                levels[j][i]<levels[j-1][i]
    if i==0: #left line
        return levels[j][i]<levels[j-1][i] and \
                levels[j][i]<levels[j][i+1] and \
                levels[j][i]<levels[j+1][i]
    if j==0: #top line
        return levels[j][i]<levels[j][i-1] and \
                levels[j][i]<levels[j+1][i] and \
                levels[j][i]<levels[j][i+1]  
    if i==len(levels[0])-1: #right line
        return levels[j][i]<levels[j-1][i] and \
                levels[j][i]<levels[j][i-1] and \
                levels[j][i]<levels[j+1][i]
    if j==len(levels)-1: #bottom line
        return levels[j][i]<levels[j][i-1] and \
                levels[j][i]<levels[j-1][i] and \
                levels[j][i]<levels[j][i+1] 
    else:
        return levels[j][i]<levels[j][i-1] and \
                levels[j][i]<levels[j-1][i] and \
                levels[j][i]<levels[j][i+1] and \
                levels[j][i]<levels[j+1][i]
 

def get_neighbourghs(levels,i,j):
    neighbourghs=set()
    if i==0 and j==0: #top left
        if levels[j][i+1] != 9:
            neighbourghs.add((i+1,j))
        if levels[j+1][i] != 9:
            neighbourghs.add((i,j+1))
    elif i==0 and j==len(levels)-1: #bottom left
        if levels[j][i+1] != 9:
            neighbourghs.add((i+1,j))
        if levels[j-1][i] != 9:
            neighbourghs.add((i,j-1))
    elif i==len(levels[0])-1 and j==0: #top right
        if levels[j][i-1] != 9:
            neighbourghs.add((i-1,j))
        if levels[j+1][i] != 9:
            neighbourghs.add((i,j+1))
    elif i==len(levels[0])-1 and j==len(levels)-1: #bottom right
        if levels[j][i-1] != 9:
            neighbourghs.add((i-1,j))
        if levels[j-1][i] != 9:
            neighbourghs.add((i,j-1))
    elif i==0: #left line
        if levels[j-1][i] != 9:
            neighbourghs.add((i,j-1))
        if levels[j][i+1] != 9:
            neighbourghs.add((i+1,j))
        if levels[j+1][i] != 9:
            neighbourghs.add((i,j+1))
    elif j==0: #top line
        if levels[j][i-1] != 9:
            neighbourghs.add((i-1,j))
        if levels[j+1][i] != 9:
            neighbourghs.add((i,j+1))
        if levels[j][i+1] != 9: 
            neighbourghs.add((i+1,j))
    elif i==len(levels[0])-1: #right line
        if levels[j-1][i] != 9:
            neighbourghs.add((i,j-1))
        if levels[j][i-1] != 9:
            neighbourghs.add((i-1,j))
        if levels[j+1][i] != 9:
            neighbourghs.add((i,j+1))
    elif j==len(levels)-1: #bottom line
        if levels[j][i-1] != 9:
            neighbourghs.add((i-1,j))
        if levels[j-1][i] != 9:
            neighbourghs.add((i,j-1))
        if levels[j][i+1] != 9: 
            neighbourghs.add((i+1,j))
    else:
        if levels[j][i-1] != 9:
            neighbourghs.add((i-1,j))
        if levels[j-1][i] != 9:
            neighbourghs.add((i,j-1))
        if levels[j][i+1] != 9:
            neighbourghs.add((i+1,j))
        if levels[j+1][i] != 9:
            neighbourghs.add((i,j+1))
    return neighbourghs
    
def get_all_neighbourghs(levels, known_neighbourghs, new_neighbourghs):
    next_gen_new_neighbourghs=set()
    for neighbourgh in new_neighbourghs:
        known_neighbourghs.add(neighbourgh)
        i,j = neighbourgh
        newly_found_neighbourghs = get_neighbourghs(levels,i,j)
        for newly_found in newly_found_neighbourghs:
            if newly_found not in known_neighbourghs:
                next_gen_new_neighbourghs.add(newly_found)
        if len(next_gen_new_neighbourghs)!=0:
            get_all_neighbourghs(levels, known_neighbourghs,next_gen_new_neighbourghs)
    return known_neighbourghs        

def process_basin(levels,i,j):
    new_neighbourghs=set()
    new_neighbourghs.add((i,j))
    return get_all_neighbourghs(levels, set(),new_neighbourghs)

if __name__ == "__main__":
    with open("input_day_9","r") as fp:
        smoke_levels=[]
        for line in fp.readlines():
            smoke_levels.append([int(x) for x in line.strip()])                 
#Part 1
total_risk_level=0
for i in range(len(smoke_levels[0])):
    for j in range(len(smoke_levels)):
        if check_position(smoke_levels,i,j):
            total_risk_level+=(smoke_levels[j][i]+1)
            
print("Solution part 1")
print(total_risk_level)


#Part 2
basins=[]
for i in range(len(smoke_levels[0])):
    for j in range(len(smoke_levels)):
        #Check if the coordinate is already in a basin
        isInBasin=False
        for basin in basins:
            if (i,j) in basin:
                isInBasin=True
                break
        if smoke_levels[j][i]!=9 and not isInBasin:
            basins.append(process_basin(smoke_levels,i,j))
            
            
three_biggest_sizes = sorted([len(basin) for basin in basins],reverse=True)[:3] 
result=1   
for size in three_biggest_sizes:
    result*=size
print("Solution part 2:")
print(result)



