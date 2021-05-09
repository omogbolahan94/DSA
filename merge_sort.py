def split(lst):
    """
    Divide the unsorted list at midpoint into sublists
    Returns two(2) sublists - left and right
    """
    mid = len(lst)//2  # floor division
    left  = lst[:mid]
    right = lst[mid:]
    return left, right


def merge(left, right):
    """
    Merges two(2) lists, and sorting them in the process
    Returns a new merged list
    """

    sorted_list = []
    i = 0  # i to trsck the index of the left list
    j = 0  # j to track the list of the right list

    # comparing values in each list
    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            sorted_list.append(left[i])
            i += 1
        else:
            sorted_list.append(right[j])
            j += 1



    # if the length of left list is greater than that of right list
    while i < len(left):
        sorted_list.append(left[i])
        i += 1

    # if the length of right list is greater than that of left list
    while j < len(right):
        sorted_list.append(right[j])
        j += 1

    return sorted_list


def merge_sort(lst):
    # if the lst contains no element or one(1) element 
    if len(lst) <= 1:
        return lst

    left_half, right_half = split(lst)
    left = merge_sort(left_half)
    right = merge_sort(right_half)

    return merge(left, right)



def verify_sorted(lst):
    """
    Compare the first two(2) element of the list and calling
    the new fuction recursively to compare the first two element
    until the base case

    Returns boolean
    """
    n = len(lst)
    if n == 0 or n == 1:
        return True
    return lst[0] < lst[1] and verify_sorted(lst[1:])


alist = [54,62,93,17,77,31,44,55,20]

print("Verify unsorted list: ", verify_sorted(alist))
print("Unsorted list is: ", alist)

print("\n")

l = merge_sort(alist)
print("Verify sorted list: ", verify_sorted(l))
print("Sorted list is: ", l)

    
