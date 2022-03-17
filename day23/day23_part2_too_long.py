#THIS METHOD UNFORTUNATELY DOESN'T WORK (MAXIMUM RECURSION ERROR)
#USING RECURSIONS WITH DYNAMIC PROGRAMMING DOESN'T WORK
from itertools import chain
import math
from copy import deepcopy

#Where could a j,i amphipod go given the board would be empty
def possibleMovesEmptyBoard(current_j,current_i,configuration):
    current_amphipod=configuration[current_j][current_i]
    floor = [(0,0),(0,1),(0,3),(0,5),(0,7),(0,9),(0,10)]
    room=[]
    if current_amphipod=="A":
        room=[(1,0),(2,0),(3,0),(4,0)]
    elif current_amphipod=="B":
        room = [(1,1),(2,1),(3,1),(4,1)]
    elif current_amphipod=="C":
        room = [(1,2),(2,2),(3,2),(4,2)]
    elif current_amphipod=="D":
        room = [(1,3),(2,3),(3,3),(4,3)]
    rooms = set(floor)
    rooms.update(room)

    return rooms
  
#Add the constraint that the new place should be empty  
def possibleMovesNobodyIsHere(configuration, possibleRooms):
    possibleRoomsEmpty=possibleRooms.copy()
    for i in range(11):
        if configuration[0][i]!="0":
            possibleRoomsEmpty.discard((0,i))
    for j in range(1,5):
        for i in range(4):
            if configuration[j][i]!="0":
                possibleRoomsEmpty.discard((j,i))
    return possibleRoomsEmpty

#Check if that there is currently no stranger in the room they want to go
def possibleMovesRoomIsOk(current_j,current_i, configuration, possibleRooms):
    possibleMovesRoom=possibleRooms.copy()
    current_amphipod=configuration[current_j][current_i]
    for i in range(4):
        #Check if there is someone different in the room 
        thereIsSomeoneDifferent=False
        for j in range(1,5):
            if configuration[j][i]!=current_amphipod and configuration[j][i]!="0":
                thereIsSomeoneDifferent=True
                break
        if thereIsSomeoneDifferent: #Remove that room
            for j in range(1,5):
                possibleMovesRoom.discard((j,i))
    return possibleMovesRoom
  
#Check that the move is possible and that onbody is on the way  
def possibleMovesNonBlocking(current_j,current_i,configuration, possibleMoves):
    finalPossibleMoves=possibleMoves.copy()
    
    #If we are in the room
    for move in possibleMoves:
        if current_j>=1:
            #and we want to go somewhere on the floor
            if move[0]==0:
                #Check if we can go out of the room
                canGoOutOfRoom=True
                for j in range(1,current_j):
                    if configuration[j][current_i]!="0":
                        canGoOutOfRoom=False
                if not canGoOutOfRoom:
                    finalPossibleMoves.discard(move)
                
                #Check that we can go right if we want to go right
                if move[1]>current_i:
                    canGoRight=True
                    for i in range(current_i+1,move[1]):
                        if configuration[0][i]!="0":
                            canGoRight=False
                    if not canGoRight:
                        finalPossibleMoves.discard(move)
                        
                #Check that we can go left if we want to go left
                elif move[1]<current_i:
                    canGoLeft=True
                    for i in range(move[1],current_i-1):
                        if configuration[0][i]!="0":
                            canGoLeft=False
                    if not canGoLeft:
                        finalPossibleMoves.discard(move)
                        
            #and we want to go in a room
            else:
                #Check if we can go out of the room
                canGoOutOfRoom=True
                for j in range(1,current_j):
                    if configuration[j][current_i]!="0":
                        canGoOutOfRoom=False
                if not canGoOutOfRoom:
                    finalPossibleMoves.discard(move)
                
                correspondingCoordOnFloor=(move[1]+1)*2

                #Check that we can go right if we want to go right
                if correspondingCoordOnFloor>current_i:
                    canGoRight=True
                    for i in range(current_i+1,correspondingCoordOnFloor):
                        if configuration[0][i]!="0":
                            canGoRight=False
                    if not canGoRight:
                        finalPossibleMoves.discard(move)
                        
                #Check that we can go left if we want to go left
                elif correspondingCoordOnFloor<current_i:
                    canGoLeft=True
                    for i in range(correspondingCoordOnFloor,current_i-1):
                        if configuration[0][i]!="0":
                            canGoLeft=False
                    if not canGoLeft:
                        finalPossibleMoves.discard(move)
                
                #Check if we can go in the room
                canGoInRoom=True
                for j in range(1,move[0]):
                    if configuration[j][move[1]]!="0":
                        canGoInRoom=False
                if not canGoInRoom:
                    finalPossibleMoves.discard(move)
    
        #If we are on the floor
        else:
            #And we want to go on the floor
            if move[0]==0:
                #Check that we can go right if we want to go right
                if move[1]>current_i:
                    canGoRight=True
                    for i in range(current_i+1,move[1]):
                        if configuration[0][i]!="0":
                            canGoRight=False
                    if not canGoRight:
                        finalPossibleMoves.discard(move)
                        
                #Check that we can go left if we want to go left
                elif move[1]<current_i:
                    canGoLeft=True
                    for i in range(move[1],current_i-1):
                        if configuration[0][i]!="0":
                            canGoLeft=False
                    if not canGoLeft:
                        finalPossibleMoves.discard(move)
                        
            #And we want to go in a room
            else:
                correspondingCoordOnFloor=(move[1]+1)*2
                #Check that we can go right if we want to go right
                if correspondingCoordOnFloor>current_i:
                    canGoRight=True
                    for i in range(current_i+1,correspondingCoordOnFloor):
                        if configuration[0][i]!="0":
                            canGoRight=False
                    if not canGoRight:
                        finalPossibleMoves.discard(move)
                        
                #Check that we can go left if we want to go left
                elif correspondingCoordOnFloor<current_i:
                    canGoLeft=True
                    for i in range(correspondingCoordOnFloor,current_i-1):
                        if configuration[0][i]!="0":
                            canGoLeft=False
                    if not canGoLeft:
                        finalPossibleMoves.discard(move)
                
                #Check if we can go in the room
                canGoInRoom=True
                for j in range(1,move[0]):
                    if configuration[j][move[1]]!="0":
                        canGoInRoom=False
                if not canGoInRoom:
                    finalPossibleMoves.discard(move)

    return finalPossibleMoves
 
