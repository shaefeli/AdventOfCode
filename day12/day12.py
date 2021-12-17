def isSmallCave(cave):
    return cave.upper()!=cave #True is small letters
    
def isTwiceInPath(path,cave):
    caves=path.split(",")
    count=0
    for c in caves:
        if c==cave:
            count+=1
    return count==2
    
def find_all_path_pt1(currentAdjency,currentNode,currentPath):
    next_caves=currentAdjency[currentNode]
    new_current_path=currentPath
    if new_current_path=="":
        new_current_path+=currentNode
    else:
        new_current_path+=","+currentNode
    if currentNode=="end":
        paths_pt1.append(new_current_path)
    #Continue if we can
    for next_cave in next_caves:
        if next_cave in currentAdjency.keys():
            new_current_adjency=currentAdjency.copy()
            if isSmallCave(currentNode):
                del new_current_adjency[currentNode]
            find_all_path_pt1(new_current_adjency,next_cave,new_current_path)
            
def find_all_path_pt2(currentAdjency,currentNode,currentPath,doubledNode):
    next_caves=currentAdjency[currentNode]
    new_current_path=currentPath
    if new_current_path=="":
        new_current_path+=currentNode
    else:
        new_current_path+=","+currentNode
    if currentNode=="end":
        paths_pt2_doubled[doubledNode].append(new_current_path)
    else:
        for next_cave in next_caves:
            if next_cave in currentAdjency.keys():
                new_current_adjency=currentAdjency.copy()
                if isSmallCave(currentNode):
                    if currentNode!=doubledNode:
                        del new_current_adjency[currentNode]
                    else:
                        if isTwiceInPath(new_current_path,doubledNode):
                            del new_current_adjency[currentNode]
                find_all_path_pt2(new_current_adjency,next_cave,new_current_path,doubledNode)
        


if __name__ == "__main__":
    with open("input_day_12","r") as fp:
        cavesAdjency=dict()
        for line in fp.readlines():
            caves=line.strip().split("-")
            if caves[0] in cavesAdjency:
                cavesAdjency[caves[0]].append(caves[1])
            else:
                cavesAdjency[caves[0]]=[caves[1]]
            if caves[1] in cavesAdjency:
                cavesAdjency[caves[1]].append(caves[0])
            else:
                cavesAdjency[caves[1]]=[caves[0]]
                              
#Global variables used by recursive functions
paths_pt1=[]
paths_pt2_doubled=dict()

           
#Part 1  
print("Solution part 1:")
find_all_path_pt1(cavesAdjency,"start","") 
print(len(paths_pt1))


#Part 2
print("Solution part 2:")
smallCavesToDouble=[]
for cave in cavesAdjency.keys():
    if isSmallCave(cave) and cave!="start" and cave!="end":
        paths_pt2_doubled[cave]=[]
        smallCavesToDouble.append(cave)
        find_all_path_pt2(cavesAdjency,"start","",cave)
paths_pt2=set()
paths_pt2.update(paths_pt1) 
for cave in smallCavesToDouble:
    paths_pt2.update(paths_pt2_doubled[cave])    
print(len(paths_pt2)) 


        



