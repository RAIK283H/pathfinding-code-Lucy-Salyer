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
            next_node = random.choice(curr_graph[curr_node][1])
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
            next_node = random.choice(curr_graph[curr_node][1])
            path.append(next_node) 
        curr_node = next_node

    assert len(path) >= 0, "No path was generated"
    return path


def get_dfs_path():
    return [1,2]


def get_bfs_path():
    return [1,2]


def get_dijkstra_path():
    return [1,2]
