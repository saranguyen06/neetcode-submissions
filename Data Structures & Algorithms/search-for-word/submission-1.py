class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        ROWS, COLS = len(board), len(board[0])
        path = set() #prevent revisiting a cell in board

        def dfs(r, c, i): #i = index of current character in target
            if i == len(word): #all chars matched -> found word
                return True
            #if out of bounds, mismatch, or already visited -> False
            if (r < 0 or c < 0 or r >= ROWS or c >= COLS or
                word[i] != board[r][c] or
                (r, c) in path):
                return False

            path.add((r, c)) #mark visited
            #visit 4 neighbors
            res = (dfs(r + 1, c, i + 1) or
                    dfs(r - 1, c, i + 1) or
                    dfs(r, c + 1, i + 1) or
                    dfs(r, c - 1, i + 1))
            path.remove((r, c)) #backtrack
            return res
        
        for r in range(ROWS): #attempt to start matching word from each cell
            for c in range(COLS):
                #if any cell returns True, answer is True
                if dfs(r, c, 0): return True 
        return False #if we go through whole board and dfs never returns True
        