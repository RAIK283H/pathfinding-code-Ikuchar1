# Pathfinding Starter Code


Derived Requirements
    
    - The Random Player will a randomly assigned path which:
        Starts at the start node
        Ends at the exit node
        Includes the target node as part of the path
    
    - The path shall be a valid traversal such that each sequential pair of nodes in the path are connected by an edge.

    - The player will not be able to go to exit node before they reach the target node

    - Add statistic to each player to show how many nodes the player visits before it reaches the exit node

    - Add tests to make sure there is a start, end, and target node in graph before it begins to search

    - Add tests to ensure the player stops at the end node

    - Add tests to ensure that it reaches the target node at some point during the player's turn

Random Walk
    My walk algorithm looks at all neighbors connected to the node and randomly picks one. It can go to each cell no matter if it is the exit or start node. But to end the game it must first reach the target and then the exit node

Scoreboard
    I added a stat to keep track of how many nodes it visits since there are many times where you cannot see the entire list. 
