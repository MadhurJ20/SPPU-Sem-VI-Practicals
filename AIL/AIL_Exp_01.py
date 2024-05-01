'''
Madhur Jaripatke
Roll No. 48
TE A Computer
RMDSSOE, Warje, Pune
'''
'''
Implement depth first search algorithm and Breadth First Search algorithm, Use an undirected
graph and develop a recursive algorithm for searching all the vertices of a graph or tree data
structure.
'''
def dfs(visited, graph, node):
    if node not in visited:
        print(node, end=" ")
        visited.add(node)
        for neighbour in graph[node]:
            dfs(visited, graph, neighbour)


def bfs(visited, graph, node, queue):
    visited.add(node)
    queue.append(node)

    while queue:
        s = queue.pop(0)
        print(s, end=" ")
        for neighbour in graph[s]:
            if neighbour not in visited:
                visited.add(neighbour)
                queue.append(neighbour)


def main():
    visited1 = set()  # TO keep track of DFS visited nodes
    visited2 = set()  # TO keep track of BFS visited nodes
    queue = []  # For BFS
    n = int(input("Enter number of nodes : "))
    graph = dict()

    for i in range(1, n + 1):
        edges = int(input("Enter number of edges for node {} : ".format(i)))
        graph[i] = list()
        for j in range(1, edges + 1):
            node = int(input("Enter edge {} for node {} : ".format(j, i)))
            graph[i].append(node)

    print("DFS: ", end="")
    dfs(visited1, graph, 1)
    print()
    print("BFS: ", end="")
    bfs(visited2, graph, 1, queue)


if __name__ == "__main__":
    main()

    # graph = {
    #     '1' : ['2','3'],
    #     '2' : ['4', '5'],
    #     '3' : ['6','7'],
    #     '4' : [],
    #     '5' : [],
    #     '6' : [],
    #     '7' : []
    #     DFS : 1 2 4 5 3 6 7 
    #     BFS : 1 2 3 4 5 6 7 
    # }
