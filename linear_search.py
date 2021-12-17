from verify import verify, numbers

def linear_search(list, target):
    """
    Returns the index position of target if found, else None
    """
    for i in range(0,len(list)):
        if list[i] == target:
            return i
    return None 


result = linear_search(numbers,2)
verify(result)
