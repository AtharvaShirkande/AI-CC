import heapq

def heuristic(a, b): return abs(a[0] - b[0]) + abs(a[1] - b[1])

def astar(grid, start, goal):
    rows, cols = len(grid), len(grid[0])
    open_list = [(heuristic(start, goal), 0, start, [start])]
    visited = set()

    while open_list:
        f, g, curr, path = heapq.heappop(open_list)
        if curr == goal: return path
        if curr in visited: continue
        visited.add(curr)

        for dx, dy in [(0,1), (1,0), (0,-1), (-1,0)]:
            nx, ny = curr[0] + dx, curr[1] + dy
            if 0 <= nx < rows and 0 <= ny < cols and grid[nx][ny] == 0:
                neighbor = (nx, ny)
                if neighbor not in visited:
                    heapq.heappush(open_list, (g+1+heuristic(neighbor, goal), g+1, neighbor, path + [neighbor]))
    return None

# Example usage
grid = [
    [0, 1, 0, 0, 0],
    [0, 1, 0, 1, 0],
    [0, 0, 0, 1, 0],
    [1, 1, 0, 1, 0],
    [0, 0, 0, 0, 0]
]
start, goal = (0, 0), (4, 4)
path = astar(grid, start, goal)
print("Path found:" if path else "No path found.")
if path: print(*path, sep="\n")