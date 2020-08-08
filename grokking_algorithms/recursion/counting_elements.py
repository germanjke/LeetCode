#typical
def counting_elements(nums):
    count = 0
    for i in range(len(nums)):
        count += 1
    return count
#rec
def recursion_counting_elements(nums):
    if len(nums) == 0:
        return 0
    if len(nums) == 1:
        return 1
    else:
        return 1 + recursion_counting_elements(nums[1:])

#clean solution
def clean_recursion_counting_elements(nums):
    if nums == []:
        return 0
    else:
        return 1 + clean_recursion_counting_elements(nums[1:])
