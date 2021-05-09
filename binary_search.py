def binary_search(lst, target):
    """
    Binary search can onl be applied to a sorted list only
    """
    first = 0
    last = len(lst) - 1

    while first <= last:
        mid = (first + last)//2
        
        if lst[mid] == target:
            return mid
        
        elif lst[mid] <  target:
            first = mid + 1
            
        else:
            last = mid - 1

    return None



def verify(result):
    print("The position of the first target value is:", result)

    
l = [1,2,3,4,5,6,7,8,9]
result = binary_search(l, 9)

verify(result)
