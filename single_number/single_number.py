'''
Input: a List of integers where every int except one shows up twice
Returns: an integer
'''


def single_number(arr):
    # Your code here
    # loop through the array
    # check if that number is repeated later
    # loop through remaining elements
    # find the element that doesn't have the pair

    # if the current index is in the copied arr
    # increase the current index
    # save value at i and see if that's equal to j

    # [3, 6, 4, 5, 6, 3, 4]
    # if we are at index 0 = 3
    # loop through copied arr
    # and the value 3 is in the rest of the array,
    # we move to the next index
    # but if the value is not in the array we return that value

    # we could loop through array and try to find the value of i within itself,
    # if that fails return the value of current index

    # during the excute phase, 
    # and failing,
    # remembered the count method in python

    for i in range(len(arr)):
        if arr.count(arr[i]) == 1:
            return arr[i]                    


'''
Understand:
    input: an array
    output: an integer

    questions:
        How do we keep track of matching elements?

    assumtions:
        1 number that does not have a pair
        Every other number will have a pair
'''


if __name__ == '__main__':
    # Use the main function to test your implementation
    arr = [1, 1, 4, 4, 5, 5, 3, 3, 9, 0, 0]

    print(f"The odd-number-out is {single_number(arr)}")
