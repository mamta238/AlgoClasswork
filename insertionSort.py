import sys


def insertionSort(a):
	l=len(a)
	for i in range(1,l):
		j=i-1
		while(j>=0):
			if a[j]<a[j+1]:
				break
			else:
				a[j+1]^=a[j]
				a[j]^=a[j+1]
				a[j+1]^=a[j]
			j-=1	
	print(a)		


def main(a):
	list1=[]
	l=int(input("Enter length:"))
	print("Enter list elements")
	for i in range(0,l):
		list1.append(int(input()))
	print(list1)
	insertionSort(list1)	

if __name__=='__main__':
	main(sys.argv)
