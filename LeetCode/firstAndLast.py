#First and last index in array
#Returns the indeces of the first and last occureance of a target value in an array
def firstAndLast(arr,target):
    if target not in arr:
        return [-1,-1]
    
    first = arr.index(target)
    last = len(arr)-arr[::-1].index(target)-1
    return [first,last]


print(firstAndLast([1,2,2,2,3,3,3,3,3,3,4,4,4,5],3))

    