import graph_data
import global_game_data
import permutations
import math

def main():
    # Get the graph index
    graph_index = 1
    curr_graph = graph_data.graph_data[graph_index]
    # If you change this to test numbers valid_cycles will not work unless lined up with a valid graph
    permutation = permutations.johnson_trotter(len(curr_graph))
    valid_cycles = []
    # Get all permutations that complete a cycle
    for item in permutation:
        if(permutations.hamilton_cycle_detector(item, graph_index)):
            item.append(item[0])
            valid_cycles.append(item)
        else:
            valid_cycles.append(-1)
    # print result 
    print("Graph: " + str(graph_index) + " Valid cycles: " + str(valid_cycles))
       

main()