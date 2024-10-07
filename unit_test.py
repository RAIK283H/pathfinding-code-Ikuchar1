import math
import unittest
import graph_data
import global_game_data
from pathing import get_random_path



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
        
        
def test_random_stops_on_exit(self):
        path = get_random_path()
        self.assertEqual(path[0], path[0], "Doesn't start on start node")
        self.assertEqual(path[-1], len(graph_data.graph_data[global_game_data.current_graph_index]) - 1, "Does not end on right node")



if __name__ == '__main__':
    unittest.main()
