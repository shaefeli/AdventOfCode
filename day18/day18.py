#We do it the "hard" way by not using objects, doing the explosions and the splittings directly in the string
#A lot of play with the indexes had to be done.

#Knowing the first index where a number starts (left most digit of the number), find the complete number starting at startIndex.
def getNumberRight(searchArray,startIndex):
    number=searchArray[startIndex]
    searchIndex=startIndex+1
    while(searchArray[searchIndex].isnumeric()):
        number+=searchArray[searchIndex]
        searchIndex+=1
    return number

#Knowing the first index where a number ends (right most digit of the number), find the complete number ending at startIndex.
def getNumberLeft(searchArray,startIndex):
    number=searchArray[startIndex]
    searchIndex=startIndex-1
    while(searchArray[searchIndex].isnumeric()):
        number=searchArray[searchIndex]+number
        searchIndex-=1
    return number
        
#Check if we have a regular pair    
def isPair(potential_pair_array):
    potential_pair_string = "".join(potential_pair_array)
    if "," not in potential_pair_string: return False
    nr_1=potential_pair_string.split(",")[0]
    nr_2=potential_pair_string.split(",")[1][0] #We might have more than 1 number, checking if first is number is enough
    return nr_1.isnumeric() and nr_2.isnumeric()

#To use only after using isPair on the text, get the text
def getPair(potential_pair_array):
    potential_pair_string = "".join(potential_pair_array)
    nr_1=potential_pair_string.split(",")[0]
    second_part=potential_pair_string.split(",")[1]
    nr_2=getNumberRight(second_part,0)
    return nr_1,nr_2

#Do the splitting in place
#numberToReduceOriginal is an array (convert string to array)
def doSplitting(numberToReduceOriginal):
    numberToReduce=numberToReduceOriginal.copy()
    currentIndex=0
    while(currentIndex<len(numberToReduce)):
        if numberToReduce[currentIndex].isnumeric():  
            #Check what number is there (can be more than 1 digit)
            number = getNumberRight(numberToReduce,currentIndex)
            if int(number)>=10: #If formed number bigger than 10, split
                new_pair="["+str(int(int(number)/2))+","+str(int((int(number)+1)/2))+"]"
                del numberToReduce[currentIndex:currentIndex+len(number)]
                for i,char in enumerate(new_pair):
                    numberToReduce.insert(currentIndex+i,char)
                return numberToReduce
        currentIndex+=1
    return numberToReduce
   
#Do the explosion in place   
def doExplosion(numberToReduceOriginal):
    numberToReduce=numberToReduceOriginal.copy()
    nrOpeningPair=0
    currentIndex=0
    while(currentIndex<len(numberToReduce)):
        if numberToReduce[currentIndex]=="[":
            nrOpeningPair+=1
        elif numberToReduce[currentIndex]=="]":
            nrOpeningPair-=1
        elif numberToReduce[currentIndex].isnumeric():                    
            if nrOpeningPair==5 and isPair(numberToReduce[currentIndex:]): 
                nr_1,nr_2=getPair(numberToReduce[currentIndex:])
                #Merge to the right
                right_index_nr2=currentIndex+len(nr_1)+len(nr_2)
                searchIndex_right=right_index_nr2+1
                firstNumericIndex_right=-1
                while(firstNumericIndex_right==-1 and searchIndex_right<len(numberToReduce)):
                    if numberToReduce[searchIndex_right].isnumeric():
                        firstNumericIndex_right=searchIndex_right
                    searchIndex_right+=1
                if firstNumericIndex_right!=-1:
                   nr_to_merge_with=getNumberRight(numberToReduce,firstNumericIndex_right)
                   new_nr=str(int(nr_to_merge_with)+int(nr_2))
                   del numberToReduce[firstNumericIndex_right:firstNumericIndex_right+len(nr_to_merge_with)]
                   for i,digit in enumerate(new_nr):
                        numberToReduce.insert(firstNumericIndex_right+i,digit)
                #Replace pair with 0
                del numberToReduce[currentIndex-1:right_index_nr2+2] #Delete with brackets
                currentIndex-=1 #Because we are at the place of the first bracket
                numberToReduce.insert(currentIndex,"0")
                
                #Merge to the left (Numbers to the left can be greater than 10 also)
                firstNumericIndex_left=-1
                searchIndex_left=currentIndex-1
                while(firstNumericIndex_left==-1 and searchIndex_left>=0):
                    if numberToReduce[searchIndex_left].isnumeric():
                        firstNumericIndex_left=searchIndex_left
                    searchIndex_left-=1
                if firstNumericIndex_left!=-1:
                   nr_to_merge_with=getNumberLeft(numberToReduce,firstNumericIndex_left)
                   new_nr=str(int(nr_to_merge_with)+int(nr_1))
                   del numberToReduce[firstNumericIndex_left-len(nr_to_merge_with)+1:firstNumericIndex_left+1]
                   for i,digit in enumerate(new_nr):
                        numberToReduce.insert(firstNumericIndex_left-len(nr_to_merge_with)+1+i,digit)
                return numberToReduce
        currentIndex+=1
    return numberToReduce
 
