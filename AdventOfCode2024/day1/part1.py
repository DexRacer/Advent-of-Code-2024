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
    
list1.sort()
list2.sort()

for i in range(len(list1)):
    diference = abs(list2[i] - list1[i])
    total += diference
print(total)

    