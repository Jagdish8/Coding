# Suppose you are at a party with n people labeled from 0 to n - 1 and among them, there may exist one celebrity. The definition of a celebrity is that all the other n - 1 people know the celebrity, but the celebrity does not know any of them.

# Now you want to find out who the celebrity is or verify that there is not one. The only thing you are allowed to do is ask questions like: "Hi, A. Do you know B?" to get information about whether A knows B. You need to find out the celebrity (or verify there is not one) by asking as few questions as possible (in the asymptotic sense).

# You are given a helper function bool knows(a, b) that tells you whether A knows B. Implement a function int findCelebrity(n). There will be exactly one celebrity if they are at the party.

# Return the celebrity's label if there is a celebrity at the party. If there is no celebrity, return -1.

 

# Example 1:


# Input: graph = [[1,1,0],[0,1,0],[1,1,1]]
# Output: 1
# Explanation: There are three persons labeled with 0, 1 and 2. graph[i][j] = 1 means person i knows person j, otherwise graph[i][j] = 0 means person i does not know person j. The celebrity is the person labeled as 1 because both 0 and 2 know him but 1 does not know anybody.
# Example 2:


# Input: graph = [[1,0,1],[1,1,0],[0,1,1]]
# Output: -1
# Explanation: There is no celebrity.
 

# Constraints:

# n == graph.length == graph[i].length
# 2 <= n <= 100
# graph[i][j] is 0 or 1.
# graph[i][i] == 1
 

# Follow up: If the maximum number of allowed calls to the API knows is 3 * n, could you find a solution without exceeding the maximum number of calls?

# can be easily using O(n**2)
# greedy approach to O(n)
# elimination approach

# lets suppose 
# 0 --> 1
# 0 --> 2
# 0 --> 3
# 1 --> 0
# 1 --> 2
# 3 --> 0
# 3 --> 1
# 3 --> 2

# inside stack -- >      [0,1,2,3]  (all candidates)
# pop last 2 from the stack
# a = 2
# b = 3
# check know(2,3) --> False
# therefore, 3 can't be the candidate
# push 2 back to the stack

# inside stack --> [0,1,2]
# a = 1
# b = 2
# know(1,2)  -- > True
# therefore 1 can't be the candidate
# push 2 back


# inside stack --> [0,2]
# know(0,2) -- > True
# 0 can't be the candidate
# push 2 back 

# inside stack --> [2]
# Now check whether 2 is known by everyone and 2 doesn't know anyone

# 1st case: 
#     2 is known by everyone:
#     know(0,2) : True
#     know(1,2) : True
#     know(3,2) : True

# 2nd case:
#     2 doesn't know anyone:
#     know(2,0) : False
#     know(2,1) : False
#     know(2,3) : False

# Since both case are satisfying we can say 2 is the celebrity

# The knows API is already defined for you.
# return a bool, whether a knows b
# def knows(a: int, b: int) -> bool:

class Solution:
    def findCelebrity(self, n: int) -> int:
        possible_celeb = 0
        for i in range(1,n):
            if(knows(possible_celeb,i)):
                possible_celeb = i
        # print(possible_celeb)
        for i in range(n):
            if(i == possible_celeb):
                continue
            else:
                if(knows(possible_celeb,i)):
                    return -1
                if(not knows(i,possible_celeb)):
                    return -1
        return possible_celeb
        