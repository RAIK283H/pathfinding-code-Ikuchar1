from graph_data import graph_data

def sjt_permutations(n):
    
    #sets up elements and direction they are facing
    elements = list(range(n))
    directions = [-1] * n #-1 is left, 1 is right
    permutations = []
    
    def get_largest_mobile():
        max_mobile = -1
        mobile_index = -1
        
        for i in range(n):
            
            #if it is facing left, not first element, and it is greater than the element to the left
            if directions[i] == -1 and i > 0 and elements[i] > elements[i-1]:
                if elements[i] > max_mobile:
                    max_mobile = elements[i]
                    mobile_index = i
            #if it is facing right, not last element, and it is greater than the element to the right
            elif directions[i] == 1 and i < n - 1 and elements[i] > elements[i+1]:
                if elements[i] > max_mobile:
                    max_mobile = elements[i]
                    mobile_index = i
        return mobile_index
    
    #add a copy of current elements list to permutations
    permutations.append(elements[:])
    
    while True:
        index = get_largest_mobile()
        if index == -1:
            #no more elements
            break
            
        #swap elements in given direction
        swap_i = index + directions[index]
        temp = elements[swap_i]
        elements[swap_i] = elements[index]
        elements[index] = temp
        
        temp = directions[swap_i]
        directions[swap_i] = directions[index]
        directions[index] = temp
        index = swap_i
        
        #reverse directions of elements larger than the swapped element
        for i in range(n):
            if elements[i] > elements[index]:
                directions[i] *= -1
        
        #add a copy of current elements list to permutations
        permutations.append(elements[:])
    return permutations

def hamiltonian_helper(perm, graph):
    
    for node in perm:
        if node >= len(graph):
            #print(f"Invalid node {node} in permutation {perm} (out of bounds)")
            return False
    
    for i in range(len(perm) - 1):
        current_node = perm[i]
        next_node = perm[i + 1]
        #if next one is not in current permutations neighbor list then it isn't cycle
        if perm[i + 1] not in graph[perm[i]][1]:
            #print(f"No edge between {current_node} and {next_node} in permutation {perm}")
            return False
    
    first_node = perm[0]
    last_node = perm[-1]
    if perm[0] not in graph[perm[-1]][1]:
        #print(f"No edge between {last_node} and {first_node} to complete cycle in permutation {perm}")
        return False
    #check to see if last one is connected to starting points neighbors
    #print(f"Valid Hamiltonian cycle found: {perm}")
    return True

def get_hamiltonians(permutations, graph):
    hamilts = []
    
    for perm in permutations:
        if hamiltonian_helper(perm, graph):
            hamilts.append(perm)
    return hamilts
 
if __name__ == '__main__':
    perms = sjt_permutations(4)
    for perm in perms:
        print(str(perm) + ",")