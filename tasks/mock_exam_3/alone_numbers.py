# array = [int(el) for el in input().split(', ')]
# target_num = int(input())
# for i in range(len(array)):
#     if array[i] == target_num:
#         index_el = i
#         last_index = len(array) - 1
#         if index_el == 0 or index_el == last_index:
#             continue
#         else:
#             index_el_first = array[index_el - 1]
#             index_el_second = array[index_el + 1]
#             biggest_num = max(index_el_first, index_el_second)
#             if target_num == biggest_num:
#                 continue
#             else:
#                 if index_el_first == index_el_second:
#                     array.pop(index_el)
#                     array.insert(index_el, index_el_second)
#                 if index_el_first > index_el_second:
#                     array.pop(index_el)
#                     array.insert(index_el, index_el_first)
#                 elif index_el_first < index_el_second:
#                     array.pop(index_el)
#                     array.insert(index_el, index_el_second)
#                 else:
#                     array.pop(index_el)
#                     array.insert(index_el, index_el_second)
# print(array)


# POINTS = 77

array = [int(el) for el in input().split(', ')]
target_num = int(input())
bigger_num = 0
for index, el in enumerate(array):
    if el == target_num and index != 0 and index != len(array) - 1:
        index_num = array.index(el)
        if array[index_num - 1] > array[index_num + 1] and array[index_num - 1] != target_num:
            bigger_num = array[index_num - 1]
        elif array[index_num - 1] == array[index_num + 1] and array[index_num + 1] != target_num:
            bigger_num = array[index_num + 1]
        elif array[index_num - 1] < array[index_num + 1]:
            bigger_num = array[index_num + 1]
        array.pop(index)
        array.insert(index, bigger_num)
print(array)

#
#
# POINTS = 77