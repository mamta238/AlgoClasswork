import sys

def check(a,ls):
    if(a in ls):
        return True
    else:
        return False

def hamil(graph,cir,vertex,st,n,count):
    ls=graph[vertex]
    if(count==n):
        if(st in ls):
            cir+=[st]
            print(cir)
    else:
        for i in range(len(ls)):
            if(ls[i] not in cir):
                cir+=[ls[i]]
                hamil(graph,cir,ls[i],st,n,count+1)
                
        


def main():
    graph=[]
    n=int(input("Enter number of vertices:"))
    for i in range(n):
        ls=[]
        v=int(input("Enter number of vertices adjacent to v"+str(i)+':'))
        for i in range(v):
            ls+=[int(input())]
        graph+=[ls]
    cir=[0]
    print(graph)
    hamil(graph,cir,0,0,n,1)    
        
    
if __name__=='__main__':
    main()
