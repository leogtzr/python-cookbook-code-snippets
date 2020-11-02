def mean(nums):
    return sum(nums, 0.0) / len(nums)

def drop_first_and_last_grades(grades):
    first, *middle, last = grades
    return mean(middle)

print(drop_first_and_last_grades([2, 4, 5, 6, 7, 9]))
