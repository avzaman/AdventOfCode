# need a normalized cuts algorithm
import cudf
import cugraph

graph = {}
for line in open("input25.txt"):
    graph[line.split(":")[0].strip()] = line.split(":")[1].strip().split(" ")
gadd = {}
for k,v in graph.items():
    for wire in v:
        if wire in graph:
            graph[wire].append(k)
        elif wire in gadd:
            gadd[wire].append(k)
        else:
            gadd[wire] = [k]
graph.update(gadd)

#print(graph)

#G = nx.DiGraph(graph)

# Check if the graph is strongly connected
#is_connected = nx.is_strongly_connected(G)

#print("Is the graph strongly connected?", is_connected)

def generate_two_clusters(graph):
    # Convert the graph dictionary to a cuGraph DataFrame
    edges_list = [(src, dest) for src, dest_list in graph.items() for dest in dest_list]
    edges_df = cudf.DataFrame(edges_list, columns=['src', 'dest'])

    # Create a cuGraph graph
    G = cugraph.Graph()
    G.from_cudf_edgelist(edges_df, source='src', destination='dest')

    # Find a 3-edge cut (k-truss subgraph with k=2)
    k = 2
    ktruss_subgraph = cugraph.ktruss_subgraph(G, k)

    # Extract two clusters based on the result
    cluster1 = ktruss_subgraph['src'].to_pandas()
    cluster2 = ktruss_subgraph['dst'].to_pandas()

    return cluster1, cluster2

try:
    cluster1, cluster2 = generate_two_clusters(graph)
    print("Cluster 1:", cluster1, "Size: ",len(cluster1))
    print("Cluster 2:", cluster2, "Size: ",len(cluster2))
except ValueError as e:
    print(e)

print(len(cluster1)*len(cluster2))

# tried a handfull of approaches to accelerate using gpu but that is currently beyond me,
# ended up installing conda to make an environment of packages that communicated with CUDA drivers for my GPU
# well that was the goal in theory, couldn't get the damn graph packages installed
# might be my python version is too new, might be not supported on windows, idk
# im calling it here for now, GG merry Christmas