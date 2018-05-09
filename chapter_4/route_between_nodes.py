from Graph import Graph
from collections import deque

def breadth_first_search(G, start, end):
    queue = deque() # using append() and popleft()
    visited = [] # list of visited nodes

    # add to visited / add to queue
    visited.append(start)
    queue.append(start)

    edges = G.return_edges("a")

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
