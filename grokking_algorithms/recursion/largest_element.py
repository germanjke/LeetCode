def typical_largest_element(nums):
    largest = nums[0]
    largest_index = 0
    for i in range(len(nums)):
        if nums[i] > largest:
            largest = nums[i]
            largest_index = i
    return largest
    
def recursion_largest_element(nums):
    #базовый случай
    if len(nums) == 0:
        return 0
    if len(nums) == 1:
        return nums[0]
    #here we go with recursion
    else:
        return recursion_largest_element(nums[1:])
