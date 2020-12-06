def insertion_sort(A):
    for k in range(len(A)):
        cur = A[k]
        j = k
        while j>0 and A[j-1] > cur:
            A[j] = A[j-1]
            j -= 1
        A[j] = cur
A = [34, 11, 9, 0, 2, 44, 32]
insertion_sort(A)
print(A)