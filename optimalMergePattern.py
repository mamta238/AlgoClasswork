import sys

def findMin(f,n):
    if(n==2):
        m1=f[0]
        m2=f[1]
    else:
        m2=m1=f[0]
        for i in range(1,n):
            if(f[i]<m1):
                m2=m1
                m1=f[i]
    return (m1,m2)
        
def optMerge(files,n):
    ls=[]
    while(n>1):
        (m1,m2)=findMin(files,n)
        files+=[m1+m2]
        files.remove(m1)
        files.remove(m2)
        ls+=[((m1,m2),m1+m2)]
        n-=1
    print(ls)

def main():
    files=[]
    n=int(input("Enter the number of files:"))
    print("Enter files")
    files=[int(input()) for x in range(n)]
    print(files)
    optMerge(files,n)

if __name__=='__main__':
    main()
