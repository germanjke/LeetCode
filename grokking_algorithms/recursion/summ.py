#typical 
def summ_array(nums):
    summ = 0
    for i in nums:
        summ += i
    return summ
#recursion
def summ_array_recursion(nums):
    if len(nums) == 0:
        return 0
    if len(nums) == 1:
        return nums[0]
    if len(nums) == 2:
        return nums[0] + nums[1]
    else:
        return nums[0] + summ_array_recursion(nums[1:])
