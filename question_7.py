list1 = [15,17,19,21,23,25,27,29,31,33,35,37,39,41,43,45,47,49,51]
list2 = [1,9,17,25,33,41,49,57,65,73]
list3 = []
for number in list1:
    if number in list2 and number not in list3:
        list3.append(number)

print("Numbers in the intersection of the two lists are: \n ", list3)
