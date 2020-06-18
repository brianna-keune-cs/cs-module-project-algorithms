'''
Input: a List of integers
Returns: a List of integers
'''


def moving_zeroes(arr):
    # Your code here

    # if the value at current index is == to zero
    # pop off index and append to the array

    # store zeros in a new list
    # append new list to given arr
    # return mutated arr

    if len(arr) == 0 or len(arr) == 1:
        return arr
    
    if arr.count(0) == len(arr):
        return arr

    for i in range(0, len(arr)):
        if arr[i] == 0:
            arr.pop(i)
            arr.append(0)

    if arr[0] == 0:
        moving_zeroes(arr)

    return arr


'''
Understand:
    input: an arr
    output: mutated arr with all zero values at the end

    questions:
    what if the given array length is zero or 1?
'''


if __name__ == '__main__':
    # Use the main function here to test out your implementation
    arr = [0, 3, 1, 0, -2]

    print(f"The resulting of moving_zeroes is: {moving_zeroes(arr)}")
