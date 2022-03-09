map = input("Please enter a map")
moves = input("Please enter a movement")
mapList = map.split("], [")
mapList[0] = mapList[0][2:]
mapList[len(mapList)-1] = mapList[len(mapList)-1][:-2]
two_dimensional_array = []

for line in mapList:

    temp_line = line.replace("'", "")
    list = temp_line.split(",")
    two_dimensional_array.append(list)

row = 0
for i in two_dimensional_array:
    line = 0
    for j in i:
        two_dimensional_array[row][line] = j.replace(" ", "")
        line+=1
    row+=1

def printBoard():
    for i in two_dimensional_array:
        print(" ".join(i))

print("Your board is:")
printBoard()

moves = moves[1:-1]
moves = moves.replace("'", "")
moves = moves.replace(" ","")
moveList = moves.split(",")

rabbit_row = -1
for i in two_dimensional_array :
    rabbit_row += 1
    for j in i :
        if j == "*":
            rabbit_line = i.index(j)

point = 0
for i in moveList:
    if i == "U":
        if rabbit_row -1 < 0:
            pass
        elif two_dimensional_array[rabbit_row-1][rabbit_line] == "W":
            pass
        elif two_dimensional_array[rabbit_row - 1][rabbit_line] == "P":
            two_dimensional_array[rabbit_row - 1][rabbit_line] = "*"
            two_dimensional_array[rabbit_row][rabbit_line] = "X"
            print("rabbit is dead")
            break
        else:
            if two_dimensional_array[rabbit_row-1][rabbit_line] == "A":
                point += 5
            elif two_dimensional_array[rabbit_row-1][rabbit_line] == "C":
                point += 10
            elif two_dimensional_array[rabbit_row-1][rabbit_line] == "M":
                point -=5
            two_dimensional_array[rabbit_row-1][rabbit_line] = "*"
            two_dimensional_array[rabbit_row][rabbit_line] = "X"
            rabbit_row = rabbit_row-1

    elif i == "R":
        if rabbit_line +1 > line-1 :
            pass
        elif two_dimensional_array[rabbit_row][rabbit_line+1] == "W":
            pass
        elif two_dimensional_array[rabbit_row][rabbit_line+1] == "P":
            two_dimensional_array[rabbit_row][rabbit_line + 1] = "*"
            two_dimensional_array[rabbit_row][rabbit_line] = "X"
            print("rabbit is dead")
            break
        else:
            if two_dimensional_array[rabbit_row][rabbit_line+1] == "A":
                point += 5
            elif two_dimensional_array[rabbit_row][rabbit_line+1] == "C":
                point += 10
            elif two_dimensional_array[rabbit_row][rabbit_line+1] == "M":
                point -=5
            two_dimensional_array[rabbit_row][rabbit_line+1] = "*"
            two_dimensional_array[rabbit_row][rabbit_line] = "X"
            rabbit_line = rabbit_line+1

    elif i == "D":
        if rabbit_row+1 > row-1 :
            pass
        elif two_dimensional_array[rabbit_row+1][rabbit_line] == "W":
            pass
        elif two_dimensional_array[rabbit_row + 1][rabbit_line] == "P":
            print("rabbit is dead")
            two_dimensional_array[rabbit_row + 1][rabbit_line] = "*"
            two_dimensional_array[rabbit_row][rabbit_line] = "X"
            break
        else:
            if two_dimensional_array[rabbit_row+1][rabbit_line] == "A":
                point += 5
            elif two_dimensional_array[rabbit_row+1][rabbit_line] == "C":
                point += 10
            elif two_dimensional_array[rabbit_row+1][rabbit_line] == "M":
                point -=5
            two_dimensional_array[rabbit_row+1][rabbit_line] = "*"
            two_dimensional_array[rabbit_row][rabbit_line] = "X"
            rabbit_row = rabbit_row+1

    elif i == "L":
        if rabbit_line-1 < 0:
            pass
        elif two_dimensional_array[rabbit_row][rabbit_line-1] == "W":
            pass
        elif two_dimensional_array[rabbit_row][rabbit_line - 1] == "P":
            two_dimensional_array[rabbit_row][rabbit_line - 1] = "*"
            two_dimensional_array[rabbit_row][rabbit_line] = "X"
            print("rabbit is dead")
            break
        else:
            if two_dimensional_array[rabbit_row][rabbit_line-1] == "A":
                point += 5
            elif two_dimensional_array[rabbit_row][rabbit_line-1] == "C":
                point += 10
            elif two_dimensional_array[rabbit_row][rabbit_line-1] == "M":
                point -=5
            two_dimensional_array[rabbit_row][rabbit_line-1] = "*"
            two_dimensional_array[rabbit_row][rabbit_line] = "X"
            rabbit_line = rabbit_line -1
print("\nYour output should be like this:")
printBoard()
print("Your score is:",point)