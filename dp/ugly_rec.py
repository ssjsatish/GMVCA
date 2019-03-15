# uly number is defined as he number whose only prime factors are 2,3 or 5
# Given a number n find the nth ugly number
# n = 7 output: 8
# n = 10 output: 12

def maxDivide(a,b):
    while a%b==0:
        a = a/b
    return a
def getNthUgly(n):
    i = 1
    count = 1
    while n>count:
        i +=1
        no = maxDivide(i,2)
        no = maxDivide(no,3)
        no = maxDivide(no,5)
        if no == 1:
            count +=1
    return i
for _ in range(int(input())):
    n = int(input())
    print(getNthUgly(n))