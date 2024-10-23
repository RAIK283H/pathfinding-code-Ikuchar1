import math
import unittest
import graph_data
import global_game_data
from pathing import get_random_path, get_bfs_path, get_dfs_path, get_dijkstra_path, get_test_path



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
        
    def test_dfs_happyCase(self):
        
        graph_index = 0
        target_node = 4
        
        global_game_data.current_graph_index = graph_index
        global_game_data.target_node = {graph_index: target_node}
        
        graph_data.graph_data = {
            graph_index: [
                (0, [1, 2]),
                (1, [3]),
                (2, [3, 4]),
                (3, [5]),
                (4, [5]),
                (5, [6, 7]),
                (6, [8]),
                (7, [8]),
                (8, [9]),
                (9, [])
            ]
        }
        
        #path it should follow
        path = [0, 2, 4, 5, 7, 8, 9]
        #path it actually follows
        real_path = get_dfs_path()
                
        self.assertEqual(path, real_path)
        
        
    def test_bfs_happyCase(self):
        
        graph_index = 0
        target_node = 4
        
        global_game_data.current_graph_index = graph_index
        global_game_data.target_node = {graph_index: target_node}
        
        graph_data.graph_data = {
            graph_index: [
                (0, [1, 2]),
                (1, [3]),
                (2, [3, 4]),
                (3, [5]),
                (4, [5]),
                (5, [6, 7]),
                (6, [8]),
                (7, [8]),
                (8, [9]),
                (9, [])
            ]
        }
        
        #path it should follow
        path = [0, 2, 4, 5, 6, 8, 9]
        #path it actually follows
        real_path = get_bfs_path()
        
        self.assertEqual(path, real_path)

if __name__ == '__main__':
    unittest.main()
