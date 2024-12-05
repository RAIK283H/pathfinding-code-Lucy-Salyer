import graph_data
import global_game_data
from numpy import random
import sys
import heapq as heap
import math
import f_w


def set_current_graph_paths():
    global_game_data.graph_paths.clear()
    global_game_data.graph_paths.append(get_test_path())
    global_game_data.graph_paths.append(get_random_path())
    global_game_data.graph_paths.append(get_dfs_path())
    global_game_data.graph_paths.append(get_bfs_path())
    #global_game_data.graph_paths.append(get_dijkstra_path())
    global_game_data.graph_paths.append(f_w.get_floyd_warshall())


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
    path_to_end.pop(0)
    
    path = path_to_target + path_to_end


    assert target in path, "Target was not in the path DFS"
    assert end_node in path, "End node was not in the path DFS"
    assert validate_path(curr_graph, path), "Path is not valid because nodes are not connected by edges DFS"

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
    path_to_end.pop(0)
    
    path = path_to_target + path_to_end

    assert target in path, "Target was not in the path BFS"
    assert end_node in path, "End node was not in the path BFS"   
    assert validate_path(curr_graph, path), "Path is not valid because nodes are not connected by edges BFS"


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
   # Get the graph that is being run
    curr_graph = graph_data.graph_data[global_game_data.current_graph_index]
    assert len(curr_graph) >= 2, "The graph is null or not big enough to generate a path"
    # Find the target node
    target = Node(global_game_data.target_node[global_game_data.current_graph_index])
    # find the end node
    end_node = Node(len(curr_graph) - 1)
    start_node = Node(0)

    path_to_target = build_dijkstra(start_node, target, curr_graph)
    path_to_end = build_dijkstra(target, end_node, curr_graph)
    # Both add the target node so you need to cut one out
    path_to_end.pop(0)

    path = path_to_target + path_to_end

    assert start_node.node_number == path[0], "Start node was not in the path Dijkstra"
    assert end_node.node_number == path[len(path) - 1], "End node was not in the path Dijkstra"
    assert validate_path(curr_graph, path), "Path is not valid because nodes are not connected by edges Dijkstra"

    return path


def build_dijkstra(start_node, end_node, graph):
    path = []
    
    # Create a heap to hold priorities
    frontier = []
    heap.heapify(frontier)
    heap.heappush(frontier, (start_node.priority, start_node))

    # Create a set to hold who is visited
    visited = set()
    visited.add(start_node)

    # A map to hold parents
    parents = {}
    parents[start_node] = False

    curr_dist = 0

    while frontier:
        # Get first node
        current = heap.heappop(frontier)[1]

        # If you are at the searched for node break
        if(current.node_number == end_node.node_number): 
            break

        # Add neighbors to be searched
        neighbors = graph[current.node_number][1]
        for neighbor in neighbors:
            # Make each node apart of the node class to hold a priority
            node = Node(neighbor)
            if node not in visited:
                visited.add(node)
                parents[node] = current
                # Use pythagorean theorem to calculate distance
                node.priority = curr_dist + math.sqrt(math.pow(graph[current.node_number][0][0] - graph[node.node_number][0][0], 2) 
                + math.pow(graph[current.node_number][0][1] - graph[node.node_number][0][1], 2))
                heap.heappush(frontier, (node.priority, node))

    # Build path backward
    while current is not False:
        path.insert(0, current.node_number)
        current = parents[current]

    return path

def validate_path(graph, path):
    is_valid = False
    for index, node in enumerate(path):
        if(index != len(path)-1):
            is_valid = path[index+1] in graph[node][1]
            if(is_valid == False):
                return False
    return is_valid


class Node:
    def __init__(self, node_number):
        self.node_number = node_number
        self.priority = sys.maxsize

    # custom comparator needed for breaking ties in heapq
    def __lt__(self, other):  
        return self.priority < other.priority
    
    def __hash__(self):
        return hash(self.node_number)

    def __eq__(self, other):
        return isinstance(other, Node) and self.node_number == other.node_number

