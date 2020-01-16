# Trying out things I learned from 영조형
# https://leetcode.com/problems/rotting-oranges/
from collections import deque

def oranges_rotting(self, grid: List[List[int]]) -> int:
    rotten_oranges = deque()
    total_orange_count = 0
    
    for r, row in enumerate(grid):
        for c, value in enumerate(row):
            if value == 2:
                rotten_oranges.append((r, c, 0))
            if value == 1:
                total_orange_count += 1
        
    timestamp = 0

    while rotten_oranges:
        r, c, timestamp = rotten_oranges.popleft()

        for next_r, next_c in (
            (r+1, c),
            (r-1, c),
            (r, c+1),
            (r, c-1)
        ):
            if (
                0<=next_r<len(grid) and
                0<=next_c<len(grid[0]) and
                grid[next_r][next_c] == 1
            ):
                grid[next_r][next_c] = 2
                total_orange_count -= 1
                rotten_oranges.append((next_r, next_c, timestamp + 1))
            
    return timestamp if not total_orange_count else -1