def roomNrAmphipod(amphipod):
    if amphipod=="A":
        return 0
    if amphipod=="B":
        return 1
    if amphipod=="C":
        return 2
    if amphipod=="D":
        return 3
        
#We don't want the amphipod to go up and down in the room if it is his room, and there is no amphipod to liberate 
def usefulMoves(current_j,current_i,configuration, possibleMoves):
    finalMoves=possibleMoves.copy()
    current_amphipod=configuration[current_j][current_i]
    for move in possibleMoves:
        if move[1]>=1 and current_j>=1:
            if move[0]==current_i:
                #Not allowed to go up if it is his room
                if move[1]<current_j:
                    if current_i==roomNrAmphipod(current_amphipod):
                        finalMoves.discard(move)
                           
                #Not Allowed to go down only if there is an anmphipod which is different
                if move[1]>current_j:
                    for j in range(current_j+1,5):
                        if configuration[j][current_i]!=current_amphipod:
                            finalMoves.discard(move)
                            break
    return finalMoves
                
    
def getPossibleMoves(current_j,current_i,configuration):
    emptyPossible=possibleMovesEmptyBoard(current_j,current_i,configuration)
    moveFree=possibleMovesNobodyIsHere(configuration,emptyPossible)
    moveRoomIsOk=possibleMovesRoomIsOk(current_j,current_i,configuration,moveFree)
    finalMoves=possibleMovesNonBlocking(current_j,current_i,configuration,moveRoomIsOk)
    OnlyUsefulMoves=usefulMoves(current_j,current_i,configuration,finalMoves)
    return OnlyUsefulMoves
    
def isAtEndingPosition(current_j,current_i,configuration):
    current_amphipod=configuration[current_j][current_i]
    room=-1
    if current_amphipod=="A":
        room=0
    elif current_amphipod=="B":
        room =1
    elif current_amphipod=="C":
        room =2
    elif current_amphipod=="D":
        room =3
        
    if current_j!=0:
        if current_i==room:
            #Check that below them there is either nothing or same amphoids 
            for j in range(current_j+1,5):
                if configuration[j][current_i]!=current_amphipod:
                    return False
                    break
            return True
    return False
                    
def configurationToString(configuration):
    conf_string=""
    for conf in configuration:
        conf_string+="".join(conf)
    return conf_string
    
