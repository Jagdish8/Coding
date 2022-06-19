# Design a map that allows you to do the following:

# Maps a string key to a given value.
# Returns the sum of the values that have a key with a prefix equal to a given string.
# Implement the MapSum class:

# MapSum() Initializes the MapSum object.
# void insert(String key, int val) Inserts the key-val pair into the map. If the key already existed, the original key-value pair will be overridden to the new one.
# int sum(string prefix) Returns the sum of all the pairs' value whose key starts with the prefix.
 

# Example 1:

# Input
# ["MapSum", "insert", "sum", "insert", "sum"]
# [[], ["apple", 3], ["ap"], ["app", 2], ["ap"]]
# Output
# [null, null, 3, null, 5]

# Explanation
# MapSum mapSum = new MapSum();
# mapSum.insert("apple", 3);  
# mapSum.sum("ap");           // return 3 (apple = 3)
# mapSum.insert("app", 2);    
# mapSum.sum("ap");           // return 5 (apple + app = 3 + 2 = 5)


class MapSum(object):

    def __init__(self):
        self.root = {}
        
    def insert(self, key, val):
        root = self.root
        for w in key:
            if w not in root:
                root[w] = {}
            root = root[w]
        root["-"] = val
        print(self.root)
        
    def get_siblings(self,prefix):
        root = self.root
        for w in prefix:
            if w not in root:
                return None
            root = root[w]
        return root
    
    def get_sum(self,root):
        cost = 0
        for w in root:
            if w == "-":
                cost+=root[w]
                continue
            cost+=self.get_sum(root[w])
        return cost
    
    def sum(self, prefix):
        root = self.get_siblings(prefix)
        print(prefix,root)
        if root: 
            return self.get_sum(root)
        return 0

# Your MapSum object will be instantiated and called as such:
# obj = MapSum()
# obj.insert(key,val)
# param_2 = obj.sum(prefix)




# for inserting:

# apple,3

# {'a': {'p': {'p': {'l': {'e': {'-': 3}}}}}}


# for getting sum for "ap"
# find the sibling of p(last element of key)
# it would return p(second p in apple)
# now starting from from p check whether "-" exists then add in the sum will last 
# till last there is no "-" in between 
# therefore sum is 3


# for inserting app,2

# {'a': {'p': {'p': {'l': {'e': {'-': 3}}, '-': 2}}}}

# for inserting apple,2
# # replace value if exists with new value

# {'a': {'p': {'p': {'l': {'e': {'-': 2}}, '-': 2}}}}


# for getting sum for "ap"
# find the sibling of p(last element of key)
# it would return p(second p in apple)
# now starting from from p check whether "-" exists then add in the sum will last 
# for p "-" is there, so add in the s = 2
# now move till last to check "-"
# at last s += 2 = 4
