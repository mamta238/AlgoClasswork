import sys

def swap(a,b,ls):
    t=ls[a]
    ls[a]=ls[b]
    ls[b]=t



def qSort(ls,l,h,p):
    if(l>h):
        return
    else:
        i=l
        j=h
        while(True):
            while(ls[i]<ls[p] and i!=p):
                i+=1
            while(ls[j]>ls[p] and j!=l):
                j-=1
            if(i<j):
                swap(i,j,ls)
            else:
                break
        swap(i,p,ls)
        qSort(ls,l,i-2,i-1)
        qSort(ls,i+1,p-1,p)
            
        


def main():
    n=int(input("Enter list length:"))
    print("Enter elements")
    ls=[int(input()) for x in range(n)]
    print(ls)
    qSort(ls,0,n-2,n-1)
    print(ls)
if __name__=='__main__':
    main()
