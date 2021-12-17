class Display:
    def __init__(self, digits_input, digits_output):
        self.digits_input=digits_input
        self.digits_output=digits_output
        
        #For ease, we numerote and refer as follows:
        #-1-
        #2 3
        #-4-
        #5 6
        #-7-
        #By taking the 4 unique length numbers, we can deduce these branches
        self.extract_clues(digits_input)
        
        self.result = self.classify_output(digits_output)
        
    def extract_clues(self,digits):
        one_nr = [x for x in digits if len(x)==2][0]
        four_nr = [x for x in digits if len(x)==4][0]
        seven_nr = [x for x in digits if len(x)==3][0]
        eight_nr = [x for x in digits if len(x)==7][0]  
        #The four following attributes correspond to branches folowing the numerotation
        #Note that only the branch one can be fully known, all others we only know pairs
        self.one = [x for x in seven_nr if x not in one_nr]    
        self.two_and_four = [x for x in four_nr if x not in one_nr]
        self.three_and_six = [x for x in one_nr]
        self.five_and_seven = [x for x in eight_nr if x not in four_nr]
        self.five_and_seven.remove(self.one[0])
    
    def get_result(self):
        return self.result
        
    def classify_output(self,digits):
        number_str = ""
        for digit in digits:
            number_str += str(self.classify_number(digit))
        return int(number_str)
        
    def classify_number(self,digit): #These rules can easily be deduced on a paper
        if len(digit)==2:
            return 1
        elif len(digit)==4:
            return 4
        elif len(digit)==3:
            return 7
        elif len(digit)==7:
            return 8
        else:
            if len(digit)==6: #Can be a 0, 6 or 9
                if all(elem in digit for elem in self.five_and_seven):
                    if all(elem in digit for elem in self.two_and_four):
                        return 6
                    else:
                        return 0
                else:
                    return 9
            else: #Can be a 2, 3 or 5
                if all(elem in digit for elem in self.five_and_seven):
                    return 2
                else:
                    if all(elem in digit for elem in self.two_and_four):
                        return 5
                    else:
                        return 3
                
                
if __name__ == "__main__":
    with open("input_day_8","r") as fp:
        digits=[(([x.strip() for x in line.split(" | ")[0].split(" ")],[y.strip() for y in line.split(" | ")[1].split(" ")])) for line in fp.readlines()]
            
#Part 1
#1,4,7 and 8 use a unique number of segments
#1: 2, 4:4, 7:3, 8:7
unique_nr_segments=[2,3,4,7]
print("Solution part 1")
print(sum([len(list(filter(lambda x: len(x) in unique_nr_segments, digit[1]))) for digit in digits]))

#Part 2
print("Solution part 2:")
print(sum([Display(line[0],line[1]).get_result() for line in digits]))


