import queue

#############################
#COMMON CODE FOR PART 1 AND 2
#############################
def is_opposite(opening,closing):
    return closing==return_opposite(opening)
        
def return_opposite(opening):
    if opening=="(":
        return ")"
    elif opening=="{":
        return "}"
    elif opening=="[":
        return "]"
    elif opening=="<":
        return ">"  

#############################    
#FOR PART 1
#############################
def get_value_pt1(char):
    if char==">":
        return 25137
    elif char=="}":
        return 1197
    elif char=="]":
        return 57
    elif char==")":
        return 3
                
def checkLine(line):
    checkQueue = queue.LifoQueue()
    for char in line:
        if char=="<" or char=="[" or char=="(" or char=="{":
            checkQueue.put(char)
        else:
            toClose=checkQueue.get()
            if not is_opposite(toClose,char):
                return get_value_pt1(char)
    return 0            

#############################
#FOR PART 2
#############################       
def get_value_pt2(char):
    if char==")":
        return 1
    elif char=="]":
        return 2
    elif char=="}":
        return 3
    elif char==">":
        return 4

def find_rest_open(line):
    currentQueue = queue.LifoQueue()
    for char in line:
        if char=="<" or char=="[" or char=="(" or char=="{":
            currentQueue.put(char)
        else:
            toClose=currentQueue.get()
            if not is_opposite(toClose,char): #Reput in the queue
                currentQueue.put(char)
    return currentQueue         
 
def create_closings(openings_queue):
    closingString=""
    while not openings_queue.empty():
        charToClose=openings_queue.get()
        closingString+=return_opposite(charToClose)
    return closingString
        
 
#############################
###MAIN CODE
############################# 
if __name__ == "__main__":
    with open("input_day_10","r") as fp:
        lines=[]
        for line in fp.readlines():
            lines.append([x for x in line.strip()]) 
            
#Part 1
print("Solution part 1")
print(sum([checkLine(line) for line in lines]))

#Part 2
totals=[]
for line in lines:
    total=0
    if checkLine(line)==0:
        closingString = create_closings(find_rest_open(line))
        for char in closingString:
            total=total*5 + get_value_pt2(char)
        totals.append(total)
        
print("Solution part 2:")
print(sorted(totals)[int(len(totals)/2)])

        



