import math
import unittest
import graph_data
import global_game_data
from pathing import get_random_path, get_bfs_path, get_dfs_path, get_dijkstra_path, get_test_path
from permutation import sjt_permutations, get_hamiltonians, hamiltonian_helper
from f_w import make_path, floyd_warshall, list_to_matrix



class TestPathFinding(unittest.TestCase):

    def test_upper(self):
        self.assertEqual('test'.upper(), 'TEST')

    def test_isupper(self):
        self.assertTrue('TEST'.isupper())
        self.assertFalse('Test'.isupper())

    def test_floating_point_estimation(self):
        first_value = 0
        for x in range(1000):
            first_value += 1/100
        second_value = 10
        almost_pi = 3.1
        pi = math.pi
        self.assertNotEqual(first_value,second_value)
        self.assertAlmostEqual(first=first_value,second=second_value,delta=1e-9)
        self.assertNotEqual(almost_pi, pi)
        self.assertAlmostEqual(first=almost_pi, second=pi, delta=1e-1)
        
    #random pathing test
    def test_random_hits_required_nodes(self):
        
        graph_index = 0
        target_node = 4
        
        global_game_data.current_graph_index = graph_index
        global_game_data.target_node = {graph_index: target_node}
        
        graph_data.graph_data = {
            graph_index: [
                [(0, 0), [1, 4]],
                [(0, 100), [0, 2, 5]],
                [(0, 200), [1, 3, 6]],
                [(0, 300), [2, 7]],
                [(100, 0), [5, 0, 8]],
                [(100, 100), [4, 6, 1, 9]],
                [(100, 200), [5, 7, 2, 10]],
                [(100, 300), [6, 3, 11]],
                [(200, 0), [9, 4, 12]],
                [(200, 100), [8, 10, 5, 13]],
                [(200, 200), [9, 11, 6, 14]],
                [(200, 300), [10, 7, 15]],
                [(300, 0), [13, 8]],
                [(300, 100), [12, 14, 9]],
                [(300, 200), [13, 15, 10]],
                [(300, 300), [14,11]]
            ]
        }
        
        #path it actually follows
        path = get_random_path()
        
        #check to make sure it starts at start, hits target, and ends at exit node
        self.assertEqual(path[0], 0, "The path does not start at the start node")
        self.assertIn(target_node, path, "The path does not include the target node")
        self.assertEqual(path[-1], 15, "The path does not end at the exit node")
    
    #tests to make sure it gets correct path
    def test_dfs_happy_case(self):
        
        graph_index = 0
        target_node = 4
        
        global_game_data.current_graph_index = graph_index
        global_game_data.target_node = {graph_index: target_node}
        
        graph_data.graph_data = {
            graph_index: [
                [(0, 0), [1, 4]],
                [(0, 100), [0, 2, 5]],
                [(0, 200), [1, 3, 6]],
                [(0, 300), [2, 7]],
                [(100, 0), [5, 0, 8]],
                [(100, 100), [4, 6, 1, 9]],
                [(100, 200), [5, 7, 2, 10]],
                [(100, 300), [6, 3, 11]],
                [(200, 0), [9, 4, 12]],
                [(200, 100), [8, 10, 5, 13]],
                [(200, 200), [9, 11, 6, 14]],
                [(200, 300), [10, 7, 15]],
                [(300, 0), [13, 8]],
                [(300, 100), [12, 14, 9]],
                [(300, 200), [13, 15, 10]],
                [(300, 300), [14,11]]
            ]
        }
        
        #path it should follow
        path = [0, 4, 8, 12, 13, 9, 5, 1, 2, 6, 10, 14, 15]
        
        #path it actually follows
        real_path = get_dfs_path()
                
        self.assertEqual(path, real_path)
        
    def test_dfs_hits_required_nodes(self):
        
        graph_index = 0
        target_node = 4
        
        global_game_data.current_graph_index = graph_index
        global_game_data.target_node = {graph_index: target_node}
        
        graph_data.graph_data = {
            graph_index: [
                [(0, 0), [1, 4]],
                [(0, 100), [0, 2, 5]],
                [(0, 200), [1, 3, 6]],
                [(0, 300), [2, 7]],
                [(100, 0), [5, 0, 8]],
                [(100, 100), [4, 6, 1, 9]],
                [(100, 200), [5, 7, 2, 10]],
                [(100, 300), [6, 3, 11]],
                [(200, 0), [9, 4, 12]],
                [(200, 100), [8, 10, 5, 13]],
                [(200, 200), [9, 11, 6, 14]],
                [(200, 300), [10, 7, 15]],
                [(300, 0), [13, 8]],
                [(300, 100), [12, 14, 9]],
                [(300, 200), [13, 15, 10]],
                [(300, 300), [14,11]]
            ]
        }
        
        #path it actually follows
        path = get_dfs_path()
        
        #check to make sure it starts at start, hits target, and ends at exit node
        self.assertEqual(path[0], 0, "The path does not start at the start node")
        self.assertIn(target_node, path, "The path does not include the target node")
        self.assertEqual(path[-1], 15, "The path does not end at the exit node")
     
    #tests to make sure it gets correct path
    def test_bfs_happy_case(self):
        
        graph_index = 0
        target_node = 4
        
        global_game_data.current_graph_index = graph_index
        global_game_data.target_node = {graph_index: target_node}
        
        graph_data.graph_data = {
            graph_index: [
                [(0, 0), [1, 4]],
                [(0, 100), [0, 2, 5]],
                [(0, 200), [1, 3, 6]],
                [(0, 300), [2, 7]],
                [(100, 0), [5, 0, 8]],
                [(100, 100), [4, 6, 1, 9]],
                [(100, 200), [5, 7, 2, 10]],
                [(100, 300), [6, 3, 11]],
                [(200, 0), [9, 4, 12]],
                [(200, 100), [8, 10, 5, 13]],
                [(200, 200), [9, 11, 6, 14]],
                [(200, 300), [10, 7, 15]],
                [(300, 0), [13, 8]],
                [(300, 100), [12, 14, 9]],
                [(300, 200), [13, 15, 10]],
                [(300, 300), [14,11]]
            ]
        }
        
        #path it should follow
        path = [0, 4, 5, 6, 7, 11, 15]
        #path it actually follows
        real_path = get_bfs_path()
        
        self.assertEqual(path, real_path)
        
    def test_bfs_hits_required_nodes(self):
        
        graph_index = 0
        target_node = 4
        
        global_game_data.current_graph_index = graph_index
        global_game_data.target_node = {graph_index: target_node}
        
        graph_data.graph_data = {
            graph_index: [
                [(0, 0), [1, 4]],
                [(0, 100), [0, 2, 5]],
                [(0, 200), [1, 3, 6]],
                [(0, 300), [2, 7]],
                [(100, 0), [5, 0, 8]],
                [(100, 100), [4, 6, 1, 9]],
                [(100, 200), [5, 7, 2, 10]],
                [(100, 300), [6, 3, 11]],
                [(200, 0), [9, 4, 12]],
                [(200, 100), [8, 10, 5, 13]],
                [(200, 200), [9, 11, 6, 14]],
                [(200, 300), [10, 7, 15]],
                [(300, 0), [13, 8]],
                [(300, 100), [12, 14, 9]],
                [(300, 200), [13, 15, 10]],
                [(300, 300), [14,11]]
            ]
        }
        
        #path it actually follows
        path = get_bfs_path()
        
        #check to make sure it starts at start, hits target, and ends at exit node
        self.assertEqual(path[0], 0, "The path does not start at the start node")
        self.assertIn(target_node, path, "The path does not include the target node")
        self.assertEqual(path[-1], 15, "The path does not end at the exit node")
        
    def test_dijkstra_happy_case(self):
        graph_index = 0
        target_node = 4

        global_game_data.current_graph_index = graph_index
        global_game_data.target_node = {graph_index: target_node}

        graph_data.graph_data = {
            graph_index: [
                [(0, 0), [1, 4]],
                [(0, 100), [0, 2, 5]],
                [(0, 200), [1, 3, 6]],
                [(0, 300), [2, 7]],
                [(100, 0), [5, 0, 8]],
                [(100, 100), [4, 6, 1, 9]],
                [(100, 200), [5, 7, 2, 10]],
                [(100, 300), [6, 3, 11]],
                [(200, 0), [9, 4, 12]],
                [(200, 100), [8, 10, 5, 13]],
                [(200, 200), [9, 11, 6, 14]],
                [(200, 300), [10, 7, 15]],
                [(300, 0), [13, 8]],
                [(300, 100), [12, 14, 9]],
                [(300, 200), [13, 15, 10]],
                [(300, 300), [14, 11]]
            ]
        }

        # Path it should follow
        expected = [0, 4, 5, 6, 7, 11, 15]
        
        # Path it actually follows
        path = get_dijkstra_path()

        # Check if the paths match
        self.assertEqual(expected, path)
        
    def test_dijkstra_hits_required_nodes(self):
        graph_index = 0
        target_node = 4

        global_game_data.current_graph_index = graph_index
        global_game_data.target_node = {graph_index: target_node}

        graph_data.graph_data = {
            graph_index: [
                [(0, 0), [1, 4]],
                [(0, 100), [0, 2, 5]],
                [(0, 200), [1, 3, 6]],
                [(0, 300), [2, 7]],
                [(100, 0), [5, 0, 8]],
                [(100, 100), [4, 6, 1, 9]],
                [(100, 200), [5, 7, 2, 10]],
                [(100, 300), [6, 3, 11]],
                [(200, 0), [9, 4, 12]],
                [(200, 100), [8, 10, 5, 13]],
                [(200, 200), [9, 11, 6, 14]],
                [(200, 300), [10, 7, 15]],
                [(300, 0), [13, 8]],
                [(300, 100), [12, 14, 9]],
                [(300, 200), [13, 15, 10]],
                [(300, 300), [14, 11]]
            ]
        }

        path = get_dijkstra_path()

        self.assertEqual(path[0], 0, "The path does not start at the start node")
        self.assertIn(target_node, path, "The path does not include the target node")
        self.assertEqual(path[-1], 15, "The path does not end at the exit node")
        
    def test_floyd_warshall_happy_case(self):
        graph = [
            [(0, 0), [1, 2]],
            [(0, 1), [0, 2]],
            [(1, 0), [0, 1]]
        ]

        weight_matrix = list_to_matrix(graph)

        # Expected distance matrix
        expected_dist = [
            [0, 1.0, 1.0],
            [1.0, 0, 1.4142135623730951],
            [1.0, 1.4142135623730951, 0]
        ]

        dist_matrix, parent_matrix = floyd_warshall(weight_matrix)

        # Assert distance matrix matches expected
        for i in range(len(expected_dist)):
            for j in range(len(expected_dist)):
                self.assertAlmostEqual(dist_matrix[i][j], expected_dist[i][j], places=6)
                
                
    def test_floyd_warshall_path_reconstruction(self):
        graph = [
            [(0, 0), [1, 2]],
            [(0, 1), [0, 2]],
            [(1, 0), [0, 1]]
        ]

        weight_matrix = list_to_matrix(graph)

        dist_matrix, parent_matrix = floyd_warshall(weight_matrix)

        path_0_to_2 = make_path(parent_matrix, 0, 2)

        expected_path = [0, 2]

        # Assert reconstructed path matches expected
        self.assertEqual(path_0_to_2, expected_path)
        
    def test_floyd_warshall_hits_required_nodes(self):
        graph = [
            [(0, 0), [1, 2]],
            [(0, 1), [0, 2]],
            [(1, 0), [0, 1]]
        ]

        weight_matrix = list_to_matrix(graph)

        dist_matrix, parent_matrix = floyd_warshall(weight_matrix)

        path = make_path(parent_matrix, 0, 2)

        # Ensure the path includes the required start and end nodes
        self.assertEqual(path[0], 0, "The path does not start at the correct start node")
        self.assertEqual(path[-1], 2, "The path does not end at the correct end node")
        
    
        
        

