if __name__ == "__main__":
    with open("input_day_7","r") as fp:
        crab_positions=[int(x) for x in fp.readline().split(",")]

#Part 1, very naive algorithm
biggest_position = max(crab_positions)
smallest_position= min(crab_positions)
min_fuel_used = float("inf")
for position in range(smallest_position, biggest_position+1):
    fuel_used = 0
    for crab in crab_positions:
        fuel_used+=abs(position-crab)
    if fuel_used<min_fuel_used:
        min_fuel_used=fuel_used
print("Solution part 1:")
print(min_fuel_used)


#Part 2, also naive algorithm
min_fuel_used_pt2 = float("inf")
for position in range(smallest_position, biggest_position+1):
    fuel_used = 0
    #Sum between 1 and n: n(n+1)/2
    for crab in crab_positions:
        n = abs(position-crab)
        fuel_used+= int(n*(n+1)/2)
    if fuel_used<min_fuel_used_pt2:
        min_fuel_used_pt2=fuel_used
print("Solution part 2:")
print(min_fuel_used_pt2)