def numberOfMoves(current_j,current_i,dest_j,dest_i):
    #If is in room and destination is in same room
    if current_j>=1 and dest_i==current_i:
        return abs(current_j-dest_j)
        
    #If in floor and dest is on floor
    if current_j==0 and dest_j==0:
        return abs(current_i-dest_i)
        
    #If in floor and goes to room
    if current_j==0 and dest_j>=1:
        correspondingFloorPosition=(dest_i+1)*2
        floorPath=abs(correspondingFloorPosition-current_i)
        roomPath=dest_j
        return roomPath+floorPath
    
    #If in room and goes to room
    if current_j>=1 and dest_j>=1:
        upRoom=current_j
        destRoom=dest_j
        correspondingCoordOnStart=(current_i+1)*2
        correspondingCoordOnEnd=(dest_i+1)*2
        floorPath=abs(correspondingCoordOnStart-correspondingCoordOnEnd)
        return upRoom+destRoom+floorPath
    
    #If in room and goes to floor
    if current_j>=1 and dest_j==0:
        upRoom=current_j
        correspondingCoordOnFloor=(current_i+1)*2
        floorPath=abs(correspondingCoordOnFloor-current_i)
        return floorPath+upRoom
        
def cost(current_amphipod,nr_moves):
    if current_amphipod=="A":
        return nr_moves
    elif current_amphipod=="B":
        return nr_moves*10
    elif current_amphipod=="C":
        return nr_moves*100
    elif current_amphipod=="D":
        return nr_moves*1000

def copyBoard(configuration):
    new_conf=[]
    first_row=["0"]*11
    for i in range(11):
        first_row[i]=configuration[0][i]
    new_conf.append(first_row)
    for jj in range(1,5):
        new_row=["0"]*4
        for ii in range(4):
            new_row[ii]=configuration[jj][ii]
        new_conf.append(new_row)
    return new_conf
    
def createNewConfiguration(current_j,current_i,move, configuration):
    new_configuration=copyBoard(configuration)
    amphipod_to_move=configuration[current_j][current_i]
    new_configuration[current_j][current_i]="0"
    new_configuration[move[0]][move[1]]=amphipod_to_move
    new_cost = cost(amphipod_to_move,numberOfMoves(current_j,current_i,move[0],move[1]))
    return new_configuration,new_cost
    
def calculateMinCost(configuration, currentCost,visitedConfigurations):
    if configurationToString(configuration)=="00000000000ABCDABCDABCDABCD":
        return currentCost
    #Move the stuff that are on floor
    all_move_costs=[]
    for i in range(11):
        if configuration[0][i]!="0":
            moves=getPossibleMoves(0,i,configuration)
            for move in moves:
                new_conf,new_cost=createNewConfiguration(0,i,move,configuration)
                if configurationToString(new_conf) not in visitedConfigurations:
                    cost=-1
                    if configurationToString(new_conf) in globalDict:
                        cost=globalDict[configurationToString(new_conf)]
                    else:
                        new_visited_confs=visitedConfigurations.copy()
                        new_visited_confs.add(configurationToString(new_conf))
                        cost = calculateMinCost(new_conf,currentCost+new_cost,new_visited_confs)
                    all_move_costs.append(cost)
            
    for jj in range(1,5):
        for ii in range(4):
            if configuration[jj][ii]!="0" and not isAtEndingPosition(jj,ii,configuration):
                moves=getPossibleMoves(jj,ii,configuration)
                for move in moves:
                    new_conf,new_cost=createNewConfiguration(jj,ii,move,configuration)
                    if configurationToString(new_conf) not in visitedConfigurations:
                        cost=-1
                        if configurationToString(new_conf) in globalDict:
                            cost=globalDict[configurationToString(new_conf)]
                        else:
                            new_visited_confs=visitedConfigurations.copy()
                            new_visited_confs.add(configurationToString(new_conf))
                            cost = calculateMinCost(new_conf,currentCost+new_cost,new_visited_confs)
                        all_move_costs.append(cost)
                            
    if len(all_move_costs)!=0:
        globalDict[configurationToString(configuration)]=min(all_move_costs)
        return min(all_move_costs)
    else:
        return math.inf
        
#Input is hardcoded here     
configuration=[["0"]*11,["C","B","D","A"],["D","C","B","A"],["D","B","A","C"],["B","D","A","C"]]
globalDict=dict() #Dict of configuration to min cost in order to not recompute confs that we already did
visited=set()
visited.add(configurationToString(configuration))
print(calculateMinCost(configuration,0,visited))