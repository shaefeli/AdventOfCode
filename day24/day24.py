class Operation:
    def __init__(self,line,w=0,x=0,y=0,z=0):
        self.x=x
        self.w=w
        self.y=y
        self.z=z
        op_parts = line.split(" ")
        self.operand = op_parts[0]
        self.arg1 = op_parts[1]
        self.arg2 = op_parts[2].strip()

    def set_variables(self,w,x,y,z):
        self.w=w
        self.x=x
        self.y=y   
        self.z=z

    def get_op_result(self):
        if self.operand=="mul":
            return self.format_result(self.arg1,self.str_to_var(self.arg1)*self.str_to_var(self.arg2))
        elif self.operand=="add":
            return self.format_result(self.arg1,self.str_to_var(self.arg1)+self.str_to_var(self.arg2))
        elif self.operand=="div":
            return self.format_result(self.arg1,self.str_to_var(self.arg1)//self.str_to_var(self.arg2))
        elif self.operand=="mod":
            return self.format_result(self.arg1,self.str_to_var(self.arg1)%self.str_to_var(self.arg2))
        elif self.operand=="eql":
            return self.format_result(self.arg1,1 if self.str_to_var(self.arg1)==self.str_to_var(self.arg2) else 0)

    def format_result(self,arg,value):
        if arg=="w":
            return value,self.x,self.y,self.z
        elif arg=="x":
            return self.w,value,self.y,self.z
        elif arg=="y":
            return self.w,self.x,value,self.z
        elif arg=="z":
            return self.w,self.x,self.y,value

    def str_to_var(self,arg):
        if arg=="x":
            return self.x
        elif arg=="w":
            return self.w
        elif arg=="y":
            return self.y
        elif arg=="z":
            return self.z
        else:
            return int(arg)

def execute_operations_one_block(op_block,w,x,y,z):
    op_block[0].set_variables(w,x,y,z)
    new_w,new_x,new_y,new_z=op_block[0].get_op_result()
    for i in range(1,len(op_block)):
        op_block[i].set_variables(new_w,new_x,new_y,new_z)
        new_w,new_x,new_y,new_z=op_block[i].get_op_result()
    return new_x,new_y,new_z

def execute_alu(operations,w_array):
    new_x,new_y,new_z=0,0,0
    for i in range(len(w_array)):
        new_x,new_y,new_z=execute_operations_one_block(operations[i],w_array[i],new_x,new_y,new_z)
    return new_z
    


operations=[] #2d array, 13xY, 13 is the size of the input, Y the number of operations done per number
with open("input_day_24","r") as fp:
    lines = fp.readlines()
    current_operation=[]
    for i,line in enumerate(lines):
        if line.startswith("inp"):
            if i!=0:
                operations.append(current_operation)
                current_operation=[]
        else:
            current_operation.append(Operation(line))
    operations.append(current_operation)

nr_ops=14
z_upper_bound=100000
possibilities=set([(0,0,0)])
poss=set() #(turn,w,res_x,res_y,res_z,inp_x,inp_y,inp_z)
for i in range(nr_ops):
    print(i)
    new_possibilities=set()
    for w in range(1,10):
        for x,y,z in possibilities:
            next_x,next_y,next_z = execute_operations_one_block(operations[i],w,x,y,z)
            if next_z<z_upper_bound: #In theory here it would be 26**(14-i-1), but let's try with something smaller, because there is a high probability that it is so
                new_possibilities.add((next_x,next_y,next_z))
                poss.add((i,w,next_x,next_y,next_z,x,y,z))
    possibilities=set(new_possibilities)

print("Total number of possibilities (when z is staying under",str(z_upper_bound),"):",str(len(possibilities)))

poss_per_turn=dict()
for i in range(nr_ops):
    for a in poss:
        if a[0]==i:
            if i in poss_per_turn:
                poss_per_turn[i].append((a[1],a[2],a[3],a[4],a[5],a[6],a[7]))
            else:
                poss_per_turn[i] = [(a[1],a[2],a[3],a[4],a[5],a[6],a[7])]

#Take only the possibilities per turn that will lead to a z=0 after the last op
valid_poss_per_turn=dict()
valid_last=[a for a in poss_per_turn[nr_ops-1] if a[3]==0]
for val in valid_last:
    if nr_ops-1 in valid_poss_per_turn:
        valid_poss_per_turn[nr_ops-1].append(val)
    else:
        valid_poss_per_turn[nr_ops-1] = [val]

for i in range(nr_ops-2,-1,-1):
    for val in poss_per_turn[i]:
        for val_last in valid_last:
            if val[1]==val_last[4] and val[2]==val_last[5] and val[3]==val_last[6]:
                if i in valid_poss_per_turn:
                    valid_poss_per_turn[i].append(val)
                else:
                    valid_poss_per_turn[i] = [val]
                break
    valid_last=valid_poss_per_turn[i]

#Part 1:
numbers=[]
for i in range(nr_ops):
    numbers.append(str(max([a[0] for a in valid_poss_per_turn[i]])))
print("Solution part 1:")
print("".join(numbers))

#Part 2:
numbers=[]
for i in range(nr_ops):
    numbers.append(str(min([a[0] for a in valid_poss_per_turn[i]])))
print("Solution part 2:")
print("".join(numbers))





