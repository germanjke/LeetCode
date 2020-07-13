def merge2arrays(arr1: List[int], arr2: List[int]): #help function number 1
    i = 0 
    j = 0
    arr3 = [] #final list
    while i < len(arr1) and j < len(arr2): #main moment
        if arr1[i] <= arr2[j]:
            arr3.append(arr1[i])
            i+=1
        else:
            arr3.append(arr2[j])
            j+=1
    if i == len(arr1) and j != len(arr2): #here we add only nums from rest of j
        for v in range(j,len(arr2)):
            arr3.append(arr2[v])
    if j == len(arr2) and i != len(arr1): #here we add only nums from rest of i 
        for v in range(i, len(arr1)):
            arr3.append(arr1[v])
                
    return arr3
    
def sort1array(arr: List[int]): #help function number 2
    if len(arr) == 1:
        return arr
    else:
        return merge2arrays(sort1array(arr[:int(len(arr)/2)]), sort1array(arr[int(len(arr)/2):])) #divide our arr on 2 halfs

    
class Solution:
     
    def sortArray(self, nums: List[int]) -> List[int]:
        return sort1array(nums)
