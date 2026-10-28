"""
ДЗ презентации 3, повышенный уровень, задача 2.
Время: 25–35 минут.

Тема: O(n) поиск min и max.

Условие:
    Реализуйте функцию min_max(nums) -> (min_val, max_val)
    за O(n).

Пример:
    In: [3, 1, 4, 1, 5, 9, 2, 6]
    Out: (1, 9)
"""

def min_max(nums: list) -> tuple:
    minimum = nums[0]
    maximum = nums[0]
    for i in nums:
        if i > maximum:
            maximum = i
        elif i < minimum:
            minimum = i
    a = minimum, maximum
    return a

def min_max_again(nums):
    n = len(nums)
    if len(nums) == 1:
        return nums[0], nums[0]

    if nums[0] < nums[1]:
        min_val, max_val = nums[0], nums[1]
    else:
        min_val, max_val = nums[1], nums[0]

    i = 2
    while i + 1 < n:
        if nums[i] < nums [i+1]:
            if nums[i] < min_val: min_val = nums[i]
            if nums[i+1] > max_val: max_val = nums[i+1]
        if nums[i] > nums[i+1]:
            if nums[i+1] < min_val: min_val = nums[i+1]
            if nums[i] > max_val: max_val = nums[i]
        i += 2

    if i < n:
        if nums[i] < min_val: min_val = nums[i]
        if nums[i] > max_val: max_val = nums[i]

    return min_val, max_val

if __name__ == "__main__":
    assert min_max_again([3, 1, 4, 1, 5, 9, 2, 6]) == (1, 9)
    assert min_max_again([7]) == (7, 7)
    assert min_max_again([-5, -1, -10]) == (-10, -1)
    print("task_02 (p3 advanced): тесты пройдены")
