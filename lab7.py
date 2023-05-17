#insertionsort algoritham

A=[]

#number of element as input
n=5

for v in range(0,n):
    number=int(input("enter your number : "))

    if(number>10 and number<20):
        A.append(number)
    else:
        print("invalid number")
size=len(A)
print(A)

def insertionsort(A):


    for i in range(1,len(A)):
        key=A[i]
        j=i-1

        while j>=0 and A[j]>key:
            A[j+1]=A[j]
            j=j-1

        A[j+1]=key

insertionsort(A)
print("sorted Array",A)
