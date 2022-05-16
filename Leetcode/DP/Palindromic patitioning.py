from sys import stdin, setrecursionlimit
import sys
setrecursionlimit(10**6)


def palindromePartitioning(string):
	t = [[sys.maxsize for i in range(len(string)+1)] for j in range(len(string)+1)]
	def palindromicPartition(string):
		return solve(string,0,len(string))
	def solve(s,i,j):
		if(ispal(s[i:j])):
			return 0
		if(i>=j):
			return 0
		if(t[i][j] != sys.maxsize):
			return t[i][j]
		for k in range(i+1,j):
			if(t[i][k] == sys.maxsize):
				t[i][k] = solve(s,i,k)
			if(t[k][j] == sys.maxsize):
				t[k][j] = solve(s,k,j)
			temp = 1 + t[i][k] + t[k][j]
			t[i][j] = min(temp,t[i][j])
		return t[i][j]
	def ispal(s):
		if(s==s[::-1]):
			return True
		return False
	return palindromicPartition(string)
t = int(input())
while t:
    string = list(map(str, input()))
    while(" " in string):
        string.remove(" ")
    print(palindromePartitioning(string))
    t = t-1
