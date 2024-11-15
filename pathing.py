from collections import deque
from numpy import random
import graph_data
import global_game_data
import math



def set_current_graph_paths():
    global_game_data.graph_paths.clear()
    global_game_data.graph_paths.append(get_test_path())
    global_game_data.graph_paths.append(get_random_path())
    global_game_data.graph_paths.append(get_dfs_path())
    global_game_data.graph_paths.append(get_bfs_path())
    global_game_data.graph_paths.append(get_dijkstra_path())


def get_test_path():
    return [0] + graph_data.test_path[global_game_data.current_graph_index]


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
    
    #get path from start to target
    start_to_target_path = dfs(graph, start_node, target_node)
    #make sure it has start and target node in path
    assert (start_node in start_to_target_path) and (target_node in start_to_target_path), "Did not go from start to target"
    
    #get path from target to end
    target_to_end_path = dfs(graph, target_node, exit_node)
    #make sure it has target and exit node in path
    assert (target_node in target_to_end_path) and (exit_node in target_to_end_path), "Did not go from target to exit"
    
    #combine the two paths
    #targetToEndPath starts at 2nd element since it started at target and the first path ended in target
    full_path = start_to_target_path + target_to_end_path[1:]

    #post conditions
    assert target_node in full_path, "Path does not go thru target node"
    assert exit_node == full_path[-1], "Path does not end at exit node"
    for i in range(len(full_path) - 1):
        assert full_path[i + 1] in graph[full_path[i]][1], "Not neighbors!"
    
    return full_path

#Helper function to get path for dfs
def dfs(graph, start, end):
    #stack has node and list of nodes in the path so far
    stack = [(start, [start])]
    visited = set()
    
    while stack:
        #get node and current path list from stack
        node, path = stack.pop()
        
        if node == end:
            #we are at the target
            return path
        
        if node not in visited:
            #add it to the nodes we are visiting
            visited.add(node)
            
            #run dfs on all of the neigbors by adding them to stack
            neighbors = graph[node][1]
            for neighbor in neighbors:
                if neighbor not in visited:
                    stack.append((neighbor, path + [neighbor]))
                    
    #returns blank list if we can't find path
    return []
        


def get_bfs_path():
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
    
    #get path from start to target
    start_to_target_path = bfs(graph, start_node, target_node)
    #make sure it has start and target node in path
    assert (start_node in start_to_target_path) and (target_node in start_to_target_path), "Did not go from start to target"
    
    #get path from target to end
    target_to_end_path = bfs(graph, target_node, exit_node)
    #make sure it has target and exit node in path
    assert (target_node in target_to_end_path) and (exit_node in target_to_end_path), "Did not go from target to exit"
    
    #combine the two paths
    #targetToEndPath starts at 2nd element since it started at target and the first path ended in target
    full_path = start_to_target_path + target_to_end_path[1:]
    
    #post conditions
    assert target_node in full_path, "Path does not go thru target node"
    assert exit_node == full_path[-1], "Path does not end at exit node"
    for i in range(len(full_path) - 1):
        assert full_path[i + 1] in graph[full_path[i]][1]
    
    return full_path

#Helper for bfs function
def bfs(graph, start, end):
    #set up queue and other lists
    queue = deque([(start, [start])])
    visited = set()
    
    while  queue:
        node, path = queue.popleft()
        
        if node in visited:
            continue
        visited.add(node)
        
        if node == end:
            #done
            return path 
                   
        #add all neigbors to the queue
        for neighbor in sorted(graph[node][1]):
            if neighbor not in visited:
                queue.append((neighbor, path + [neighbor]))
                    
    #returns blank if we can't get path
    return []

    
def calculate_dist(node1, node2):
    x1, y1 = node1
    x2, y2 = node2
    return math.sqrt((x2-x1) ** 2 + (y2-y1) ** 2)
    
def dijkstra_helper(graph, start, end):
    dist = {node: float('inf') for node in range(len(graph))}
    parent = {node: None for node in range(len(graph))}
    dist[start] = 0
    unvisited = dist.copy()
    
    while unvisited:
        curr_node = min(unvisited, key=unvisited.get)
        curr_dist = unvisited[curr_node]
        
        del unvisited[curr_node]
        
        if curr_node == end:
            break
        
        for neighbor in graph[curr_node][1]:
            curr_coords = graph[curr_node][0]
            neighbor_coords = graph[neighbor][0]
            edge_dist = calculate_dist(curr_coords, neighbor_coords)
        
            new_dist = curr_dist + edge_dist
            if new_dist < dist[neighbor]:
                dist[neighbor] = new_dist
                parent[neighbor] = curr_node
                unvisited[neighbor] = new_dist
            
    path = []
    current = end
    while current is not None:
        path.append(current)
        current = parent[current]
    path.reverse()
    return path
    
def get_dijkstra_path():
    graph_index = global_game_data.current_graph_index
    graph = graph_data.graph_data[graph_index]
    
    start_node = 0
    target_node = global_game_data.target_node[graph_index]
    exit_node = len(graph) - 1
    
    
    #pre condition
    assert (start_node in range(len(graph))) and (target_node in range(len(graph))) and (exit_node in range(len(graph))), "Missing vital node in graph"
    
    start_to_target_path = dijkstra_helper(graph, start_node, target_node)
    target_to_exit_path = dijkstra_helper(graph, target_node, exit_node)
    path = start_to_target_path + target_to_exit_path[1:]
    
    #post conditions
    assert path[0] == start_node, "Path does not start at start_node"
    assert path[-1] == exit_node, "Path does not end at exit_node"
    for i in range(len(path) - 1):
        assert path[i + 1] in graph[path[i]][1], "There are nodes that aren't neighbors"
    
    return path
