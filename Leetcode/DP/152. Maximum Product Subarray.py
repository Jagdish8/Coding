def solve(arr):
    if(not arr):
        return 0
    mi = ma = res = arr[0]
    for i in range(1,len(arr)):
        tmin,tmax = mi,ma
        mi = min(arr[i]*tmin,arr[i]*tmax,arr[i])
        ma = max(arr[i]*tmin,arr[i]*tmax,arr[i])
        res = max(res,ma)
    return res
print(solve([2,3,8,-1,8,-4,1,-4,2,0]))