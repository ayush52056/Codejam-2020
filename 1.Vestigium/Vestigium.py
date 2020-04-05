def rcheck(A,N,index):
    array=A[index]
    a ={i:array.count(i) for i in array}
    a=list(a.values())
    if any(a[x] > 1 for x in range(N)):
        return 1
    return 0
def ccheck(A,N,index):
    trans = [[A[j][i] for j in range(len(A))] for i in range(len(A[0]))] 
    array=trans[index]
    a = {i:array.count(i) for i in array}
    a=list(a.values())
    if any(a[x] > 1 for x in range(N)):
        return 1
    return 0
for i in range(int(input())):
    A=[]
    su=0
    r=0
    c=0
    N=int (input())
    for _ in range(N):
        As=list(map(int,input().split()))
        A.append(As)
    for k in range(N):
        su+=A[k][k]    
        r=r+rcheck(A,N,k)
        c=c+ccheck(A,N,k) 
    print('case #{}: {} {} {}'.format(i+1, su,r, c))
