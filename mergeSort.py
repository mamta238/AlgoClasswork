
import sys

def merge(a,low,mid,high):
    i=low
    j=mid
    k=0
    b=[]
    while(i<mid and j<high):
        if(a[i]<=a[j]):
            e=a[i]
            b+=[e]
            k+=1
            i+=1
        else:
            e=a[j]
            b+=[e]
            j+=1
            k+=1
           
    if(i<mid):
        while(i<mid):
            e=a[i]
            b+=[e]
            k+=1
            i+=1
    if(j<high):
        while(j<high):
            e=a[j]
            b+=[e]
            k+=1
            j+=1
   
    p=low        
    for z in range(0,k):
        a[p]=b[z]
        p+=1
    
     

def mergeSort(a,low,high):
    if(low<(high-1)):
        mid=int((low+high)/2)
        mergeSort(a,low,mid)
        mergeSort(a,mid,high)
        merge(a,low,mid,high)
        

def main(a):
    list1=[]
    n=int(input("Enter list length:"))
    print("Enter list elements:")
    for i in range(0,n):
        list1+=[int(input())]
    mergeSort(list1,0,n)
    print(list1)

if __name__=='__main__':
    main(sys.argv)