class TestPermutationsAndHamiltonian(unittest.TestCase):
    def test_sjt_3(self):
        expected = [
            [0, 1, 2],
            [0, 2, 1],
            [2, 0, 1],
            [2, 1, 0],
            [1, 2, 0],
            [1, 0, 2]
        ]
        result = sjt_permutations(3)
        self.assertEqual(len(result), 6)
        self.assertEqual(result, expected)
    
    def test_sjt_4(self):
        expected = [
            [0, 1, 2, 3], [0, 1, 3, 2], [0, 3, 1, 2], [3, 0, 1, 2],
            [3, 0, 2, 1], [0, 3, 2, 1], [0, 2, 3, 1], [0, 2, 1, 3],
            [2, 0, 1, 3], [2, 0, 3, 1], [2, 3, 0, 1], [3, 2, 0, 1],
            [3, 2, 1, 0], [2, 3, 1, 0], [2, 1, 3, 0], [2, 1, 0, 3],
            [1, 2, 0, 3], [1, 2, 3, 0], [1, 3, 2, 0], [3, 1, 2, 0],
            [3, 1, 0, 2], [1, 3, 0, 2], [1, 0, 3, 2], [1, 0, 2, 3]
        ]
        result = sjt_permutations(4)
        self.assertEqual(len(result), len(expected))
        self.assertEqual(result, expected)
    
           
    def test_hamiltonian_cycle_test_happy(self):
        i = 0
        permutations = sjt_permutations(len(graph_data.hamiltonianGraphs[i]))
        actual = get_hamiltonians(permutations, graph_data.hamiltonianGraphs[i])
        expected = [
            [0, 1, 2],
            [0, 2, 1],
            [2, 0, 1],
            [2, 1, 0],
            [1, 2, 0],
            [1, 0, 2]
        ]
        self.assertEqual(actual, expected)
    def test_hamiltonian_cycle_test_not_happy(self):
        i = 1
        permutations = sjt_permutations(len(graph_data.hamiltonianGraphs[i]))
        actual = get_hamiltonians(permutations, graph_data.hamiltonianGraphs[i])
        expected = []
        self.assertEqual(actual, expected)

if __name__ == '__main__':
    unittest.main()
