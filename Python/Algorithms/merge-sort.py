unsorted_lst = [38, 27, 43, 77, 127, 5, 52, 12, 333, 2, 32, 125, 10]

def merge_sort(unsorted_lst): 

    # If the list is empty or only have one element its already sorted, and we return the input
    if len(unsorted_lst) <= 1:
        return unsorted_lst
    
    # If the list contains a lot of elements, its better to use a non-recursice algorithm
    if len(unsorted_lst) > 20:
        return sorted(unsorted_lst)

    # Define sorted list location
    sorted_lst = []

    # Find the middle of the list
    mid_index = int(len(unsorted_lst) / 2)

    # Split the list in the middle 
    right_lst = merge_sort(unsorted_lst[:mid_index])
    left_lst = merge_sort(unsorted_lst[mid_index:])

    # Define pointers
    r_p = 0
    l_p = 0

    # Merge the lists
    while r_p < len(right_lst) and l_p < len(left_lst):
        
        if right_lst[r_p] > left_lst[l_p]:
            sorted_lst.append(left_lst[l_p])
            l_p += 1
        else:
            sorted_lst.append(right_lst[r_p])
            r_p += 1
   
    # Add remaining elements from a larger list to the sorted result
    sorted_lst += right_lst[r_p:]
    sorted_lst += left_lst[l_p:]
    return sorted_lst 


# Trigger point for the algorithm
if __name__ == '__main__':
    print(merge_sort(unsorted_lst))


