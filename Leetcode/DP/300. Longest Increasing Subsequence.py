def solve(nums):
    dptable = [1]*(len(nums))

    for i in range(1,len(nums)):
        res = 1
        for j in range(i):
            if nums[i] > nums[j]:
                res = max(res, dptable[j]+1)

        dptable[i] = res

    return max(dptable)