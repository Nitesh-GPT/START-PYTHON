def in_list(L, e):
    if len(L) == 1:
        return L[0] == e
    else:
        if L[0] == 0:
            return True
        else:
            return in_list(L[1:], e)
            #this return fucntion will be called again with new value and again all condition will be checked.
value = in_list([2,4,5,6], [7])
print(value)

