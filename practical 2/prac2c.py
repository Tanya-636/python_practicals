def histogram(val):
    for i in val:
        print('*'*i)
        
lst = []
n = int(input("Enter number of elements : "))

for i in range(0, n):
    ele = int(input())
    lst.append(ele)
    
histogram(lst)