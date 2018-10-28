
import sys

def swap(i,j,a):
     a[i]^=a[j]
     a[j]^=a[i]
     a[i]^=a[j]

def percolate(i,n,a):
    p=int(n/2)-1
    flag=0
    while(i<=p):
        c1=i*2+1
        c2=i*2+2
        if(c1<n):
            if(c2<n):
                if(a[c1]>=a[c2]):
                    if(a[c1]>a[i]):
                       swap(c1,i,a)
                       i=c1
                    else:
                        flag=1
                elif(a[c2]>a[c1]):
                    if(a[c2]>a[i]):
                       swap(c2,i,a)
                       i=c2
                    else:
                        flag=1
            else:
                    if(a[c1]>a[i]):
                       swap(c1,i,a)
                       i=c1
                    else:
                       flag=1
        else:flag=1
        if(flag==1):break;
        


def maxHeap(a):
    n=len(a)
    p=int(n/2)-1
    i=p;
    while(i>=0):
       c1=i*2+1
       c2=i*2+2
       if(c1<n):
            if(c2<n):
                if(a[c1]>=a[c2]):
                    if(a[c1]>a[i]):
                       swap(c1,i,a)
                       percolate(c1,n,a)
                elif(a[c2]>a[c1]):
                    if(a[c2]>a[i]):
                       swap(c2,i,a)
                       percolate(c2,n,a)
            else:
                    if(a[c1]>a[i]):
                       swap(c1,i,a)
                       percolate(c1,n,a)
       i-=1    


def heapSort(a):
    n=len(a)
    maxHeap(a)
    swap(0,n-1,a)
    n=n-1
    while(n>1):
        percolate(0,n,a)
        swap(0,n-1,a)
        n=n-1

        
def main():
    n=int(input("Enter list size:"))
    list1=[]
    print("Enter list elements:")
    for i in range(0,n):
        list1+=[int(input())]
    print(list1)    
    heapSort(list1)
    print(list1)
    
if __name__=='__main__':
    main()
