'''import copy
# shallow copy makes a new object, but inside it still points to the same inner stuff.
shallow = [[1,2,3], [2,3,4]]
shallow_copy = copy.copy(shallow)
shallow_copy[0][0] = 9
print("original", shallow)
print(shallow_copy)'''


#this program without using any built-in import

original = [[1,2,3], [2,4,5]]
shallow_copy = original[ : ]
shallow_copy[0][1] = [5]
print(shallow_copy)