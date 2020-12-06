import os


def disk_usage(path):
    ''' Return the number of bytes used by a file/folder and any descendents '''
    total = os.path.getsize(path)
    if os.path.isdir(path):
        for filename in os.listdir(path):
            child_path = os.path.join(path, filename)
            total += disk_usage(child_path)
    print(f'usage: {total}')
    return total

def binary_search_iterative(data, target):
    ''' Return True if target is found in the given Python list'''
    low = 0
    high = len(data) -1
    while low <= high:
        mid = (low +high) // 2
        if target == data[mid]:
            return True
        elif target < data[mid]:
            high = mid -1
        else:
            low = mid + 1
