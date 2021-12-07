def read_input():
    f = open('inputs/input 7.txt', 'r')
    return [int(x) for x in f.read().split(',')]


crabs = read_input()
minimum = 0
fuel = -1
potential_fuel = 0

for opt in range(min(crabs), max(crabs)):
    potential_fuel = sum([abs(x - opt)*(abs(x - opt) + 1)/2 for x in crabs])
    if potential_fuel < fuel or fuel == -1:
        minimum = opt
        fuel = potential_fuel

print(fuel)
