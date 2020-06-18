'''
Input: a List of integers as well as an integer `k` representing the size of the sliding window
Returns: a List of integers
'''


def sliding_window_max(nums, k):
    # Your code here
    window_maxes = []
    for i in range(len(nums) - k + 1):
        window = nums[i: k + i]
        max_in_window = window[0]
        for j in window:
            if j > max_in_window:
                max_in_window = j
            
        window_maxes.append(max_in_window)

    return window_maxes


'''
Understand:
    input: a list of numbers, and a window of size k
    output: an array of max values in each window

    what happens if the window size is larger than array length?
    what happens if window size is 0?
    both are 0?

    assumtions we start at index 0,
    and window end does not go past last index
    

'''

if __name__ == '__main__':
    # Use the main function here to test out your implementation
    arr = [1, 3, -1, -3, 5, 3, 6, 7]
    k = 3

    print(
        f"Output of sliding_window_max function is: {sliding_window_max(arr, k)}")
