import sys

solList=[]

def nQueen(ls,n,i):
    global solList
    if(n==i):
        solList+=[ls]
    else:    
        j=0
        pos=[]
        while(j<i):
                p=ls[j]
                d=i-j
                q=p-d
                r=p+d
                if p not in pos:
                    pos+=[p]
                if(q>=0):
                    if(q not in pos):
                        pos+=[q]
                if(r<n):
                    if(r not in pos):
                        pos+=[r]
                j+=1
        for j in range(0,n):
            if j not in pos:
                ls[i]=j
                nQueen(ls,n,i+1)


def main():
    global solList
    n=int(input("Enter number of queens:"))
    ls=[]
    for i in range(0,n):
        ls.append(-1)
    nQueen(ls,n,0)
    print(len(solList))
    
if __name__=='__main__':
    main()
