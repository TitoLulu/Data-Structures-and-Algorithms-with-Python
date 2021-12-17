from linear_search import verify, numbers
def binary_search(list,target):
    first = 0
    last = len(list) - 1

    while first <= last:
        midpoint = (first + last)//2

        if list[midpoint] == target:
            return midpoint
        elif list[midpoint] < target:
            first = midpoint + 1
            print('aaah!!')
        else:
            last = midpoint - 1

    return -1
result = binary_search(numbers,2)
verify(result)