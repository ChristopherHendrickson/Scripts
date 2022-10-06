#Kth largest element

def kth(arr,k):
    return sorted(arr)[-k]


print(kth([1,5,3,6,6,4,7,8,4,3,2,78,45,3],4))