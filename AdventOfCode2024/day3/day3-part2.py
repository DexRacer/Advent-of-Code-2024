import fileinput
import re

input2 = "xmul(2,4)&mul[3,7]!^don't()_mul(5,5)+mul(32,64](mul(11,8)undo()?mul(8,5))"
result = 0

with open("E:\AdventOfCode2024\day3\day3-input.txt") as file:
    input = file.read()
    
dontSplit = re.split("don't()", input)
x = re.findall("mul\(([0-9]{1,3}),([0-9]{1,3})\)", dontSplit[0])
for i in range(len(x)): 
    result += int(x[i][0]) * int(x[i][1])
    
for don in range(len(dontSplit)):
    doSplit = re.split("do()",dontSplit[don])
    for index in range(1,len(doSplit)):
        x = re.findall("mul\(([0-9]{1,3}),([0-9]{1,3})\)", doSplit[index])
        if not x:
            continue
        else:
            for i in range(len(x)):
                result += int(x[i][0]) * int(x[i][1])
print(result)