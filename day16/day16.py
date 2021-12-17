class Packet:
    def __init__(self, binary):
        self.version=BinaryToDecimal(binary[0:3])
        self.type_id=BinaryToDecimal(binary[3:6])
        self.bin=binary
        self.children=[]
        self.value=-1
        self.length=-1
        if self.type_id==4: #Literal
            #Process all the numbers
            numbers=[]
            startsWithOne=binary[6]=="1"
            firstTimeZero=not startsWithOne
            currentIndex=7
            while(startsWithOne or firstTimeZero):
                numbers.append(binary[currentIndex:currentIndex+4])
                if firstTimeZero: #We don't continue
                    currentIndex+=4
                    firstTimeZero=False
                else:
                    startsWithOne=binary[currentIndex+4]=="1"
                    firstTimeZero=not startsWithOne
                    currentIndex+=5
         
            self.length=currentIndex
            self.value = BinaryToDecimal("".join(numbers))
            
        else: #Operator
            length_type_id=binary[6]
            if length_type_id=="1":
                nr_subpackets=BinaryToDecimal(binary[7:7+11])
                currentIndex=7+11
                for i in range(nr_subpackets):
                    child=Packet(binary[currentIndex:])
                    currentIndex+=child.length
                    self.children.append(child)
                self.length=currentIndex
            else:
                length_subpackets=BinaryToDecimal(binary[7:7+15])
                currentIndex=7+15
                while currentIndex < length_subpackets+7+15:
                    child=Packet(binary[currentIndex:])
                    currentIndex+=child.length
                    self.children.append(child)
                self.length=currentIndex
            if self.type_id==0:
                self.value = sum(child.value for child in self.children)
            elif self.type_id==1:
                self.value=1
                for child in self.children:
                    self.value*=child.value
            elif self.type_id==2:
                self.value = min(child.value for child in self.children)
            elif self.type_id==3:
                self.value = max(child.value for child in self.children)
            elif self.type_id==5:
                self.value = 1 if self.children[0].value > self.children[1].value else 0
            elif self.type_id==6:
                self.value = 1 if self.children[0].value < self.children[1].value else 0  
            elif self.type_id==7:
                self.value = 1 if self.children[0].value == self.children[1].value else 0
                
    def sum_of_versions(self):
        return self.version+sum(child.sum_of_versions() for child in self.children) 
               
def hexToBinary(hex_char):
    return bin(int(hex_char, 16))[2:].zfill(4)

def BinaryToDecimal(n):
    return int(n,2)

line="9C0141080250320F1802104A08"
test=False
if __name__ == "__main__":
    if test:
        binary_repr=[hexToBinary(x) for x in line]
        binary_repr="".join(binary_repr)
    else:
        with open("input_day_16","r") as fp:
            line =fp.readline().strip()
            binary_repr = [hexToBinary(x) for x in line]
            binary_repr="".join(binary_repr)



packet = Packet(binary_repr)
#Part 1 
print("Solution part 1:")
print(packet.sum_of_versions())

#Part 2 
print("Solution part 2:") 
print(packet.value)    
                
    


