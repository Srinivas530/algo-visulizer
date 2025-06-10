import time
import matplotlib.pyplot as plt
from collections import deque
import heapq

def draw_grid(grid_size, start, end, visited, path, container):
    fig, ax = plt.subplots(figsize=(10, 10))  # Bigger figure
    for i in range(grid_size):
        for j in range(grid_size):
            color = 'white'
            if (i, j) in visited:
                color = 'purple'
            if (i, j) in path:
                color = 'yellow'
            if (i, j) == start:
                color = 'orange'
            elif (i, j) == end:
                color = 'green'
            rect = plt.Rectangle((j, i), 1, 1, facecolor=color, edgecolor='black')
            ax.add_patch(rect)
    ax.set_xlim(0, grid_size)
    ax.set_ylim(0, grid_size)
    ax.set_xticks(range(grid_size + 1))
    ax.set_yticks(range(grid_size + 1))
    ax.grid(True)
    ax.set_xticklabels([])
    ax.set_yticklabels([])
    container.pyplot(fig)

def bfs(grid_size, start, end, speed, container):
    visited = set()
    parent = {}
    q = deque([start])
    visited.add(start)

    while q:
        x, y = q.popleft()
        if (x, y) == end:
            break
        draw_grid(grid_size, start, end, visited, [], container)
        time.sleep(speed)
        for dx, dy in [(-1,0),(1,0),(0,-1),(0,1)]:
            nx, ny = x + dx, y + dy
            if 0 <= nx < grid_size and 0 <= ny < grid_size:
                if (nx, ny) not in visited:
                    visited.add((nx, ny))
                    parent[(nx, ny)] = (x, y)
                    q.append((nx, ny))

    # Reconstruct path
    path = []
    node = end
    while node in parent:
        path.append(node)
        node = parent[node]
    path.append(start)
    path.reverse()

    draw_grid(grid_size, start, end, visited, path, container)

def dfs(grid_size, start, end, speed, container):
    visited = set()
    parent = {}
    found = False

    def _dfs(x, y):
        nonlocal found
        if not (0 <= x < grid_size and 0 <= y < grid_size):
            return
        if (x, y) in visited or found:
            return
        visited.add((x, y))
        draw_grid(grid_size, start, end, visited, [], container)
        time.sleep(speed)
        if (x, y) == end:
            found = True
            return
        for dx, dy in [(-1,0),(1,0),(0,-1),(0,1)]:
            _dfs(x + dx, y + dy)
            if found:
                parent[(x + dx, y + dy)] = (x, y)
                return

    _dfs(*start)

    # Reconstruct path
    path = []
    node = end
    while node in parent:
        path.append(node)
        node = parent[node]
    path.append(start)
    path.reverse()

    draw_grid(grid_size, start, end, visited, path, container)

def dijkstra(grid_size, start, end, speed, container):
    visited = set()
    dist = [[float('inf')]*grid_size for _ in range(grid_size)]
    parent = {}
    dist[start[0]][start[1]] = 0
    pq = [(0, start)]

    while pq:
        d, (x, y) = heapq.heappop(pq)
        if (x, y) in visited:
            continue
        visited.add((x, y))
        draw_grid(grid_size, start, end, visited, [], container)
        time.sleep(speed)
        if (x, y) == end:
            break
        for dx, dy in [(-1,0),(1,0),(0,-1),(0,1)]:
            nx, ny = x + dx, y + dy
            if 0 <= nx < grid_size and 0 <= ny < grid_size:
                new_dist = dist[x][y] + 1
                if new_dist < dist[nx][ny]:
                    dist[nx][ny] = new_dist
                    parent[(nx, ny)] = (x, y)
                    heapq.heappush(pq, (new_dist, (nx, ny)))

    # Reconstruct path
    path = []
    node = end
    while node in parent:
        path.append(node)
        node = parent[node]
    path.append(start)
    path.reverse()

    draw_grid(grid_size, start, end, visited, path, container)