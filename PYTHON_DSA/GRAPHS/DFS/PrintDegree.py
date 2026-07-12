graph = [
    [1,2],
    [0,3],
    [0,4],
    [1],
    [2]
]

for vertex in range(len(graph)):
    degree = len(graph[vertex])
    # print(f"Vertex {vertex} -> Degree {degree}")
    print("Vertex",vertex,"-> Degree",degree)