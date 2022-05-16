# You are given N identical eggs and you have access to a K-floored building from 1 to K.

# There exists a floor f where 0 <= f <= K such that any egg dropped at a floor higher than f will break, and any egg dropped at or below floor f will not break. There are few rules given below. 

# An egg that survives a fall can be used again.
# A broken egg must be discarded.
# The effect of a fall is the same for all eggs.
# If the egg doesn't break at a certain floor, it will not break at any floor below.
# If the eggs breaks at a certain floor, it will break at any floor above.
# Return the minimum number of moves that you need to determine with certainty what the value of f is.

# For more description on this problem see wiki page

# Example 1:

# Input:
# N = 1, K = 2
# Output: 2
# Explanation: 
# 1. Drop the egg from floor 1. If it 
#    breaks, we know that f = 0.
# 2. Otherwise, drop the egg from floor 2.
#    If it breaks, we know that f = 1.
# 3. If it does not break, then we know f = 2.
# 4. Hence, we need at minimum 2 moves to
#    determine with certainty what the value of f is.
# Example 2:

# Input:
# N = 2, K = 10
# Output: 4


    def __init__(self):
        self.h = {}
    def eggDrop(self,e, k):
        if(e == 1):
            return k
        if(k ==1 or k == 0):
            return k
        if((e,k) in self.h):
            return self.h[(e,k)]
        mini = sys.maxsize
        for i in range(1,k+1):
            if((e-1,i-1) in self.h):
                t1 = self.h[(e-1,i-1)]
            else:
                t1 = self.h[(e-1,i-1)] = self.eggDrop(e-1,i-1)
            if((e,k-i) in self.h):
                t2 = self.h[(e,k-i)]
            else:
                t2 = self.h[(e,k-i)] = self.eggDrop(e,k-i)
            temp = 1 + max(t1,t2)
            self.h[(e,k)] = mini = min(mini,temp)
        return mini