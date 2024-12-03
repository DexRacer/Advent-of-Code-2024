import fileinput

filename = "E:\AdventOfCode2024\day1\day1-input.txt"
input = []
list1 = []
list2 = []
total = 0
for line in fileinput.input(files=filename):
    input.append(line)
    

for i in range(len(input)):
    compare =input[i].split(" ")
    
    list1.append(int(compare[0]))
    list2.append(int(compare[3].rstrip()))
    
for i in range(len(list1)):
    amount = list2.count(list1[i])
    simScore = amount * list1[i]
    total += simScore

print(total)