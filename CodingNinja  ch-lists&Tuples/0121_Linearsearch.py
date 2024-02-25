def linear_search(li,ele):
    # Here li means list in this and ele means element...
    for i in range(len(li)):
        if li[i] == ele:
            return  i
    return -1

li = [1,2,3,6,5]
index = linear_search(li,5)
print(index)