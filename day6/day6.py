def add_to_dict(fishs_summary,fish,nr_incr):    
    if fish in fishs_summary:
        fishs_summary[fish]+=nr_incr
    else:
        fishs_summary[fish]=nr_incr
        
#Note that a naive approach is not doable with growing size of fishs
#This is thus an optimized version in terms of space (constant and small space)
def compute_nr_fishs(fishs,nr_turns):
    #Create a dict that counts the number of fishs per state
    fishs_summary = dict()
    for fish in fishs:
        add_to_dict(fishs_summary,fish,1) 
        
    for turn in range(nr_turns):
        new_fish_summary=dict()
        for fish,nr_fish in fishs_summary.items():
            if fish>0:
                add_to_dict(new_fish_summary,fish-1,nr_fish)
            else:
                add_to_dict(new_fish_summary,6,nr_fish)
                add_to_dict(new_fish_summary,8,nr_fish)
        fishs_summary=new_fish_summary.copy()
            
    return sum(list(fishs_summary.values()))


if __name__ == "__main__":
    with open("input_day_6","r") as fp:
        fishs=[int(x) for x in fp.readline().split(",")]
      
#Part 1      
print("Solution part 1:")
print(compute_nr_fishs(fishs,80))

#Part 2
print("Solution part 2:")
print(compute_nr_fishs(fishs,256))

