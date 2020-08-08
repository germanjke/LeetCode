#O(n)
def smallest_element(nums):
    smallest = nums[0]
    smallest_index = 0
    for i in range(1,len(nums)):
        if nums[i] < smallest:
            smallest = nums[i]
            smallest_index = i
    return smallest_index
    
def sorting_array(nums):
    new_array = []
    for i in range(len(nums)):
        smallest = smallest_element(nums)
        new_array.append(nums.pop(smallest))
    return new_array
