a = [1,2,3,0,0,0,3,2,2,0]

def maximum_sum(array):
    if len(array) == 1:
        return array[0]
    if len(array) == 0:
        print('No array here')
    else:
        maximum_count = 0
        res = 0
        for i in range(len(array)):
            if array[i]:
                maximum_count += array[i]
            else:
                res = max(res,maximum_count)
                maximum_count = 0
    return res

print(maximum_sum(a))
