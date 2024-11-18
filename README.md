# Pathfinding Starter Code
My random path gets all of the important nodes like target, current, and end. I also creat an array to hold the nodes to visit in order. I then go into a loop until target has been visited. In that loop I grab random nodes from the curr_node adjacency list. I do not account for if the node chosen has already been visited or not so nodes can be visited multiple times and can return to the start. When the target node is in the adjacency list that node will be automatically chosen. After target is visited the code goes into another while loop until end_node is visited. This works the same way as the target node. 

I added a statistic that tracks how many nodes are visited each run through a graph. This is implemented in scoreboard.py and player_object.py. 

# I did the extra credit homework 6!
I used a heap in Dijkstra's
