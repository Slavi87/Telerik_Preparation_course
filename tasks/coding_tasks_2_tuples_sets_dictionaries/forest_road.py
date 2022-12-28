width = int(input())
for i in range(width):
    road = ['.'] * width
    index = i
    road.insert(index, '*')
    road.pop()
    print(*road, sep='')
for j in range(width - 1, 0, -1):
    road_2 = ['.'] * width
    index = j - 1
    road_2.insert(index, '*')
    road_2.pop()
    print(*road_2, sep='')

