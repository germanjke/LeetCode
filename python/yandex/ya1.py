#maximum len of subaray of ones in array of zeros/ones
#[1,1,1,0,0,1,1] - 3
#[1,1,1,1,1,1,1] - 7
#[1,1,0,0,0,0,0] - 2
def max_ones_subbaray(data): 
    res = 0
    count = 0
    for i in data:
        if i:
            count += 1
            res = max(res,count)
        else:
            count = 0
    return res
    
#here we go now its more hard question 
#maximum len of subaray of ones in array of zeros/ones IF we deleting one random elemnent in this array

#NEED CHANGES

def orig(data):
    res = 0
    p = 0
    c = 0
    p1 = False
    for i in data:
        if i:
            c += 1
            res = max(res, p + c)
            p1 = False
        elif p1:
            p = c
            c = 0
            p1 = False
        else:
            p = 0
    return res
