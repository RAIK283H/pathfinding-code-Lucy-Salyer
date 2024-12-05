import math
import graph_data
import global_game_data

def adjacency_matrix(curr_graph):
    # Length of the graph
    num_vertices = len(curr_graph)
    # build a matrix as big as the graph vertically and horizontally
    adj_matrix = [[math.inf] * num_vertices for _ in range(num_vertices)]

    for i in range(num_vertices):
        for neighbor in curr_graph[i][1]:
            # Calculate the distance for each neighbor
            adj_matrix[i][neighbor] = dist_calc(i, neighbor, curr_graph)

    return adj_matrix


def Floyd_Warshall_Algorithm(curr_graph):
    adj_matrix = adjacency_matrix(curr_graph)
    num_vertices = len(curr_graph)
    # Create a parent matrix to track each parent
    parent_matrix = [[None] * num_vertices for i in range(num_vertices)]

    for i, node in enumerate(curr_graph):
        # If you are comparing a node to itself the distance is 0
        adj_matrix[i][i] = 0
        parent_matrix[i][i] = i
        for neighbor in node[1]:
            parent_matrix[i][neighbor] = i


    for k in range(len(adj_matrix)):
        for i in range(len(adj_matrix)):
            for j in range(len(adj_matrix)):
                # Compare if the distances added together are smaller than current held distance
                if(adj_matrix[i][k] + adj_matrix[k][j] < adj_matrix[i][j]):
                    # set shorter distance as new distance
                    adj_matrix[i][j] = adj_matrix[i][k] + adj_matrix[k][j]
                    # k is the parent of the current node
                    parent_matrix[i][j] = parent_matrix[k][j]
    
    return parent_matrix

def build_path(i, j, graph):
    parent_matrix = Floyd_Warshall_Algorithm(graph)
    # build path backwards
    if parent_matrix[i][j] is None:
        return []
    path = [j]
    while (i != j):
        j = parent_matrix[i][j]
        path.insert(0, j)
    return path

def get_floyd_warshall():
    # get graph
    curr_graph = graph_data.graph_data[global_game_data.current_graph_index]

    assert len(curr_graph) >= 2, "The graph is null or not big enough to generate a path"
    # Find the target node
    target = global_game_data.target_node[global_game_data.current_graph_index]
    # find the end node
    end_node = len(curr_graph) - 1
    # Find start node
    start_node = global_game_data.current_player_index

    # Get first path to target
    path_to_target = build_path(start_node, target, curr_graph)

    # Find second path to end
    path_to_end = build_path(target, end_node, curr_graph)
    # Take the target off the path so it is not input twice
    path_to_end.pop(0)
    # Combine the paths
    path = path_to_target + path_to_end

    assert start_node == path[0], "Start node was not in the path Floyd-Warshall"
    assert end_node == path[len(path) - 1], "End node was not in the path Floyd-Warshall"
    return path
    
def dist_calc(node_one, node_two, graph):
    # Euclidean distance
    return math.sqrt(math.pow(graph[node_one][0][0] - graph[node_two][0][0], 2) 
                + math.pow(graph[node_one][0][1] - graph[node_two][0][1], 2))

