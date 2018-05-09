from Graph import Graph
from collections import deque

def depth_first_search(G, vert, end, visited):
    if not vert:
        return None

    if vert == end:
        return True

    visited.append(vert)
    adjacent = G.return_edges(vert)

    for vert in adjacent:
        if vert not in visited:
            return depth_first_search(G, vert, end, visited)

    print(vert)
    return False

def dfs_util(G, start, end):
    visited = []
    return depth_first_search(G, start, end, visited)


def breadth_first_search(G, start, end):
    queue = deque() # using append() and popleft()
    visited = [] # list of visited nodes

    # add to visited / add to queue
    visited.append(start)
    queue.append(start)


    while queue:
        vert = queue.popleft()
        visited.append(vert)

        if vert == end:
            return True

        # search adjacent
        vert_edges = G.return_edges(vert)
        for vert in vert_edges:
            # if not visited then add to queue
            if vert not in visited:
                queue.append(vert)


    return False


if __name__ == "__main__":

    # go a -> c
    g = { "a" : ["d"],
          "b" : ["c"],
          "c" : ["b", "c", "d", "e"],
          "d" : ["a", "c"],
          "e" : ["c"],
          "f" : []
        }

    G = Graph(g)

    is_path = breadth_first_search(G, "a", "c")
    print(is_path)

    print("*****")

    bfs_is_path = dfs_util(G, "a", "c")
    print(bfs_is_path)
