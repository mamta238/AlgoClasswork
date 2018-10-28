import sys


def sumS(sets,sub,index,sum1,n,m):
    if(sum1==m):
        print(sub)
        return
    elif(sum1>m):
        return
    elif(index==n):
        return
    else:
        sumS(sets,sub,index+1,sum1,n,m)
        sum1+=sets[index]
        sub+=[sets[index]]
        sumS(sets,sub,index+1,sum1,n,m)
        sub.pop()
        


def main():
    n=int(input("Enter list length:"))
    print("Enter elements:")
    sets=[int(input()) for x in range(n)]
    m=int(input("Enter sum:"))
    sub=[]
    sumS(sets,sub,0,0,n,m)


if __name__=='__main__':
    main()
