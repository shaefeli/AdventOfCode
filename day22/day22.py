if __name__=="__main__":
    with open("input_day_22","r") as fp:
        input_coords=[]
        for line in fp.readlines():
            first_sep=line.strip().split(" ")
            on_or_off=first_sep[0]
            coordinates=first_sep[1].split(",")
            start_coords=[]
            end_coords=[]
            for coord in coordinates:
                numbers=coord.split("=")[1].split("..")
                start_coords.append(int(numbers[0]))
                end_coords.append(int(numbers[1]))
            input_coords.append((on_or_off,start_coords,end_coords))

#Part 1 
input_instructions_pt1=input_coords[:20]
on_coords=set()
for instruction in input_instructions_pt1:
    for x in range(instruction[1][0],instruction[2][0]+1):
            for y in range(instruction[1][1],instruction[2][1]+1):
                for z in range(instruction[1][2],instruction[2][2]+1):
                    if instruction[0]=="on":
                        on_coords.add((x,y,z))
                    else:
                        on_coords.discard((x,y,z))  

print("Solution part 1:")
print(len(on_coords))
        
def getCubeDifference(coords1Start,coords1End,coords2Start,coords2End):
    #What is in cube 2 that is not in cube 1?
    #Start coords are always smaler than end coords
    #Coords1 are our "base" cube, we compare coords2 with coords1
    #In order to give the express the difference, we answer with a list of cubes
    x1_start=coords1Start[0]
    y1_start=coords1Start[1]
    z1_start=coords1Start[2]
    x2_start=coords2Start[0]
    y2_start=coords2Start[1]
    z2_start=coords2Start[2]
    x1_end=coords1End[0]
    y1_end=coords1End[1]
    z1_end=coords1End[2]
    x2_end=coords2End[0]
    y2_end=coords2End[1]
    z2_end=coords2End[2]
    
    cubesAreDisjoint=x2_end<x1_start or x2_start>x1_end or y2_end<y1_start or y2_start>y1_end or z2_end<z1_start or z2_start>z1_end
    if cubesAreDisjoint:
        return [(coords2Start,coords2End)]
        
    #The result of the difference between cube 2 and cube 1 are 6 new cubes 
    #(Overshooting cube 2 parts from cube 1 in the 6 directions)

    #Top cube
    top_cube=((x2_start,y2_start,z1_end+1),(x2_end,y2_end,z2_end))
    #bottom cube
    bottom_cube=((x2_start,y2_start,z2_start),(x2_end,y2_end,z1_start-1))
    #Left cube (care to not overlap top and bottom cube)
    left_cube=((x2_start,y2_start,max(z1_start,z2_start)),(x1_start-1,y2_end,min(z1_end,z2_end)))
    #Right cube (care to not overlap top and bottom cube)
    right_cube=((x1_end+1,y2_start,max(z1_start,z2_start)),(x2_end,y2_end,min(z1_end,z2_end)))
    #Back cube (care to not overlap top, bottom, left and right cube)
    back_cube=((max(x1_start,x2_start),y1_end+1,max(z1_start,z2_start)),(min(x1_end,x2_end),y2_end,min(z1_end,z2_end)))
    #Front cube (care to not overlap top, bottom, left and right cube)
    front_cube=((max(x1_start,x2_start),y2_start,max(z1_start,z2_start)),(min(x1_end,x2_end),y1_start-1,min(z1_end,z2_end)))
    potentialCubes = [top_cube,bottom_cube,left_cube,right_cube,back_cube,front_cube]
    
    #Keep only real cubes and squares)
    new_cubes=[]
    for cube in potentialCubes:
        diffs=[cube[1][0]-cube[0][0],cube[1][1]-cube[0][1],cube[1][2]-cube[0][2]]
        putCube=True
        for diff in diffs:
            if diff<0:
                putCube=False
                break
        if putCube:
            new_cubes.append(cube)
    return new_cubes

#Part 2
#As we go through the "on" cubes, we do a disjoint union with the new on cube with the existing on cubes
#Whenever we find an "off" cube, we set the current "on" cubes to be the difference between them and the off cube
current_on_cubes=set()
for i,input_coord in enumerate(input_coords):
    if i%10==0:
        print(int(i/len(input_coords)*100),"% done")
    cube_to_process=(input_coord[1]),(input_coord[2])
    if input_coord[0]=="on":
        disjoint_part=set()
        disjoint_part.add(tuple(cube_to_process[0]+cube_to_process[1]))
        for on_cube in current_on_cubes:
            new_disjoint_parts=set()
            for part in disjoint_part:
                new_cubes=getCubeDifference(on_cube[:3],on_cube[3:],part[:3],part[3:])
                for new_c in new_cubes:
                    new_disjoint_parts.add(tuple(new_c[0]+new_c[1]))
            disjoint_part=new_disjoint_parts.copy()
        current_on_cubes.update(disjoint_part)
    else:
        new_current_on_cubes=set()
        for on_cube in current_on_cubes:
            new_cubes=getCubeDifference(cube_to_process[0],cube_to_process[1],on_cube[:3],on_cube[3:])
            for new_c in new_cubes:
                new_current_on_cubes.add(tuple(new_c[0]+new_c[1]))
        current_on_cubes=new_current_on_cubes.copy()
                 
totalSum=0
for c in current_on_cubes:
    totalSum+=(c[3]-c[0]+1)*(c[4]-c[1]+1)*(c[5]-c[2]+1)
print("Solution part 2:")  
print(totalSum)




     
        

                
    


