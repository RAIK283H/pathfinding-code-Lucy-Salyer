import graph_data

def johnson_trotter(n):
    # Dictionary of numbers (not indices) and true or false True = Left
    directions = {}
    # numbers 1 through n
    permutations = []
    # end result of all different permutations
    diff_permutations = []
    # Set everything to start facing left (True)
    for i in range(1, n - 1):
        directions[i] = True
        permutations.append(i)

    # First permutation is the original list
    diff_permutations.append(permutations.copy())
    
    while True:
        # Get largest mobile info
        largest_mobile_index = mobile_integer(permutations, directions, n)
        largest_mobile_number = permutations[largest_mobile_index]
         # If mobile integer return -1 the function found no more mobile integers
        if largest_mobile_index == -1:
            break

        # Move left and append new permutation
        if(directions[largest_mobile_number] == True):
            permutations = move_left(permutations, largest_mobile_index, largest_mobile_index - 1)
            diff_permutations.append(permutations.copy())
        # Move right and append new permutation
        elif(directions[largest_mobile_number] == False):
            permutations = move_right(permutations, largest_mobile_index, largest_mobile_index + 1)
            diff_permutations.append(permutations.copy())    

        # Change direction of all integers larger than the current mobile one
        for i in permutations:
            if(i > largest_mobile_number):
                directions[i] = not directions[i]
    
    return diff_permutations

def move_left(permutations, permutation, before):
    # Classic swap left  of values in a list
    temp = permutations[before]
    permutations[before] = permutations[permutation]
    permutations[permutation] = temp

    return permutations

def move_right(permutations, permutation, after):
    # Classic swap right of values in a list
    temp = permutations[after]
    permutations[after] = permutations[permutation]
    permutations[permutation] = temp

    return permutations

def mobile_integer(permutations, directions, n):
    # Initialize as -1 so you can tell when no mobiles are found
    largest_mobile_index = -1
    largest_mobile_number = -1

    for index in range(len(permutations)):
        # If left
        if (directions[permutations[index]] is True):
            # Make sure not at a boundary and the one before is less than current
            if((index > 0) and (permutations[index] > permutations[index - 1])):
                # If greater than current largest mobile
                if (permutations[index] > largest_mobile_number):
                    largest_mobile_number = permutations[index]
                    largest_mobile_index = index
        # If right
        elif(directions[permutations[index]] is False):
            #Make sure not at the end of the list and value to right is less than
            if((index < len(permutations) - 1) and (permutations[index] > permutations[index + 1])):
                # If value is larger than current mobile
                if (permutations[index] > largest_mobile_number):
                    largest_mobile_number = permutations[index]
                    largest_mobile_index = index
    return largest_mobile_index

def hamilton_cycle_detector(permutations, graph):
    curr_graph = graph_data.graph_data[graph]

    # Make sure all values are in each others adjacency list
    for i in range(len(permutations) - 1):
        if (permutations[i + 1] not in curr_graph[permutations[i]][1]):
            return False
    if (permutations[0] not in curr_graph[permutations[len(permutations) - 1]][1]):
        return False
    
    return True
    
    
    
