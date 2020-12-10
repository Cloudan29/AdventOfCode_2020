inp_file = open('inputs/day10.txt')
adapters = []
for line in inp_file:
    adapters.append(int(line))

adapters.append(0)
adapters.sort()
adapters.append(adapters[-1] + 3)


class Graph:
    def __init__(self):
        self.adj_list = []

    def add_edge(self, from_vertex, to_vertex):
        self.adj_list[from_vertex].append(to_vertex)
    
    def add_vertex(self, vertex):
        self.adj_list.append(vertex)

    def count_paths(self, source, destination):
        visited = [False] * len(self.adj_list)

        path_count = [0]
        self.count_paths_util(source, destination, visited, path_count)
        return path_count[0]

    def count_paths_util(self, current_vertex, destination, visited, path_count):
        visited[current_vertex] = True
      
        if current_vertex == destination:
            path_count[0] += 1
        else:
            i = 0
            while i < len(self.adj_list[current_vertex]): 
                if not visited[self.adj_list[current_vertex][i]]:  
                    self.count_paths_util(self.adj_list[current_vertex][i], destination, visited, path_count)
                i += 1
      
        visited[current_vertex] = False

    def __repr__(self):
        return str(self.adj_list)

    def __str__(self):
        return str(self.adj_list)


def part1():
    diffs = [0, 0, 0]

    for i in range(1, len(adapters)):
        diffs[adapters[i] - adapters[i-1] - 1] += 1

    return diffs[0] * diffs[2]



def part2():
    graph = Graph()
    current_vertex = 0
    for i in range(len(adapters)):
        new_edges = []
        for j in range(1,4):
            if i+j < len(adapters) and adapters[i+j] - adapters[i] <= 3:
                new_edges.append(current_vertex+j)

        if len(new_edges) == 1 and (len(graph.adj_list) == 0 or len(graph.adj_list[-1]) == 1):
            continue
        else:
            graph.add_vertex(new_edges)
            current_vertex += 1

    return graph.count_paths(0, len(graph.adj_list) - 1)


print (part1())
print (part2())