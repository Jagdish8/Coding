# Given a nested list of integers, return the sum of all integers in the list weighted by their depth.

# Each element is either an integer, or a list -- whose elements may also be integers or other lists.

# Different from the previous question where weight is increasing from root to leaf, now the weight is defined from bottom up. i.e., the leaf level integers have weight 1, and the root level integers have the largest weight.

# Example 1: Given the list [[1,1],2,[1,1]], return 8. (four 1's at depth 1, one 2 at depth 2)

# Example 2: Given the list [1,[4,[6]]], return 17. (one 1 at depth 3, one 4 at depth 2, and one 6 at depth 1; 13 + 42 + 6*1 = 17)

l =  [1,2,[3,[5],7]]
h={}
st = []
for i in str(l):
    if(i == ',' or i == ' '):
        continue
    elif(i == '['):
        st.append(i)
    elif(i == ']'):
        st.pop()
    else:
        if(len(st) not in h.keys()):
            h[len(st)] = [i]
        else:
            h[len(st)].append(i)
s=0
print(h)
for i in h.keys():
    for j in h[i]:
        s = s + (len(h)-i+1)*int(j)
print(s)