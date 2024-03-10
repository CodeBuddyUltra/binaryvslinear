import time
from math import floor
T1 = eval(input("Enter some numbers : "))
num = eval(input("Enter the number to be searched: "))
T1 = list(T1)
T2 = T1.copy()
T1.sort()
t = time.time()

l = len(T1)
flag = False
first = 0
last = l-1
#rmoved function for optimization
#def closest(lst, K):
 #   smallest_diff = abs(K - lst[0])
  #  number = 0
   # for m in lst:
    #    diff = abs(K - m)
     #   if diff <=smallest_diff:
      #      smallest_diff = diff
       #     number = m
    #return m
while first <=last:
    while l>=4:
        l = len(T1)
        first = T1[0] 
        last = l-1
        #middle = int((first+last)/2)
        mid = floor(l/2)
        #mid = closest(T1, middle)
        
        if T1[mid] == num or T1[-1] == num:
                
            flag = True
            break
        if T1[mid] < num:
                
            #print("Now searching in the right  part")
            del T1[:mid-1]
            
        if T1[mid] > num:
                
                #print("Now searching in the left part")
            del T1[mid:]
            
    if T1[0] == num or T1[-1] == num:
        flag = True
        break
t1 = time.time()
if flag == True:
    
    print("Element has been found")
else:
    print("Element has not been entered")

print("Time taken in binary search=" , t1-t)
t2 = time.time()
flag_1 = False
for m in T2:
    if m == num:
        flag_1 = True
        break
if flag_1 == True:
    print("Number found")
else:
    print("Number not found")
t3 = time.time()
print("Time taken in linear search=", t3-t2)

