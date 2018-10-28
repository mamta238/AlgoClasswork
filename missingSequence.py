import sys

def findM(ls):
    n=len(ls)
    sum1=0
    for i in range(1,n+1):
        sum1^=i^ls[i-1]
    sum1^=i+1
    sum1^=i+2
    ans1='{:b}'.format(sum1)
    ans2=(ans1[::-1]).find('1')
    l=0
    for i in range(0,n):
        x='{:b}'.format(ls[i])
        x=x[::-1]
        if(x.find('1')==ans2):
            l^=ls[i]
    for i in range(1,n+3):
        x='{:b}'.format(i)
        x=x[::-1]
        if(x.find('1')==ans2):
            l^=i

    sum1^=l
    return(l,sum1)
            
        

def main():
    ls=input("Enter list:")
    ls=[int(x) for x in ls.split(',')]
    print(ls)
    (x,y)=findM(ls)
    print("Missing Numbers are "+str(x)+','+str(y))
    
if __name__=='__main__':
    main()
