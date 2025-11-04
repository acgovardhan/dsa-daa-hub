#MergeSort 

def MergeSort(A, low, high):
  if(low<high):
    mid = (low+high)//2
    MergeSort(A, low, mid)
    MergeSort(A, mid+1, high)
    Merge(A, low, mid, high)

def Merge(A, low, mid, high):
  Arr1 = A[low : mid+1]
  Arr2 = A[mid+1: high+1]
  ResArr = []
  i = j = 0
  while i < len(Arr1) and j < len(Arr2):
    if(Arr1[i]<Arr2[j]):
      ResArr.append(Arr1[i])
      i+=1
    else:
      ResArr.append(Arr2[j])
      j+=1
  
  while i < len(Arr1):
    ResArr.append(Arr1[i])
    i+=1
  while j < len(Arr2):
    ResArr.append(Arr2[j])
    j+=1
  A[low : high+1] = ResArr

#output
A = [9,3,7,5,6,4,8,2]
l = 0
h = len(A)-1
MergeSort(A, l, h)
print(A)
