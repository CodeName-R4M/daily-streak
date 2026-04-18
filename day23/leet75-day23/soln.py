from collections import Counter
from typing import List

class Solution:
    def equalPairs(self, grid: List[List[int]]) -> int:
        row_count = Counter(tuple(row) for row in grid)
        
        count = 0
        n = len(grid)
        
        for c in range(n):
            col = tuple(grid[r][c] for r in range(n))
            count += row_count[col]
        
        return count