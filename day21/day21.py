from collections import Counter

currentPosition=[9,6] #Input

#Part 1 (naive solution that works well)
currentPositionPt1=currentPosition.copy()
currentScore=[0,0]
turnToPlay=0
gameFinished=False
currentDiceValue=1
nrTimesDiceRolled=0
losingPlayerPoints=-1
while not gameFinished:
    #Three dice values rolled
    nr1=currentDiceValue
    currentDiceValue +=1 
    currentDiceValue=((currentDiceValue-1)%100)+1
    nr2=currentDiceValue
    currentDiceValue +=1 
    currentDiceValue=((currentDiceValue-1)%100)+1
    nr3=currentDiceValue
    currentDiceValue +=1 
    currentDiceValue=((currentDiceValue-1)%100)+1
    sumDice=nr1+nr2+nr3
    nrTimesDiceRolled+=3
    #Update position
    position_old=currentPositionPt1[turnToPlay]
    position_new=position_old+sumDice
    position_new=((position_new-1)%10)+1
    currentPositionPt1[turnToPlay]=position_new
    #Update score and check score
    currentScore[turnToPlay]+=currentPositionPt1[turnToPlay]
    if currentScore[turnToPlay]>=1000:
        gameFinished=True
        losingPlayer=1 if turnToPlay==0 else 0
        losingPlayerPoints=currentScore[losingPlayer]
    #Change turn
    turnToPlay=1 if turnToPlay==0 else 0
    
print("Solution part 1:")
print(losingPlayerPoints*nrTimesDiceRolled)

#Note that out of these 27 spaces, there are only 7 distinct spaces, which we use for optimization
def generateSpaces():
    spaces=[]
    for i in range(1,4):
        for j in range(1,4):
            for k in range(1,4):
                spaces.append(i+j+k)
    return Counter(spaces)

def getNewPosition(old_position, dice_sum_val):
    new_position=old_position+dice_sum_val
    return ((new_position-1)%10)+1
    
def playOneTurn(turn,currentPosition,currentScore,spaces):
    key = (currentPosition[0],currentPosition[1],currentScore[0],currentScore[1],turn)
    if currentScore[0]>=minScore:
        numberOfUniversToWin[key]=(1,0)
        return (1,0)
    if currentScore[1]>=minScore:
        numberOfUniversToWin[key]=(0,1)
        return (0,1)
    player1Wins=0
    player2Wins=0
    for universe in spaces:
        nr_universes=spaces[universe] #We use the fact here that there are 7 distinct universes 
        new_current_position=currentPosition.copy()
        new_current_position[turn]=getNewPosition(currentPosition[turn],universe)
        new_current_score=currentScore.copy()
        new_current_score[turn]=currentScore[turn]+new_current_position[turn]
        new_turn=1 if turn==0 else 0
        new_key=(new_current_position[0],new_current_position[1],new_current_score[0],new_current_score[1],new_turn)
        if new_key in numberOfUniversToWin:
            player1Wins+=nr_universes*numberOfUniversToWin[new_key][0]
            player2Wins+=nr_universes*numberOfUniversToWin[new_key][1]
        else:
            outcome=playOneTurn(new_turn,new_current_position,new_current_score,spaces)
            player1Wins+=nr_universes*outcome[0]
            player2Wins+=nr_universes*outcome[1]
    numberOfUniversToWin[key]=(player1Wins,player2Wins)
    return player1Wins,player2Wins
        
    

#Part 2
#For this part, with the Dirac Dice, since every roll of dice creates one univere,
#3 consecutives roles of dices create in total 27 universe. So there are 27 universes per turn and we will think in terms of turns.
#We use "dynamic programming" to solve this, i.e we store results and when having to compute something that is already computed, use it
#Another optimization is to see that we have 7 distinct spaces. We use this optimization to divide the runtime by ~3.5
numberOfUniversToWin=dict()#(currentPosition,currentScore,turn) -> (nrUniverse1Wins,nrUniverse2Wins)
spaces = generateSpaces()
minScore=21
print("Solution part 2:")
player1Wins,player2Wins = playOneTurn(0,currentPosition,[0,0],spaces)
print(max(player1Wins,player2Wins))


     
        

                
    


