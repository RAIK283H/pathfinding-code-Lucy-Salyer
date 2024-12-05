import unittest
import f_w
import graph_data
import global_game_data
import math

class TestFloydWarshall(unittest.TestCase):
    def test_adjacency_matrix(self):
        self.graphs = graph_data.graph_data
        global_game_data.current_graph_index = 11
        global_game_data.current_player_index = 0
        curr_graph = graph_data.graph_data[global_game_data.current_graph_index]
        expected = [[math.inf, 300.0, 335.4101966249685], [300.0, math.inf, 335.4101966249685], [335.4101966249685, 335.4101966249685, math.inf]]

        results = f_w.adjacency_matrix(curr_graph)

        self.assertEqual(results, expected)

    def test_adjacency_matrix_two(self):
        self.graphs = graph_data.graph_data
        global_game_data.current_graph_index = 12
        global_game_data.current_player_index = 0
        curr_graph = graph_data.graph_data[global_game_data.current_graph_index]
        expected = [[math.inf, 282.842712474619, 447.21359549995793, math.inf, math.inf],
        [282.842712474619, math.inf, 200.0, 223.60679774997897, math.inf],
        [447.21359549995793, 200.0, math.inf, 223.60679774997897, math.inf],
        [math.inf, 223.60679774997897, 223.60679774997897, math.inf, 200.0],
        [math.inf, math.inf, math.inf, 200.0, math.inf]]

        results = f_w.adjacency_matrix(curr_graph)

        self.assertEqual(results, expected)

    def test_parent_matrix(self):
        self.graphs = graph_data.graph_data
        global_game_data.current_graph_index = 1
        global_game_data.current_player_index = 0
        curr_graph = graph_data.graph_data[global_game_data.current_graph_index]
        expected = [[0, 0, 1, 2], [1, 1, 1, 2], [1, 2, 2, 2], [1, 2, 3, 3]]

        results = f_w.Floyd_Warshall_Algorithm(curr_graph)

        self.assertEqual(results, expected)

    def test_parent_matrix_two(self):
        self.graphs = graph_data.graph_data
        global_game_data.current_graph_index = 12
        global_game_data.current_player_index = 0
        curr_graph = graph_data.graph_data[global_game_data.current_graph_index]
        expected = [[0, 0, 0, 1, 3], [1, 1, 1, 1, 3], [2, 2, 2, 2, 3], [1, 3, 3, 3, 3], [1, 3, 3, 4, 4]]

        results = f_w.Floyd_Warshall_Algorithm(curr_graph)

        self.assertEqual(results, expected)

    def test_build_path(self):
        self.graphs = graph_data.graph_data
        global_game_data.current_graph_index = 4
        global_game_data.current_player_index = 0
        global_game_data.target_node = [0, 0, 0, 0, 1]
        expected = [0, 1, 2, 5, 6, 9, 10]

        results = f_w.get_floyd_warshall()
        self.assertEqual(results, expected)

    def test_3rd_graph(self):
        self.graphs = graph_data.graph_data
        global_game_data.current_graph_index = 2
        global_game_data.current_player_index = 0
        global_game_data.target_node = [0, 0, 7]
        expected = [0, 17, 12, 7, 9, 15, 18, 23]

        results = f_w.get_floyd_warshall()
        self.assertEqual(results, expected)


if __name__ == '__main__':
    unittest.main()
