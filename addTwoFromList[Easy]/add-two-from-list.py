#!/usr/bin/env python3
# Given a list of numbers and a number k, return whether any two numbers from the list add up to k.
# For example, given [10, 15, 3, 7] and k of 17, return true since 10 + 7 is 17.
# Bonus: Can you do this in one pass?

# For Self:
#    Question #1: Can syou add the same number?
#       Answer: I think not since it says any TWO numbers.
#    Question #2: Can there be the same number in the list?
#       Answer: Since it is a list, probably... if it was a set, then no

def is_sum_in_list(num_list: list, k: int):
    for i in num_list:
        temp_num = k - i
        if (temp_num != i and (temp_num) in num_list):
            return True
    return False

def isEqual(actual, expected, message):
    if (actual == expected):
        print ('test passed')
        return True
    else:
        print(message)
        return False

def test_original_example():
    expected = True
    actual = is_sum_in_list([10, 15, 3, 7], 17)
    isEqual(actual, expected,'Test original example did not pass')

def test_same_number():
    expected = True
    actual = is_sum_in_list([10, 10, 3, 7], 20)
    isEqual(actual, expected,'Test same number in list did not pass')

if __name__ == '__main__':
    test_original_example()
    test_same_number()