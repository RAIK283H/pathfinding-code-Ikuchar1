import math

def list_to_matrix(graph):
    """This will convert adjacency list to matrix"""
    
    n = len(graph)
    weight_matrix = [[math.inf] * n for _ in range(n)]
    
    for i in range(n):
        weight_matrix[i][i] = 0
        for neighbor in graph[i][1]:
            x1, y1 = graph[i][0]
            x2, y2 = graph[neighbor][0]
            #get dist between point and neighbor
            weight_matrix[i][neighbor] = math.sqrt((x2-x1) ** 2 + (y2-y1) ** 2)
            
    return weight_matrix

def floyd_warshall(weight_matrix):
    """This will get shortest path to each point from each point"""
    n = len(weight_matrix)
    #set up matrices
    dist_matrix = [row[:] for row in weight_matrix]
    parent_matrix = [[None] * n for _ in range(n)]
    
    for i in range(n):
        for j in range(n):
            if weight_matrix[i][j] < math.inf and i != j:
                #set parent
                parent_matrix[i][j] = i
                
    for k in range(n):
        for i in range(n):
            for j in range(n):
                if dist_matrix[i][j] > dist_matrix[i][k] + dist_matrix[k][j]:
                    dist_matrix[i][j] = dist_matrix[i][k] + dist_matrix[k][j]
                    #update parent matrix
                    parent_matrix[i][j] = parent_matrix[k][j]
                    
    return dist_matrix, parent_matrix
    
def make_path(parent_matrix, start, end):
    """Make shortest path from start to end using the parent matrix made in fro floyd-warshall"""
    
    #check for no path
    if parent_matrix[start][end] is None:
        return []
    
    #make path using parent matrix
    path = [end]
    while end != start:
        end = parent_matrix[start][end]
        path.append(end)
        
    #reverse the path to get it from start to end
    path.reverse()
    return path

def make_entire_path(parent_matrix, start, target, end):
    """Makes path that goes from start to target to end"""
    start_to_target = make_path(parent_matrix, start, target)
    
    target_to_end = make_path(parent_matrix, target, end)
    
    if target_to_end:
        path = start_to_target + target_to_end[1:]
    else:
        path = start_to_target
    
    return path

def get_floyd_warshall_path(graph, start, target, end):
    weight_matrix = list_to_matrix(graph)
    dist_matrix, parent_matrix = floyd_warshall(weight_matrix)
    path = make_entire_path(parent_matrix, start, target, end)

    return path