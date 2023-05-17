A=[]
for v in range(4):
    A.append(int(input('Enter your number : ')))

print(A)


def selectionsort(A):
    n=len(A)

    for j in range (0,n-1):

        smallest=j

        for i in range(j+1,n-1):
            if A[i] < A[smallest]:
                smallest = i
            #A[j],A[smallest]=A[smallest],A[j]
            temp=A[j]
            A[j]=A[smallest]
            A[smallest]=temp


selectionsort(A)
print('sorted Array : ',A)
