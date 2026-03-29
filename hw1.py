"""
Question 1 – N-th Biggest Number
Write a function that gets:

A list of numbers (with duplicates)
A number n
The function should return the n-th biggest unique number in the list

Example:

[88, 100, 90, 95, 95, 97, 97, 99, 97, 99] , n = 4

Result:

95

Explanation:

Unique sorted values (descending):

100, 99, 97, 95, 90, 88

The 4th biggest number is 95

Rules:

Ignore duplicates when counting
Assume n is valid (you don’t need to handle errors)
"""


def nth_biggest(nums: list, n: int) -> int:
    unique_nums = set(nums)
    print(unique_nums)
    sorted_unique = sorted(unique_nums, reverse=True)
    print(sorted_unique)

    return sorted_unique[n - 1]

numbers = [88, 100, 90, 95, 95, 97, 97, 99, 97, 99]
print(nth_biggest(numbers, 4))  # פלט: 95

