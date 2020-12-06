def quicksort(array):
    if len(array) <2:
        return array
    else:
        pivot = array[0]
        less = [i for i in array[1:] if i<= pivot]
        greater = [i for i in array[1:] if i>pivot]
        return quicksort(less) + [pivot] + quicksort(greater)

def merge_sort(array):
    def merge(array, arr1, arr2):
        size1 = len(arr1)
        size2 = len(arr2)
        p1 = p2 = 0
        while p1<size1 and p2 < size2:
            
    def helper(array, l, r):
        if l>=r:
            return
        mid = (l+r)//2
        helper(array, l, mid)
        helper(array, mid+1, r)
        merge(array[l:mid+1], array[mid+1:r+1])
a = [3,2,1,5,3, 6, 7, 1]
print(quicksort(a))