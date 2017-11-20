'''
 quick sort 
'''

def quickSqort(arr):
    if len(arr)<=1:
        return arr
    pivot =arr[len(arr)/2]
    left=[x for x in arr if x < pivot]
    right=[x for x in arr if x > pivot]
    midle=[x for x in arr if x==pivot]
    return quickSqort(left)+midle+quickSqort(right)
    
    
    
    
if __name__ == '__main__':
    print quickSqort([1,2,6,3])
    
    