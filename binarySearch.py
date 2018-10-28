import sys


def binarySearch(ls,key,low,high):
    if(low>=high):
        return -1
    else:
        mid=int((low+high)/2)
        if(key==ls[mid]):
            return mid
        elif(key<ls[mid]):
            n=binarySearch(ls,key,low,mid-1)    
        else:
            n=binarySearch(ls,key,mid+1,high)
        return n


def main():
    ls=[]
    n=int(input("Enter n:"))
    print("Enter numbers")
    for i in range(0,n):
        ls.append(int(input()))
    key=int(input("Enter key"))
    ls=sorted(ls)
    pos=binarySearch(ls,key,0,n-1)
    if(pos==-1):
        print("not found")
    else:
        print("found at position:"+str(pos+1))
    
if __name__=='__main__':
    main()
