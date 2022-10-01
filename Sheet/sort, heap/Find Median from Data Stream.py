# # https://leetcode.com/problems/find-median-from-data-stream/

# The median is the middle value in an ordered integer list. If the size of the list is even, there is no middle value and the median is the mean of the two middle values.

# For example, for arr = [2,3,4], the median is 3.
# For example, for arr = [2,3], the median is (2 + 3) / 2 = 2.5.
# Implement the MedianFinder class:

# MedianFinder() initializes the MedianFinder object.
# void addNum(int num) adds the integer num from the data stream to the data structure.
# double findMedian() returns the median of all elements so far. Answers within 10-5 of the actual answer will be accepted.
 

# Example 1:

# Input
# ["MedianFinder", "addNum", "addNum", "findMedian", "addNum", "findMedian"]
# [[], [1], [2], [], [3], []]
# Output
# [null, null, null, 1.5, null, 2.0]

# Explanation
# MedianFinder medianFinder = new MedianFinder();
# medianFinder.addNum(1);    // arr = [1]
# medianFinder.addNum(2);    // arr = [1, 2]
# medianFinder.findMedian(); // return 1.5 (i.e., (1 + 2) / 2)
# medianFinder.addNum(3);    // arr[1, 2, 3]
# medianFinder.findMedian(); // return 2.0


# https://www.youtube.com/watch?v=Yv2jzDzYlp8


class MedianFinder:

    def __init__(self):
        
        # max heap
        self.leftSide = []
        heapify(self.leftSide)
        
        # min heap
        self.rightSide = []
        heapify(self.rightSide)
        

    def addNum(self, num: int) -> None:
        
        if(not self.leftSide or num <= -self.leftSide[0]):
            heappush(self.leftSide,-num)
        else:
            heappush(self.rightSide,num)


        # making sure the balance is correct 
        if(len(self.leftSide) > len(self.rightSide) + 1):
            heappush(self.rightSide,-heappop(self.leftSide))
        elif(len(self.rightSide) > len(self.leftSide)):
            heappush(self.leftSide,-heappop(self.rightSide))
            

    def findMedian(self) -> float:
        
        if(len(self.rightSide) == len(self.leftSide)):
            return (self.rightSide[0] - self.leftSide[0]) / 2
        return - self.leftSide[0]


# at each point we are making sure that size of leftSide is either greater than rightSide by 1 
# or equal to rightSide