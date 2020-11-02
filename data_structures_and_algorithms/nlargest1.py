def nsmallest(n, ls):
    if not ls:
        return ls
    if n >= len(ls):
        return ls
    copy = ls[:]
    copy.sort()
    return copy[:n]

def nlargest(n, ls):
    if not ls:
        return ls
    if n >= len(ls):
        return ls
    copy = ls[:]
    # copy.sort(reverse=True)
    copy = copy[(-n):]
    copy.sort(reverse=True)
    return copy

nums = [1, 8, 2, 23, 7, -4, 18, 23, 42, 37, 2]

original_list = nums[:]

# nums.sort()

#print(nums)
#print(original_list)

print(nlargest(3, nums))
# print(nsmallest(3, nums))
