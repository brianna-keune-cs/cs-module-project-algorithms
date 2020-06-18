'''
Input: a List of integers
Returns: a List of integers
'''

def multiply(arr):
    product = 1
    for a in arr:
        product *= a
    return product


def product_of_all_other_numbers(arr):
    # Your code here

    # keep track of current index
    # while current index > len(arr)
    # using slicing with the current index
    # to create a list of arguments to pass in
    # send ^ list into a helper product function
    # for each product add it to a new array

    # loop over arr,
    # multiple i by next element
    list_of_products = []
    for i in range(len(arr)):
        product = multiply(arr) / arr[i]
        list_of_products.append(int(product))

    return list_of_products

'''
Understand:
    input: a list of numbers
    output: a list of equal length, with products of all other numbers

    [2, 4]
    [4 , 2] ???
    what happens in the above situation?
    what happens if there is only 1 digit? 

    [1, 1, 1]
    [1 * 1, 1 * 1, 1 * 1]
    [1, 1, 1]

    what happens if there is a zero?
    [0, 1, 1]
    [1 * 1, 0 * 1, 0 * 1]
    [1, 0, 0]
    

'''


if __name__ == '__main__':
    # Use the main function to test your implementation
    arr = [1, 2, 3, 4, 5]
    # arr = [2, 6, 9, 8, 2, 2, 9, 10, 7, 4, 7, 1, 9, 5, 9, 1, 8, 1, 8, 6, 2, 6, 4, 8, 9, 5, 4, 9, 10, 3, 9, 1, 9, 2, 6, 8, 5, 5, 4, 7, 7, 5, 8, 1, 6, 5, 1, 7, 7, 8]


    print(f"Output of product_of_all_other_numbers: {product_of_all_other_numbers(arr)}")
    # expected for first arr
    # [2 * 3 * 4 * 5, 1 * 3 * 4 * 5, 1 * 2 * 4 * 5, 1 * 2 * 3 * 5, 1 * 2 * 3 * 4]
    # [120, 60, 40, 30, 24]
