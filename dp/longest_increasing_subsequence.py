'''
Given a unsorted array, find the length of logest increasing subsequence 
and print the longest increasing subsequence
e.g. a = [5, 1, 6, 3, 9, 11, 2]
length = 4
sequence: [5, 6, 9, 11]
'''
global maximum
def _lis(a, n):
    global maximum
    if n == 1:
        return 1
    maxEndHere = 1

    for i in range(1,n):
        res = _lis(a, i)
        if a[i-1]<a[n-1] and res+1 > maxEndHere:
            maxEndHere = res + 1
    maximum = max(maximum, maxEndHere)
    return maxEndHere
def lis(ar):
    global maximum
    n = len(ar)
    maximum = 1
    _lis(ar, n)
    return maximum

arr = [10 , 22 , 9 , 33 , 21 , 50 , 41 , 60] 
n = len(arr) 
print("Length of lis is ", lis(arr) )