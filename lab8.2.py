arr=[]

for v in range(5):
    arr.append(input('enter a Number :   '))

print(arr)

def partition(arr,low,high):
    i=(low-1)
    pivot=arr[high]

    for j in range(low,high):
        if arr[j] <=pivot:
            i=i+1
            #arr[i],arr[j]=arr[j],arr[i]
            temp=arr[i]
            arr[i]=arr[j]
            arr[j]=temp
    #arr[i+1],arr[high]=arr[high],arr[i+1]
    temp=arr[high]
    arr[high]=arr[i+1]
    arr[i+1]=temp
    
    return i+1

def quicksort(arr,low,high):

    if low < high:
        q = partition(arr,low,high)
        quicksort(arr,low,q-1)
        quicksort(arr,q+1,high)


quicksort(arr,0,len(arr)-1)
print('sorted array : ',arr)
for i in range(len(arr)):
    print(arr[i])
