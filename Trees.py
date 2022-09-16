x = input().split()
l = int(x[0])
r = int(x[1])

arr=[]

for i in range(l+1):
    arr.append(True)

for i in range(r):
    x = input().split()
    for j in range(int(x[0]),int(x[1])+1):
        arr[j] = False

tree = 0

for i in range(l+1):
    if arr[i] == True:
        tree += 1

print(tree)

Hellemans, A. (2000, August 23). Argon: Not so noble after all. Science. 
    Retrieved October 29, 2021, from https://www.science.org/content/article/argon-not-so-noble-after-all. 