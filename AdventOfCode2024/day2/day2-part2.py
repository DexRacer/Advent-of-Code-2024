import fileinput

filename = "E:\AdventOfCode2024\day2\day2-input.txt"
input = []
input2 =["7 6 4 2 1", "1 2 7 8 9", "9 7 6 2 1", "1 3 2 4 5","8 6 4 4 1" ,"1 3 6 7 9"]
safe = 0
safe2 = 0
for line in fileinput.input(files=filename):
    input.append(line)
def acend(list):
    for i in range(len(list)-1):
        if int(list[i]) - int(list[i+1]) >= 0 or int(list[i]) - int(list[i+1]) < -3:     
            return False
    return True

def decend(list):
    for i in range(len(list)-1):
        if int(list[i]) - int(list[i+1]) <= 0 or int(list[i]) - int(list[i+1]) > 3:
            return False
    return True

for i in range(len(input)):
    report = (input[i]).strip().split(" ")
    
    print(report ,(acend(report) or decend(report)))
    #part1

    if acend(report) or decend(report): 
            safe+=1
    #part2
    for i in range(len(report)):
        print(i, len(report))
        holeList = list(report)
        print(holeList)
        print("holeList")
        holeList.pop(i)
        print(report)
        if acend(holeList) or decend(holeList):
            safe2+=1
            break
        #temlist.insert(i, report)

print(safe2)
print(acend([2, 4, 6, 8, 9, 9]))
print(acend([1, 2]))
print(acend(['69', '71', '74', '75', '77', '80']))