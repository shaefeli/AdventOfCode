#We use as a naming convention a scanner to be what a certain scanner sees in its orientation. 
#A cube of a scanner is the set of coordinates of a scanner in one particular orientation

#Given a pair of coordinates in any orientation, generate the coordinates for the same position but all possible orientations
def generate24Coordinates(coord):
    x=coord[0]
    y=coord[1]
    z=coord[2]
    all_coord=[]
    #Cadran (x,y,z) ok
    all_coord.append((x,y,z)) 
    all_coord.append((y,z,x)) 
    all_coord.append((z,x,y)) 
    #Cadran (-x,y,z) 
    all_coord.append((y,-x,z)) 
    all_coord.append((-x,z,y)) 
    all_coord.append((z,y,-x)) 
    #Cadran (-x,-y,z)
    all_coord.append((-x,-y,z)) 
    all_coord.append((-y,z,-x)) 
    all_coord.append((z,-x,-y)) 
    #Cadran (x,-y,z)
    all_coord.append((-y,x,z)) 
    all_coord.append((x,z,-y)) 
    all_coord.append((z,-y,x)) 
    #Cadran (x,y,-z)
    all_coord.append((y,x,-z)) 
    all_coord.append((x,-z,y)) 
    all_coord.append((-z,y,x)) 
    #Cadran (-x,y,-z)
    all_coord.append((-x,y,-z)) 
    all_coord.append((y,-z,-x)) 
    all_coord.append((-z,-x,y)) 
    #Cadran (-x,-y,-z)
    all_coord.append((-y,-x,-z)) 
    all_coord.append((-x,-z,-y))
    all_coord.append((-z,-y,-x))
    #Cadran (x,-y,-z)
    all_coord.append((x,-y,-z))
    all_coord.append((-y,-z,x))
    all_coord.append((-z,x,-y))                      
    return all_coord            
 
#Generate all possible cubes for a scanner
def coordinatesAllOrientations(coordinates):
    all_coordinates_per_coord = [generate24Coordinates(coord) for coord in coordinates]
    cubes=[]
    for i in range(len(all_coordinates_per_coord[0])):
        cubes.append([coord[i] for coord in all_coordinates_per_coord])
    return cubes

#Check if 2 cubes are overlapping
#Note the trick to reduce complexity drastically: You "vote" for translations from one cube to another,
#Keep the vote if it has more than 12 votes. 
def checkCube(cube1,cube2): #Check if at least 12 beacons are similar
    translations=dict() #Compute the translation that we would need between every pair of points
    for pt1 in cube1:
        for pt2 in cube2:
            diff_x=pt1[0]-pt2[0]
            diff_y=pt1[1]-pt2[1]
            diff_z=pt1[2]-pt2[2]
            translation=(diff_x,diff_y,diff_z)
            if translation in translations:
                translations[translation]+=1
            else:
                translations[translation]=1
    for trans,val in translations.items():
        if val>=12:
            return trans
    return None
    
def translateCoord(coord,trans):
    return (coord[0]+trans[0],coord[1]+trans[1],coord[2]+trans[2])

#Check two scanners if they are pairs
#For this, we use the scan1 as a reference (one cube for it), and compare the 24 cubes of scanner 2 to scanner 1
#If there is a match, return the coordinates of the cube of scan2 in the scan1 reference and the translation needed
def checkScannerPair(scan1,scan2):
    cubesScan2 = coordinatesAllOrientations(scan2)
    translation=None
    cubeThatWorkedIndex=-1
    for i,cube2 in enumerate(cubesScan2):
        translation = checkCube(scan1,cube2)
        if translation!=None:
            cubeThatWorkedIndex=i
            break 
    InScan1Coord=None
    if translation!=None:
        #To go from scan2 to scan1, you need to use the cubeThatWorkedIndex cube of scan2, and then translate the coordinates by trans (x2,y2,z2)+trans
        InScan1Coord = [translateCoord(x,translation) for x in cubesScan2[cubeThatWorkedIndex]]
    return InScan1Coord, translation
  
#We define scanner 0 to be the reference.
#We then find pairs with scanner 0, and transform their scanners into absolute coordinates.
#We then use them as references again to find other pairs.  
def getCubesInAbsolute(scanners): #We define the absolute to be scanner 0
    scannersToPair=list(range(1,len(scanners)))
    knownScanners=[]
    scannersInAbsolute=dict()
    translationsToAbsolute=dict()
    scannersInAbsolute[0]=scanners[0]
    translationsToAbsolute[0]=(0,0,0)
    
    #First get all pairs that pair with scanner 0
    for i in range(1,len(scanners)):
        j_inCoord_ref, translation_to_ref =checkScannerPair(scanners[0],scanners[i])
        if translation_to_ref != None:
            scannersInAbsolute[i]=j_inCoord_ref
            translationsToAbsolute[i]=translation_to_ref
            scannersToPair.remove(i)
            knownScanners.append(i)
    
        
    while(len(scannersToPair)!=0):
        for scannerToPair in scannersToPair:
            for knownScanner in knownScanners:
                j_inCoord_ref, translation_to_ref =checkScannerPair(scannersInAbsolute[knownScanner],scanners[scannerToPair])
                if translation_to_ref != None:
                    scannersInAbsolute[scannerToPair]=j_inCoord_ref
                    translationsToAbsolute[scannerToPair]=translation_to_ref
                    knownScanners.append(scannerToPair)
                    break
        for knownScanner in knownScanners:
            if knownScanner in scannersToPair:
                scannersToPair.remove(knownScanner)
    
    return scannersInAbsolute,translationsToAbsolute
            
def manhattanDistance(coord1,coord2):
    return abs(coord1[0]-coord2[0])+abs(coord1[1]-coord2[1])+abs(coord1[2]-coord2[2])

if __name__ == "__main__":
    #with open("test_input_19","r") as fp:
    with open("input_day_19","r") as fp:
        scanners=[]
        currentScanner=[]
        lines=fp.readlines()
        for i,line in enumerate(lines):
            if len(line.strip())==0:
                scanners.append(currentScanner)
                currentScanner=[]
            elif "scanner" in line:
                pass
            elif i==len(lines)-1:
                coords=line.strip().split(",")
                coordinate=(int(coords[0]),int(coords[1]),int(coords[2]))
                currentScanner.append(coordinate)
                scanners.append(currentScanner)
            else:
                coords=line.strip().split(",")
                coordinate=(int(coords[0]),int(coords[1]),int(coords[2]))
                currentScanner.append(coordinate)
   
#Part 1
absBoards, translations = getCubesInAbsolute(scanners)
all_coordinates_abs=set()
for scanNr, absScan in absBoards.items():
    for coord in absScan:
        all_coordinates_abs.add(coord)
print("Solution part 1:")
print(len(all_coordinates_abs))

#Part 2
largestManhattanDistance=0
for i in range(len(scanners)):
    for j in range(i+1,len(scanners)):
        manDist = manhattanDistance(translations[i],translations[j])
        if manDist>largestManhattanDistance:
            largestManhattanDistance=manDist
print("Solution part 2:")
print(largestManhattanDistance)
        
        

                
    


