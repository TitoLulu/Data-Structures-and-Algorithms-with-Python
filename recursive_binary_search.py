from verify import verify, numbers

def recursive_binary_search(list, target):

    mid = len(list) // 2
    print(list, '-->', mid)
    if list[mid] == target:
        return True

    else:
        if list[mid] < target:
            return recursive_binary_search(list[mid+1:],target)
        else:
            return recursive_binary_search(list[:mid], target)

result = recursive_binary_search(numbers,9)
verify(result)