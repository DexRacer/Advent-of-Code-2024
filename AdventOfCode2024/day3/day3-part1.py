import fileinput
import re
filename = "E:\AdventOfCode2024\day3\day3-input.txt"
input = []
result = 0
for line in fileinput.input(files=filename):
    input.append(line)
    
for i in range(len(input)):
    x = re.findall("mul\(([0-9]{1,3}),([0-9]{1,3})\)", input[i])
    for index in range(len(x)):
        result += int(x[index][0]) * int(x[index][1])
print(result)