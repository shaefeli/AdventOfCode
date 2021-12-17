import sys

def get_neighbourgh_indices(i,j):
    if i==0 and j==0: #top left
        return [(i+1,j),(i+1,j+1),(i,j+1)]
    if i==0 and j==height-1: #bottom left
        return [(i+1,j),(i+1,j-1),(i,j-1)]
    if i==width-1 and j==0: #top right
        return [(i-1,j),(i-1,j+1),(i,j+1)]
    if i==width-1 and j==height-1: #bottom right
        return [(i-1,j),(i-1,j-1),(i,j-1)]
    if i==0: #left line
        return [(i,j-1),(i+1,j-1),(i+1,j),(i+1,j+1),(i,j+1)]
    if j==0: #top line
        return [(i-1,j),(i-1,j+1),(i,j+1),(i+1,j+1),(i+1,j)]  
    if i==width-1: #right line
        return [(i,j-1),(i-1,j-1),(i-1,j),(i-1,j+1),(i,j+1)]
    if j==height-1: #bottom line
        return [(i-1,j),(i-1,j-1),(i,j-1),(i+1,j-1),(i+1,j)] 
    else:
        return [(i-1,j),(i-1,j-1),(i,j-1),(i+1,j-1),(i+1,j),(i+1,j+1),(i,j+1),(i-1,j+1)]
        


if __name__ == "__main__":
    with open("input_day_11","r") as fp:
        lines=[]
        for line in fp.readlines():
            lines.append([int(x) for x in line.strip()]) 
width=10
height=width  
    
#Part 1 and 2 in a variable
#We follow a naive approach since we can (small sizes (10x10), only 100 steps)
solutionPart2=-1
step=0
total_nr_flashing=0
while solutionPart2==-1 or step<=100:
    step+=1
    #First increase all levels by 1 and store indices of the ones that are flashing
    flashing_lights=[]
    for i in range(width):
        for j in range(height):
            if lines[j][i]==9:
                lines[j][i]=0
                flashing_lights.append((i,j))
            else:
                lines[j][i]+=1
    
    #Propagate the flashing
    while len(flashing_lights)!=0:
        new_flashing_lights=[]
        for flashing_light in flashing_lights:
            neighbourghs_to_increment = get_neighbourgh_indices(flashing_light[0],flashing_light[1])
            for neighb in neighbourghs_to_increment:
                if lines[neighb[1]][neighb[0]]==9:
                    lines[neighb[1]][neighb[0]]=0
                    new_flashing_lights.append((neighb[0],neighb[1]))
                elif lines[neighb[1]][neighb[0]]!=0: #If it is 0, it is already flashing
                    lines[neighb[1]][neighb[0]]+=1
        flashing_lights=new_flashing_lights.copy()
        
    #Count the number of flashing lights until step 100(useful for part 1)
    if step<=100:
        for i in range(width):
            for j in range(height):
                if lines[j][i]==0:
                    total_nr_flashing+=1
    
    #Check if all are flashing (useful for part 2)
    all_flashing=True
    for i in range(width):
        for j in range(height):
            if lines[j][i]!=0:
                all_flashing=False
                break
    if all_flashing:
        solutionPart2=step
            
                      
print("Solution part 1:")
print(total_nr_flashing)
print("Solution part 2:")
print(solutionPart2)
    


        