#One reduction step 
def reduceNumberOneStep(numberToReduceOriginal):
    reduceAfterExplosion=doExplosion(numberToReduceOriginal)
    if reduceAfterExplosion==numberToReduceOriginal:
        reduceAfterSplit=doSplitting(numberToReduceOriginal)
        return reduceAfterSplit
    return reduceAfterExplosion
       
#Reduce a whole number       
def reduceNumber(number):
    reducingFinished=False
    before_reduced=number.copy()
    reduced=[]
    while(not reducingFinished):
        reduced=reduceNumberOneStep(before_reduced)
        if reduced==before_reduced:
            reducingFinished=True
        before_reduced=reduced
    return reduced

def addTwoNumbers(nr1_str,nr2_str):
    new_nr_str="["+nr1_str+","+nr2_str+"]"
    return "".join(reduceNumber([x for x in new_nr_str]))
    

def addList(nr_list):
    currentReducedNr = nr_list[0]
    for i in range(1,len(nr_list)):
        currentReducedNr=addTwoNumbers(currentReducedNr,nr_list[i])
    return currentReducedNr

#An inplace method that looks through the string
def getMagnitude(number_str):
    number_arr=[x for x in number_str]
    nrOpeningPair=0
    for depth in range(4,0,-1):
        currentIndex=0
        while(currentIndex<len(number_arr)):
            if number_arr[currentIndex]=="[":
                nrOpeningPair+=1
                if nrOpeningPair==depth:
                    nr_1=getNumberRight(number_arr,currentIndex+1)
                    nr_2=getNumberRight(number_arr,currentIndex+1+len(nr_1)+1)
                    result=str(3*int(nr_1)+2*int(nr_2))
                    del number_arr[currentIndex:currentIndex+len(nr_1)+1+len(nr_2)+2]
                    for i, digit in enumerate(result):
                        number_arr.insert(currentIndex+i,digit)
                    nrOpeningPair-=1
            elif number_arr[currentIndex]=="]":
                nrOpeningPair-=1
            currentIndex+=1
            
    return "".join(number_arr)            
            
    
if __name__ == "__main__":
    with open("input_day_18","r") as fp:
        nr_list=[x.strip() for x in fp.readlines()]
        

#Part 1
print("Solution part 1:")
print(getMagnitude(addList(nr_list)))

#Part 2
largestMagnitude=-1
for i in range(len(nr_list)):
    for j in range(i+1,len(nr_list)):
        magnitude1 = int(getMagnitude(addList([nr_list[i],nr_list[j]])))
        magnitude2 = int(getMagnitude(addList([nr_list[j],nr_list[i]])))
        max_magnitude=max(magnitude1,magnitude2)
        if max_magnitude>largestMagnitude:
            largestMagnitude=max_magnitude
print("Solution part 2:")
print(largestMagnitude)
        
        

                
    


