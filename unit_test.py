import math
import unittest
import global_game_data
import pathing
import graph_data

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

    def test_dfs_happy(self):
       self.graphs = graph_data.graph_data
       global_game_data.current_graph_index = 3
       global_game_data.target_node = [0, 0, 0, 14]
       global_game_data.current_player_index = 0
       path = pathing.get_dfs_path()

       expected = [0, 4, 8, 12, 13, 14, 14, 15]
       self.assertEqual(path, expected)

    def test_dfs_bad(self): 
        self.graphs = graph_data.graph_data
        global_game_data.current_graph_index = 1
        global_game_data.target_node = [0, 2]
        global_game_data.current_player_index = 0
        path = pathing.get_dfs_path()

        bad = [0, 3, 1, 2]
        self.assertNotEqual(path, bad)

    def test_bfs_happy(self):
        self.graphs = graph_data.graph_data
        global_game_data.current_graph_index = 3
        global_game_data.target_node = [0, 0, 0, 14]
        global_game_data.current_player_index = 0
        path = pathing.get_bfs_path()

        expected = [0, 1, 2, 6, 10, 14, 14, 15]
        self.assertEqual(path, expected)

    def test_bfs_bad(self): 
        self.graphs = graph_data.graph_data
        global_game_data.current_graph_index = 1
        global_game_data.target_node = [0, 2]
        global_game_data.current_player_index = 0
        path = pathing.get_bfs_path()

        bad = [0, 3, 1, 2]
        self.assertNotEqual(path, bad)



if __name__ == '__main__':
    unittest.main()
