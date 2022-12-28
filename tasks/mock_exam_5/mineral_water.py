number_small_bottles = int(input())
number_big_bottles = int(input())
capacity_of_truck = int(input())
litters_big_bottles = number_big_bottles * 5
total_warehouse_litters = litters_big_bottles + number_small_bottles
free_capacity_in_track = capacity_of_truck - total_warehouse_litters
free = capacity_of_truck - litters_big_bottles

if free_capacity_in_track > 0:
    print('-1')
elif total_warehouse_litters == capacity_of_truck:
    print(number_small_bottles)
else:
    if free >= 0:
        print(free)
    else:
        print('-1')

# PONTS = 77









