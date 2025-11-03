n = 5
a = [2, 8, 5, 3, 9, 4]

for i in range(2, n+1):
  key = a[i]
  j=i-1
  while j>0 and a[j]>key:
    a[j+1] = a[j]
    j = j-1
  a[j+1] = key

print(a)