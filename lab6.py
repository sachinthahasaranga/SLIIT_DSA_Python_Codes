A=[]

for v in range(4):
    A.append(int(input("Enter your number : ")))

print(A)    


def bubblesort(A):
    n=len(A)

    for i in range (1,n):
        for j in range (1,n-i+1):
            if A[j]< A[j-1]:
                temp=A[j]
                A[j]=A[j-1]
                A[j-1]=temp


bubblesort(A)
print('sorted Array ')
print(A)
