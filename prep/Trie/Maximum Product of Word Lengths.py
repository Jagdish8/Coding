# https://leetcode.com/problems/maximum-product-of-word-lengths/

# https://leetcode.com/problems/maximum-product-of-word-lengths/discuss/2088561/What-about-a-trie

class Solution:
    def maxProduct(self, words: List[str]) -> int:
        n = len(words)
        best = 0
        trie = {}

        # Build a trie
		# O(N * U * logU) where U is the number of unique letters (at most 26), simplified to O(N)
        
        for word in words:
            letters = sorted(set(word))
            temp = trie
            for i in letters:
                if(i not in temp):
                    temp[i] = {}
                temp = temp[i]
            # temp[None] = len(word)
            if(None in temp):
                temp[None] = max(temp[None], len(word))
            else:
                temp[None] = len(word)
            
        print(trie)

        # Loop through each word
		# O(N)
        for word in words:
            
            letters = set(word)
            word_len = len(word)

            # With BFS find the longest word inside the trie that does not have any common letters with current word
			# O(2^26 - 1) => O(1)
            queue = [trie]

            while queue:
                node = queue.pop(0)

                if None in node:
                    best = max(best, node[None] * word_len)

                # Explore the neighbors
                for char in node.keys():
                    if char is not None and char not in letters:
                        queue.append(node[char])

        return best