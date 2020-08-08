def binary_search(nums, item):
    low = 0 
    high = len(nums)-1
    while low <= high: #пока не сократим всё до единственного элемента
        mid = low + (high-low)//2 
        guess_item = nums[mid]
        if guess_item == item:
            return mid
        if guess_item > item:
            high = mid - 1
        else:
            low = mid + 1
    return None
