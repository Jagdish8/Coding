# Given two version numbers, version1 and version2, compare them.

# Version numbers consist of one or more revisions joined by a dot '.'. Each revision consists of digits and may contain leading zeros. Every revision contains at least one character. Revisions are 0-indexed from left to right, with the leftmost revision being revision 0, the next revision being revision 1, and so on. For example 2.5.33 and 0.1 are valid version numbers.

# To compare version numbers, compare their revisions in left-to-right order. Revisions are compared using their integer value ignoring any leading zeros. This means that revisions 1 and 001 are considered equal. If a version number does not specify a revision at an index, then treat the revision as 0. For example, version 1.0 is less than version 1.1 because their revision 0s are the same, but their revision 1s are 0 and 1 respectively, and 0 < 1.

# Return the following:

# If version1 < version2, return -1.
# If version1 > version2, return 1.
# Otherwise, return 0.
 

# Example 1:

# Input: version1 = "1.01", version2 = "1.001"
# Output: 0
# Explanation: Ignoring leading zeroes, both "01" and "001" represent the same integer "1".
# Example 2:

# Input: version1 = "1.0", version2 = "1.0.0"
# Output: 0
# Explanation: version1 does not specify revision 2, which means it is treated as "0".
# Example 3:

# Input: version1 = "0.1", version2 = "1.1"
# Output: -1
# Explanation: version1's revision 0 is "0", while version2's revision 0 is "1". 0 < 1, so version1 < version2.


class Solution:
    def compareVersion(self, version1: str, version2: str) -> int:
        one = version1.split(".")
        for i,j in enumerate(one):
            one[i] = int(j)
        two = version2.split(".")
        for i,j in enumerate(two):
            two[i] = int(j)
        # print(one,two)
        i = 0
        while(i<len(one) and i<len(two)):
            if(one[i] == two[i]):
                i += 1
            elif(one[i] > two[i]):
                return 1
            else:
                return -1
        # print(i)
        if(i<len(one)):
            while(i<len(one) and one[i] == 0):
                i += 1
            if(i<len(one)):
                return 1
        if(i<len(two)):
            while(i<len(two) and two[i] == 0):
                i += 1
            if(i<len(two)):
                return -1
        return 0
        
        
# ok