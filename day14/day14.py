insertion_rules=dict()
if __name__ == "__main__":
    with open("input_day_14","r") as fp:
        for i,line in enumerate(fp.readlines()):
            if i==0:
                template=line.strip()
            if i>=2:
                two_parts = line.strip().split(" -> ")
                insertion_rules[two_parts[0]]=two_parts[1]


def increment_dict(dict_to_inc,key,count):
    if key in dict_to_inc:
        dict_to_inc[key]+=count
    else:
        dict_to_inc[key]=count
    return dict_to_inc
        
def update_pairs_dict(pairs_dict, rules):
    new_dict=dict()
    for pair,count in pairs_dict.items():
        if count==0:
            if pair not in new_dict:
                new_dict[pair]=0
        else:
            toInsert = rules[pair]
            new_pair1 = pair[0]+toInsert
            new_pair2 = toInsert+pair[1]
            new_dict=increment_dict(new_dict,new_pair1,count)
            new_dict=increment_dict(new_dict,new_pair2,count)
    return new_dict

def getCounts(template, insertion_rules, steps):
    #Prefill the pairs count dict that will count the number of pairs
    pairs_count=dict()
    for pair,toInsert in insertion_rules.items():
        pairs_count[pair]=0
    for i in range(0,len(template)-1):
        pair=template[i:i+2]
        pairs_count[pair]+=1
    
    #Update the pairs count    
    for step in range(steps):
        pairs_count=update_pairs_dict(pairs_count,insertion_rules)
        
    #Count the occurences of each letter (note that we need to dedouble from pairs)
    counts_with_double=dict()
    for pair, count in pairs_count.items():
        counts_with_double=increment_dict(counts_with_double,pair[0],count)
        counts_with_double=increment_dict(counts_with_double,pair[1],count)
    counts=dict()
    for letter,count in counts_with_double.items():
        if letter==template[0] or letter==template[-1]:
            counts[letter]=int(1+(counts_with_double[letter]-1)/2)
        else:
            counts[letter]=int(counts_with_double[letter]/2)
            
    count_vals_in_order=sorted(counts.values())
    return count_vals_in_order[-1]-count_vals_in_order[0]
   
#A naive approach cannot work because of the growing number of pairs to process (exponentially)
#You cannot do a single operation per newly created pair
#This approach consists of counting the number of pairs of each type that will be created
#At the end, the letter occurences can be computed from these   
#Part 1 
print("Solution part 1:")
print(getCounts(template,insertion_rules,10))

#Part 2
print("Solution part 2:")
print(getCounts(template,insertion_rules,40))