'''
Input: an integer
Returns: an integer
'''


def eating_cookies(n, cache=[]):
    # Your code here
    if n <= 0:
        return 1
    if n == 1:
        return 1
    if n == 2:
        return 2
    if n == 3:
        return 4
    if n > 3:
        return eating_cookies(n - 3) + eating_cookies(n - 2) + eating_cookies(n - 1)


if __name__ == "__main__":
    # Use the main function here to test out your implementation
    num_cookies = 5

    print(
        f"There are {eating_cookies(num_cookies)} ways for Cookie Monster to each {num_cookies} cookies")


'''
input, number of cookies to be eaten
output, how many ways he could eat amount of cookies


'''
