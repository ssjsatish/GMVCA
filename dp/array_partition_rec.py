def isSubsetSum(a, n, summ):
    if summ==0:
        return True
    if n == 0 and summ != 0:
        return False
    # if the last element is greater than the sum
    if a[n-1] > summ:
        return isSubsetSum(a, n-1, summ)
    return isSubsetSum(a, n-1, summ) or isSubsetSum(a, n-1, summ-a[n-1])

def find_partition(a,n):
    summ = sum(a)
    #print(summ)
    if summ%2==1:
        return False
    return isSubsetSum(a,n,summ//2)

arr = [2,2,1,8] 
n = len(arr) 
if find_partition(arr, n) == True: 
    print ("Can be divided into two subsets of equal sum") 
else: 
    print ("Can not be divided into two subsets of equal sum")