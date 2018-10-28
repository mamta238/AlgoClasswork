import sys

c=0

def gColor(graph,n,vertex,index,colors,nc):
    global c
    if(index==n):
        l=[]
        c+=1
        for i in range(n):
            l+=[colors[vertex[i]]]
        print(l)   
    else:
        lc=[-1 for x in range(nc)]
        ls=graph[index]
        for j in range (len(ls)):
            if(vertex[ls[j]]!=-1):
               lc[vertex[ls[j]]]=1 
        for j in range(nc):
            
            if(lc[j]==-1):
                vertex[index]=j
                gColor(graph,n,vertex,index+1,colors,nc)
                vertex[index]=-1

def main():
    graph=[]
    n=int(input("Enter number of vertices:"))
    for i in range(n):
        no=int(input("Enter number of vertices adjacent to vertex "+str(i)+':'))
        print("Enter adjacent vertices for vertex "+str(i)+':')
        ls=[int(input()) for x in range (no)]
        graph+=[ls]

    nc=int(input("Enter number of colours:"))
    print("Enter colors:")
    colors=[input() for x in range(nc)]
    vertex=[-1 for x in range(n)]
    gColor(graph,n,vertex,0,colors,nc)
    print("Total combinations:"+str(c))

if __name__=='__main__':
    main()
