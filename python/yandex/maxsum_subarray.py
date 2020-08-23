a = [24,0,1,2,3,0,0,0,2,3,4,1,11]

def max_subarray(numbers):
    best_sum = 0  
    current_sum = 0
    for x in numbers:
        if x:
            current_sum = max(0, current_sum + x)
            best_sum = max(best_sum, current_sum)
        else:
            current_sum = 0
    return best_sum

print(max_subarray(a))
