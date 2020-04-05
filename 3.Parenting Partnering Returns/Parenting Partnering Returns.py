def PPReturns(list):
    arr = []
    for i in range(len(list)):
        arr.append((list[i][0],list[i][1], i))
    arr.sort()
    end_C = 0
    end_J = 0
    ans = []
    for start, end, index in arr:
        if start < end_C and start < end_J:
            return "IMPOSSIBLE"
        if start >= end_C:
            ans.append(('C', index))
            end_C = end
        else:
            ans.append(('J', index))
            end_J = end
    final = ''
    for c, index in sorted(ans, key=lambda x: x[1]):
        final += c
    return final
for i in range(int(input())):
    N = int(input())
    arr = []
    for k in range(N):
        S,E=map(int,input().split())
        arr.append([S,E])
    final = PPReturns(arr)
    print("Case #{}: {}".format(i+1, final))