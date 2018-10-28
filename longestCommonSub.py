import sys

def lcs(s1,s2):
    len1=len(s1)+1
    len2=len(s2)+1
    max1=0

    arr=[]
    for i in range(0,len1):
        arr.append([])
        for j in range(0,len2):
            arr[i].append(0)
            
    for i in range(1,len1):
        for j in range(1,len2):
            if(s1[i-1]==s2[j-1]):
                arr[i][j]=1+arr[i-1][j-1]
                if(arr[i][j]>max1):
                    max1=arr[i][j]
                    p1=i
                    p2=j
            else:
                arr[i][j]=max(arr[i-1][j],arr[i][j-1])
                if(arr[i][j]>max1):
                    max1=arr[i][j]
                    p1=i
                    p2=j                
    s=''                
    ele=arr[p1][p2]
    while(ele!=0):
     if(s1[p1-1]==s2[p2-1]):
        s=s1[p1-1]+s
        ele=arr[p1-1][p2-1]
        p1-=1
        p2-=1
     elif(ele==arr[p1-1][p2]):
        ele=arr[p1-1][p2]
        p1-=1
     elif(ele==arr[p1][p2-1]):
        ele=arr[p1][p2-1]
        p2-=1
        
    return str(s)

def main(a):
    s1=input("Enter first string:")
    #s2=input("Enter Second string:")
    s2=list(s1)
    s2=s2.sort()
    print(s2)
    s21=''
    for l in s2:
    	s21+=l
    str1=lcs(s1,s21)
    print("Longest common subsequence is:"+str1)

if __name__=='__main__':
    main(sys.argv)
