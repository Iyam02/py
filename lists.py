#empty list
my_list = []

#Adding items to my_list
my_list.append(10)
my_list.append(20)
my_list.append(30)
my_list.append(40)
print('my_list after appending items: ', my_list)

#inserting 15 at index 1
my_list.insert(1, 15)
print("After inserting value 15 at index 1: ", my_list)

#extending the list
my_list.extend([50,60,70])
print("After extending the list: ", my_list)

#removing last item
my_list.pop(-1)
print('After removing the last item: ', my_list)

#sorting in ascending order
print('After sorting in ASC order: ', my_list)
my_list.sort()

#printing the index of the value 30
print(my_list.index(30))