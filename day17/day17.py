if __name__ == "__main__":
    input_day_17= "target area: x=217..240, y=-126..-69"
    target_x=(217,240)
    target_y=(-126,-69)

def Vx_next(Vx):
    if Vx<0: return Vx+1
    elif Vx>0: return Vx-1
    else: return Vx
def Vy_next(Vy):
    return Vy-1

                                        
#Part 1 and 2
#Very dirty and slow solution
#The x boundaries are estimated with common sense
#The y top boundary is given after knowing the part1 solution max vy...
#This solution only works because we can check our solution
highestY=0
countIsIn=0
for vx in range(0,250):
    if vx%20==0:
        print("Percentage handled:",int(vx/250*100),"%")
    for vy in range(-126,126):
        passedOrIn=False
        current_highestY=0
        current_vx=vx
        current_vy=vy
        X=0
        Y=0
        while(not passedOrIn):
            X+=current_vx
            Y+=current_vy
            current_vx=Vx_next(current_vx)
            current_vy=Vy_next(current_vy)
            if Y>current_highestY:
                current_highestY=Y
            isIn = X>=target_x[0] and X<=target_x[1] and Y>=target_y[0] and Y<=target_y[1]
            hasPassed = Y<target_y[0]
            passedOrIn=isIn or hasPassed
            if isIn:
                countIsIn+=1
                if current_highestY>highestY:
                    highestY=current_highestY
                    
print("Solution part 1:")
print(highestY)

print("Solution part 2:") 
print(countIsIn)  
                
    


