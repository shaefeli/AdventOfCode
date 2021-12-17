if __name__ == "__main__":
    with open("input_day_15","r") as fp:
        risk_levels_pt1=[[int(x) for x in line.strip()] for line in fp.readlines()]

def get_neighbourgh_indices(index,width,height):
    i=index[0]
    j=index[1]
    if i==0 and j==height-1:
        return [(i+1,j),(i,j-1)]
    elif i==width-1 and j==height-1:
        return [(i-1,j),(i,j-1)]
    elif i==width-1 and j==0:
        return [(i-1,j),(i,j+1)]
    elif i==0:
        return [(i,j-1),(i+1,j),(i,j+1)]
    elif j==0:
        return [(i-1,j),(i,j+1),(i+1,j)]
    elif i==width-1:
        return [(i,j-1),(i-1,j),(i,j+1)]
    elif j==height-1:
        return [(i-1,j),(i,j-1),(i+1,j)]
    else:
        return [(i-1,j),(i,j-1),(i+1,j),(i,j+1)]
        

def compute_total_risk_level(index,width,height,total_risk_levels, risk_levels, nr_risk_levels):
    #Min for current index
    i=index[0]
    j=index[1]
    if i==0 and j==0:
        total_risk_levels[j][i]=risk_levels[j][i]
    else:
        indices_to_come_from=get_neighbourgh_indices(index,width,height)
        if len(indices_to_come_from)==1:
            from_i, from_j = indices_to_come_from[0]
            total_risk_levels[j][i]=risk_levels[j][i] + total_risk_levels[from_j][from_i]
        else:
            minimumVal = nr_risk_levels*10
            minIndex = (-1,-1)
            for index in indices_to_come_from:
                if total_risk_levels[index[1]][index[0]]<minimumVal:
                    minimumVal=total_risk_levels[index[1]][index[0]]
                    minIndex=index
            total_risk_levels[j][i]=risk_levels[j][i] + minimumVal
            
        
#Part 1 
#We solve this problem with Dynamic programming
#The risk level of a position (i,j) can formally be defined as.
#R(i,j) is the total risk to position (i,j), r(i,j) is the single risk at position (i,j)
#R(i,j) = r(i,j) + min(R(i-1,j);R(i,j-1);R(i+1,j);R(i,j+1))
#In order to take in account paths coming from the right and bottom, we do multiple sweeps 
width_pt1=len(risk_levels_pt1[0])
height_pt1=len(risk_levels_pt1)
nr_risk_levels_pt1=width_pt1*height_pt1
total_risk_levels_pt1=[[nr_risk_levels_pt1*9]*width_pt1 for i in range(height_pt1)]

for e in range(3):
    for i in range(width_pt1):
        for j in range(height_pt1):
            compute_total_risk_level((i,j),width_pt1,height_pt1,total_risk_levels_pt1, risk_levels_pt1, nr_risk_levels_pt1)

print("Solution part 1:")
print(total_risk_levels_pt1[height_pt1-1][width_pt1-1]-total_risk_levels_pt1[0][0])


#Part 2
#Create risk levels for part 2
width_pt2=len(risk_levels_pt1[0])*5
height_pt2=len(risk_levels_pt1)*5
nr_risk_levels_pt2=width_pt2*height_pt2
total_risk_levels_pt2=[[nr_risk_levels_pt2*9]*width_pt2 for i in range(height_pt2)]

risk_levels_pt2=[[-1]*width_pt2 for e in range(height_pt2)]
for i in range(5):
    for j in range(5):
        toAdd=i+j
        for ii in range(len(risk_levels_pt1[0])):
            for jj in range(len(risk_levels_pt1)):
                new_val = (risk_levels_pt1[jj][ii]+toAdd-1)%9+1
                risk_levels_pt2[j*height_pt1+jj][i*width_pt1+ii]=new_val

for e in range(10):
    for i in range(width_pt2):
        for j in range(height_pt2):
            compute_total_risk_level((i,j),width_pt2,height_pt2,total_risk_levels_pt2, risk_levels_pt2, nr_risk_levels_pt2)
            
print("Solution part 2:")             
print(total_risk_levels_pt2[height_pt2-1][width_pt2-1]-total_risk_levels_pt2[0][0])          
    


