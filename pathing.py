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
    #Gets random path from start to target node to the exit node
    
    #get graph
    graph_index = global_game_data.current_graph_index
    graph = graph_data.graph_data[graph_index]
    
    #set up main nodes
    start_node = 0
    target_node = global_game_data.target_node[graph_index]
    exit_node = len(graph) - 1
    
    #pre condition
    #make sure start, target, and exit node are actually in the graph
    assert (start_node in range(len(graph))) and (target_node in range(len(graph))) and (exit_node in range(len(graph))), "Missing vital node in graph"
    
    random_path = []
    random_path.append(start_node)
    #loop to randomly move until we reach the target node
    curr_node = start_node
    while curr_node != target_node:
        #pick random node to move to next
        connected_nodes = graph[curr_node][1]
        next_node = random.choice(connected_nodes)
        #add it to the random path list
        if next_node == exit_node:
            #if it is trying to go back to start then skip iteration
            # or if it tries to get to the exit node before it reaches the target node
            continue
        random_path.append(next_node)
        curr_node = next_node
    
    #loop to randomly move from target node to exit node
    while curr_node != exit_node:
        #same thing but we go til exit node
        connected_nodes = graph[curr_node][1]
        next_node = random.choice(connected_nodes)
        #add it to the random path list
        #if next_node == start_node:
            #if it is trying to go back to start then skip iteration
            #continue
        
        random_path.append(next_node)
        curr_node = next_node
        
    
    #post condition
    #make sure we actually made it to the exit node
    assert exit_node in random_path, "Random Path did not go through the exit node"
    #make sure we made it to target node
    assert target_node in random_path, "Random Path did not go through the target node"

    return random_path


def get_dfs_path():
    return [1,2]


def get_bfs_path():
    return [1,2]


def get_dijkstra_path():
    return [1,2]
