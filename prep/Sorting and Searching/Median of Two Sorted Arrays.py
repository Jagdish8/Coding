# Given two sorted arrays nums1 and nums2 of size m and n respectively, return the median of the two sorted arrays.

# The overall run time complexity should be O(log (m+n)).

 

# Example 1:

# Input: nums1 = [1,3], nums2 = [2]
# Output: 2.00000
# Explanation: merged array = [1,2,3] and median is 2.
# Example 2:

# Input: nums1 = [1,2], nums2 = [3,4]
# Output: 2.50000
# Explanation: merged array = [1,2,3,4] and median is (2 + 3) / 2 = 2.5.
 

class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        if(len(nums2)<len(nums1)):
            return self.findMedianSortedArrays(nums2,nums1)
        n1 = len(nums1)
        n2 = len(nums2)
        low = 0
        high = n1
        while(low <= high):
            cut1 = low + (high-low)//2
            cut2 = ((1+n1+n2)//2) - cut1
            l1 = -sys.maxsize if cut1 == 0 else nums1[cut1 - 1]
            l2 = -sys.maxsize if cut2 == 0 else nums2[cut2 - 1]
            r1 = sys.maxsize if cut1 == n1 else nums1[cut1]
            r2 = sys.maxsize if cut2 == n2 else nums2[cut2]
            if(l1 <= r2 and l2 <= r1):
                if((n1+n2) % 2):
                    return max(l1,l2)
                else:
                    return (max(l1,l2)+min(r1,r2))/2
            if(l1 > r2):
                high = cut1 - 1
            else:
                low = cut1 + 1
        return 0

"""

naive approach will be O(n1+n2)

using binary search approach
lets do it for even sum of lengths first
example : nums1 : 1,3,4,7,10,12
          n1 = 6
          nums2 : 2,3,6,15
          n2 = 4
total sum of lengths = 6 + 4 = 10
merge array will look like : 1,2,3,3,4,6,7,10,12,15
therefore, if we want the median from the new merged array then we have to partition the new array
            between two halfs of length (n1+n2)//2 = 5
example : 1,2,3,3,4 | 6,7,10,12,15


so we'll be working on finding which elements from nums1 and nums2 will come in on the left side 
and which remaining of both on the right side

lets suppose we take the 4 elements from array import array
from nums1 on left and remaining (5 - 4 = 1) of nums2
and the remaining of both will be on the side side
example:           left     |     right
      nums1      1,3,4,7    |     10,12
      nums2          2      |     3,6,15

or lets take 3 from nums1 and remaining 2 from nums2
example:           left     |     right
      nums1      1,3,4      |     7,10,12
      nums2        2,3      |     6,15

or lets take 2 from nums1 and remaining 3 from nums2
example:           left     |     right
      nums1         1,3     |     4,7,10,12
      nums2         2,3,6   |     15

we need to check whether the picked left half is valid(all the elements on left should
be less than or equal to the all elements on the rigth side)

since nums1 and nums2 are already sorted, no need to check whether left of nums1 is less
than or equal to the right of nums1
||ly for nums2

we need to check whether elements on left of nums1 is less or equal to elements on right of nums2
||ly elements on left of nums2 with elements on right of nums1

for example:       left     |     right
      nums1      1,3,4,7    |     10,12
      nums2          2      |     3,6,15

to check left of nums1 with right of nums2
check whether last element in left of nums1 is less than or equal to first element of right of nums2
i.e., 7 <= 3, which is False 
Therefore, the partition is incorrect


for example:       left     |     right
      nums1         1,3     |     4,7,10,12
      nums2         2,3,6   |     15

left of nums1 with right of nums2
3 <= 15 : True
left of nums2 with right of nums1:
6 <= 4 : False
Therefore, the partition is incorrect

for example:       left     |     right
      nums1        1,3,4    |     7,10,12
      nums2        2,3      |     6,15

left of nums1 with right of nums2
4 <= 6 : True
left of nums2 with right of nums1:
3 <= 7 : True
Therefore, the partition is correct

now, we have the left and right partitions
lets take l1 = last element in left of nums1 = 4
lets take l2 = last element in left of nums2 = 3
lets take r1 = first element in right of nums1 = 7
lets take r2 = first element in right of nums2 = 6

now, after merge the last element on left side will be max(l1,l2) = max(4,3) = 4
and first element on right side will be min(r1,r2) = min(7,6) = 6

therefore the median is (4+6)/2 = 5

for all this, we need to know how to use the binary search
through binary search we need to find where we can partition in nums1

let cut1 be the cut in nums1
let cut2 be the cut in nums2

for example:       left     |     right
      nums1      1,3,4,7    |     10,12
      nums2          2      |     3,6,15

we know this is not a valid partition because l1 > r2
so fix this we need to decrease l1 and increase r2
we can decrease l1 by moving the partition toward left
when we move partition to left the size of left becomes 4 so we need to add a element from right
of nums2 into left of nums1 to get same size on both sides
In this way, we decrease l1 by shifting left and also increase r2 as a by product

After shift:
                   left     |     right
      nums1        1,3,4    |     7,10,12
      nums2        2,3      |     6,15


for example:       left     |     right
      nums1         1,3     |     4,7,10,12
      nums2         2,3,6   |     15

invalid because l2 > r1
so need to decrease l2 and increase r1
same logic like previous, if we want to increase r1 we need to shift partition towards right
since lenght of left will be more, last element of left of nums2 will shift to right
In this way, we increas r1 by shifting right and also decrease l2 as a by product

After shift:
                   left     |     right
      nums1        1,3,4    |     7,10,12
      nums2        2,3      |     6,15


dry run
lets take nums1 : 7,12,14,15
          nums2 : 1,2,3,4,9,11
now we can minimum of 0 elements
and maximum of 4 elements from nums1
low = 0
high = 4

mid = (0+4)/2 = 2
cut1 = 2 on nums1               (7,12  | 14,15)
cut2 = (4+6)/2 - cut1 = 3       (1,2,3 | 4,9,11)

12<4 False
l1(12) has to decreased (shift left), high = cut1 - 1 = 1

low = 0
high = 1
cut1 = 0    (   -INF   | 7,12,14,15)
cut2 = 5    (1,2,3,4,9 | 11        )

9 < 7 : False
r1(7) has to be increase (shift right), low = cut1 + 1 = 1

low = 1
high = 1
cut1 = 1    (   7    | 12,14,15)
cut2 = 4    (1,2,3,4 | 9,11    )

this is valid
median  = (max(7,4)+min(12,9))/2 = (7+9)/2 = 8


we can say,
l1 = -INF if cut1 == 0 else nums1[cut1-1]
l1 = -INF if cut1 == 0 else nums2[cut1-1]
r1 = INF if cut1 == 4 else nums1[cut1+1]
r2 = INF if cut1 == 4 else nums2[cut1+1]

 

Now comes for the odd lengths
since we know that for odd length we need to check for only one element
lets take nums1 : 7,12,14,15,16
          nums2 : 1,2,3,4,9,11
        total = 11
lets divide the new_list such that left half is 6 and right half is 5
            1,2,3,4,7,9 | 11,12,14,15,16

in this the median will be the last from the left
so median  = max(l1,l2)

and we have to add 6 on left and 5 on left 
low = 0
high = 5 (len(nums1))
cut1 = (high-low)//2 = 2
cut2 = (1+n1+n2)//2 - cut1 = 6-2 = 4

(1+n1+n2)//2 - cut1 will work for even length as well since (1+4+6)//2 = 11//2 = 5

Try to do the binary search on the smaller array


Time complexity:
        since we will be doing binary search on minimum length array
        O(log2(min(n1,n2)))
space complexity:
        O(1)

https://www.youtube.com/watch?v=NTop3VTjmxk
"""
