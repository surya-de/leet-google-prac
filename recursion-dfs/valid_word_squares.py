class Solution:
    def validWordSquare(self, words: List[str]) -> bool:
        rows = len(words)
        for k in range (rows):
            cols = len(words[k])

            for i in range(cols):
                if  i >= rows or \
                    k >= len(words[i]) or \
                    words[k][i] != words[i][k]:
                    return False
        
        return True