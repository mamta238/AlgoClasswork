
def allPairs(cur,n,max1):
    for i in range(n):
        prev=cur
        for j in range(n):
            for p in range(n):
                if(j==p):
                    cur[j][p]=0
                elif(j==i or p==i):
                    cur[j][p]=prev[j][p]
                else:
                    if(prev[j][p]<0 and (prev[j][i]<0 or prev[i][p]<0)):
                        cur[j][p]=-1
                    elif(prev[j][p]>0 and (prev[j][i]<0 or prev[i][p]<0)):
                        cur[j][p]=prev[j][p]
                    elif(prev[j][p]<0 and (prev[j][i]>0 and prev[i][p]>0)):
                        cur[j][p]=prev[j][i]+prev[i][p]
                    else:
                        cur[j][p]=min(prev[j][p],(prev[j][i]+prev[i][p]))
                    
    return cur

def main():
    n=int(input("Enter number of vertices:"))
    graph=[]
    max1=0
    for i in range(n):
        ls=[]
        for j in range(n):
            if(i!=j):
                w=int(input("Enter path distance between v"+str(i)+" and v"+str(j)+":"))
                if(w>max1):
                    max1=w
            else:
                w=0
            ls+=[w]
        graph+=[ls]
    print(graph)
    ans=allPairs(graph,n,max1)
    print(ans)
            
if __name__=='__main__':
    main()
