import sys

def construct(n):
    a=[[0 for x in range(n)] for y in range (n)]
    return a


def cMult(n,d,m,p1):
    i=1
    while(i<n):
        
        for j in range(0,n-i):
            k=j+i
            min1=1000000000
            pos=0
            for p in range(j,k):
                val=m[j][p]+m[p+1][k]+(d[j]*d[p+1]*d[k+1])
                if(val<min1):
                    min1=val
                    pos=p
            m[j][k]=min1
            p1[j][k]=pos
        i+=1
        
    return (p1,m[0][n-1])    

def resPrint(p,i,n,a):
    if(len(a)==2 or len(a)==1):
        return a
    else:
        no=p[i][n]
        one=a[i:no+1]
        two=a[no+1:]
        ans='('+resPrint(p,i,no,one)+')'+'('+resPrint(p,no+1,n,two)+')'
        return ans
    
    
    
def main():
    n=int(input("Enter the number of matrices:"))
    d=[]
    prev=0
    for i in range(0,n):
        print("Enter dim of matrix-"+str(i+1))
        a=int(input())
        b=int(input())
        if(i!=0):
            if(a!=prev):
                print("Cannot be multiplied")
                return
        
        prev=b
        d.append(a)
    d.append(b)
    m=[]
    p=[]
    
    m=construct(n)
    p=construct(n)
    (p,res)=cMult(n,d,m,p)
    a="".join([chr(x) for x in range(65,65+n)])
    str1=resPrint(p,0,n-1,a)
    print(str1)
    
if __name__=='__main__':
    main()
