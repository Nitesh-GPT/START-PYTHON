'''import copy
list = [[1,3,4,5], [4,5,6,7]]
deep_copy = copy.deepcopy(list)
deep_copy[1][2] = (9)
print(deep_copy)
print(list)


this program without using the built-in Import, this is the manual way to do the deep copy of the object'''

list1 = [[1,2,3,4], [4,5,6,7]]
deepcpy = [ [item for item in sublist] for sublist in list1 ]
deepcpy[0][2] = (9)
print(list1)
print(deepcpy)

