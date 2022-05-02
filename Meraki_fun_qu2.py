 
def  fun(num):
    i=0
    max=num[0]
    while i<len(num):
        if num[i]>max:
          max=num[i]
        i=i+1
    print(max)
num=[3, 5, 7, 34, 2, 89, 2, 5]
fun(num)



def fun(num):
    i=0
    sum=0
    while i<len(num):
        sum+=num[i]
        i=i+1
    print(sum)
num=[1, 2, 3, 4, 5]
fun(num)


list = [8, 6, 4, 8, 4, 50, 2, 7]
def minimum(number):
    i=0
    a=[]
    while i<len(number):
        a=min(number)
        i+=1
    print(a)
number=[8,6,4,8,4,50,2,7]
minimum(number)
    