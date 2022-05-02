

list1=[50,60,10]
list2=[10,20,13]
def add_numbers_lis(list1,list2): 
    i=0
    j=0
    sum=0
    while i<len(list1)and j<len(list2):
        sum=list1[i]+list2[j]
        print(sum)
        i=i+1
        j=j+1
add_numbers_lis(list1,list2)
   