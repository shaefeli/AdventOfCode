def filter_with_new_bit(array_to_filter, current_bit_index, most_common=True):
    nr_ones= sum([int(x[current_bit_index]) for x in array_to_filter]) #Count number of ones at a certain index in array
    if nr_ones>=len(array_to_filter)-nr_ones: #1 is more common
       result_bit= "1" if most_common else "0"
    else: #0 is more common
        result_bit = "0" if most_common else "1"
    
    return list(filter(lambda x:x[current_bit_index]==result_bit,array_to_filter))

if __name__ == "__main__":
    with open("input_day_3","r") as fp:
        oxygen_gen_most = [line.strip() for line in fp.readlines()]
           
    scrubber_rate_least = oxygen_gen_most.copy()
    oxygen_val=-1
    scrubber_val=-1
    for i in range(len(oxygen_gen_most[0])):
        if oxygen_val==-1:
            oxygen_gen_most=filter_with_new_bit(oxygen_gen_most,i,most_common=True)
            if len(oxygen_gen_most)==1:
                oxygen_val=oxygen_gen_most[0]
           
        if scrubber_val==-1:
            scrubber_rate_least=filter_with_new_bit(scrubber_rate_least,i, most_common=False)
            if len(scrubber_rate_least)==1:
                scrubber_val=scrubber_rate_least[0]

    print("The result is:")      
    print(int(oxygen_val,2)*int(scrubber_val,2))   