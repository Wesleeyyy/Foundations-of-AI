
# Task Four: Breadth First Search (BFS) & Depth First Search (DFS)

from collections import deque


graph = {
    'A': ['B', 'C'],
    'B': ['D', 'E'],
    'C': ['F'],
    'D': [],
    'E': ['G'],
    'F': [],
    'G': []
}



# BREADTH FIRST SEARCH (BFS)


def bfs(graph, start, goal):
    print("\n========== BREADTH FIRST SEARCH (BFS) ==========")
    print(f"Start Node : {start}")
    print(f"Goal Node  : {goal}")
    print("-------------------------------------------------")

    # Queue stores the current node and the path taken to reach it
    queue = deque()
    queue.append((start, [start]))

    visited = set()  # Track visited nodes to avoid revisiting

    while queue:
        current_node, path = queue.popleft()  # Take from the front

        print(f"Visiting: {current_node}  |  Path so far: {' -> '.join(path)}")

        # Goal check
        if current_node == goal:
            print(f"✔ Goal '{goal}' FOUND!")
            print(f"✔ Final Path: {' -> '.join(path)}")
            print(f"✔ Total steps: {len(path) - 1}")
            return path

        # Mark as visited
        if current_node not in visited:
            visited.add(current_node)

            # Add all unvisited neighbors to the queue
            for neighbor in graph[current_node]:
                if neighbor not in visited:
                    queue.append((neighbor, path + [neighbor]))

    print(f"✘ Goal '{goal}' NOT found.")
    return None


# DEPTH FIRST SEARCH (DFS)
def dfs(graph, start, goal):
    print("\n DEPTH FIRST SEARCH (DFS) ")
    print(f"Start Node : {start}")
    print(f"Goal Node  : {goal}")

    # Stack stores the current node and the path taken to reach it
    stack = []
    stack.append((start, [start]))

    visited = set()  # Track visited nodes to avoid revisiting

    while stack:
        current_node, path = stack.pop()  # Take from the top

        print(f"Visiting: {current_node}  |  Path so far: {' -> '.join(path)}")

        # Goal check
        if current_node == goal:
            print(f"✔ Goal '{goal}' FOUND!")
            print(f"✔ Final Path: {' -> '.join(path)}")
            print(f"✔ Total steps: {len(path) - 1}")
            return path

        # Mark as visited
        if current_node not in visited:
            visited.add(current_node)

            # Add neighbors to stack in REVERSE order so left neighbor is explored first
            for neighbor in reversed(graph[current_node]):
                if neighbor not in visited:
                    stack.append((neighbor, path + [neighbor]))

    print(f"✘ Goal '{goal}' NOT found.")
    return None


#  Run both searches
if __name__ == "__main__":
    start_node = 'A'
    goal_node  = 'G'

    bfs(graph, start_node, goal_node)
    dfs(graph, start_node, goal_node)