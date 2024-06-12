from random import randint

map = []
lines = 100
height = 5

for i in range(lines):
    map.append([])
    for j in range(height):
        if j == 0:
            map[i].append(1)
        else:
            x = randint(0,1)
            if map[i][j-1] == 1:
                map[i].append(randint(0,1))
            else:
                map[i].append(0)

for j in range(height):
    for i in range(lines):
        item = map[i][height - 1 - j]
        if item == 1:
            print("#",end="")
        elif item == 0:
            print(" ",end="")
        # print(map[i][height-1-j], end="")
    print()