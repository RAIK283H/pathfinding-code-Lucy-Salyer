import graph_data
import global_game_data
from numpy import random

def set_current_graph_paths():
    global_game_data.graph_paths.clear()
    global_game_data.graph_paths.append(get_test_path())
    global_game_data.graph_paths.append(get_random_path())
    global_game_data.graph_paths.append(get_dfs_path())
    global_game_data.graph_paths.append(get_bfs_path())
    global_game_data.graph_paths.append(get_dijkstra_path())


def get_test_path():
    return graph_data.test_path[global_game_data.current_graph_index]


def get_random_path():
    # Get the graph that is being run
    curr_graph = graph_data.graph_data[global_game_data.current_graph_index]
    assert len(curr_graph) >= 2, "The graph is null or not big enough to generate a path"
    # Find the target node
    target = global_game_data.target_node[global_game_data.current_graph_index]
    # find the end node
    end_node = len(curr_graph) - 1
    curr_node = 0
    path = []
    # Find random nodes until target is hit
    while curr_node != target:
        # If target node is in the adjacency list automatically choose it.
        if(target in curr_graph[curr_node][1]):
            next_node = target
            path.append(next_node)
        else:
            # Continue grabbing random nodes from the adjacency list
            next_node = int(random.choice(curr_graph[curr_node][1]))
            path.append(next_node) 
        # We are now on next_node so update curr_node
        curr_node = next_node
    # After hitting the target find the end node
    while curr_node != end_node:
        # If end_node is in the adjacency list choose it. 
        if(end_node in curr_graph[curr_node][1]):
            next_node = end_node
            path.append(next_node)
        else:
            # Keep grabbing random nodes
            next_node = int(random.choice(curr_graph[curr_node][1]))
            path.append(next_node) 
        curr_node = next_node

    assert len(path) >= 0, "No path was generated"
    return path


def get_dfs_path():
    # Get the graph that is being run
    curr_graph = graph_data.graph_data[global_game_data.current_graph_index]
    assert len(curr_graph) >= 2, "The graph is null or not big enough to generate a path"
    # Find the target node
    target = global_game_data.target_node[global_game_data.current_graph_index]
    # find the end node
    end_node = len(curr_graph) - 1
    start_node = global_game_data.current_player_index
    
    path_to_target = build_dfs_path(curr_graph, start_node, target)
    path_to_end = build_dfs_path(curr_graph, target, end_node)
    
    path = path_to_target + path_to_end

    assert target in path, "Target was not in the path DFS"
    assert end_node in path, "End node was not in the path DFS"
    # for i in range(len(path) - 2):
    #     assert path[i + 1] in curr_graph[path[i]][1], "Not all the paths are connected with an edge DFS"
    return path

def build_dfs_path(graph, start_node, end_node):
    path = []
    # Queue for cells that have not been explored
    frontier = []
    frontier.append(start_node)

    # Set to hold visited nodes
    visited = set()
    visited.add(start_node)

    # Map of parents
    parents = {}
    parents[start_node] = False

    # Depth First Search for target
    while frontier:
        # Get next element in the list
        current = frontier.pop()

        # Break when the target is found
        if (current == end_node):
            break

        # Add neighbors to be searched
        neighbors = graph[current][1]
        for neighbor in neighbors:
            if neighbor not in visited:
                visited.add(neighbor)
                parents[neighbor] = current
                frontier.append(neighbor)
    
    while current is not False:
        path.insert(0, current)
        current = parents[current]

    return path


def get_bfs_path():
   # Get the graph that is being run
    curr_graph = graph_data.graph_data[global_game_data.current_graph_index]
    assert len(curr_graph) >= 2, "The graph is null or not big enough to generate a path"
    # Find the target node
    target = global_game_data.target_node[global_game_data.current_graph_index]
    # find the end node
    end_node = len(curr_graph) - 1
    start_node = global_game_data.current_player_index
    
    path_to_target = build_bfs_path(curr_graph, start_node, target)
    path_to_end = build_bfs_path(curr_graph, target, end_node)
    
    path = path_to_target + path_to_end

    assert target in path, "Target was not in the path BFS"
    assert end_node in path, "End node was not in the path BFS"
    # for i in range(len(path) - 1):
    #     assert path[i + 1] in curr_graph[path[i]][1], "Not all the paths are connected with a node BFS"

    return path

def build_bfs_path(graph, start_node, end_node):
    path = []

    # Queue for cells that have not been explored
    frontier = []
    frontier.append(start_node)

    # Set to hold visited nodes
    visited = set()
    visited.add(start_node)

    # Map of parents
    parents = {}
    parents[start_node] = False

    # Breadth First Search for target
    while frontier:
        # Get next element in the list
        current = frontier.pop(0)

        # Break when the target is found
        if (current == end_node):
            break

        # Add neighbors to be searched
        neighbors = graph[current][1]
        for neighbor in neighbors:
            if neighbor not in visited:
                visited.add(neighbor)
                parents[neighbor] = current
                frontier.append(neighbor)
    
    while current is not False:
        path.insert(0, current)
        current = parents[current]

    return path

def get_dijkstra_path():
    return [1,2]
