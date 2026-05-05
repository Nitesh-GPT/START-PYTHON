# "*" single star called “splat operator” or “unpacking operator” it used in values unpacking
value = [1,2,3,4]
def unpack(*args):
    return args
hello = unpack(*value)
print(hello)



'''def packing(*h):
    return h

yes = packing(*value)
print(yes)'''

numbers = [1,2,2,3,4,5]
print(*numbers)