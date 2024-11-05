import unittest
import permutations

class TestPermutations(unittest.TestCase):
    def test_move_left(self):
        list = [1, 2, 3, 4]
        excepted = [2, 1, 3, 4]

        result = permutations.move_left(list, 1, 0)

        self.assertEqual(excepted, result)

    def test_move_right(self):
        list = [1, 2, 3, 4]
        excepted = [1, 3, 2, 4]

        result = permutations.move_right(list, 1, 2)

        self.assertEqual(excepted, result)
    
    def test_mobile_integer(self):
        list = [1, 2, 3, 4]
        directions = {1: True, 2: True, 3: True, 4: True}
        excepted = 3

        result = permutations.mobile_integer(list, directions, len(list))
        self.assertEqual(result, excepted)
    
    def test_johnson_trotter(self):
        list = [1, 2, 3, 4, 5, 6]
        n = len(list)
        expected = [
            [1, 2, 3, 4],
            [1, 2, 4, 3],
            [1, 4, 2, 3],
            [4, 1, 2, 3],
            [4, 1, 3, 2],
            [1, 4, 3, 2],
            [1, 3, 4, 2],
            [1, 3, 2, 4],
            [3, 1, 2, 4],
            [3, 1, 4, 2],
            [3, 4, 1, 2],
            [4, 3, 1, 2],
            [4, 3, 2, 1],
            [3, 4, 2, 1],
            [3, 2, 4, 1],
            [3, 2, 1, 4],
            [2, 3, 1, 4],
            [2, 3, 4, 1],
            [2, 4, 3, 1],
            [4, 2, 3, 1],
            [4, 2, 1, 3],
            [2, 4, 1, 3],
            [2, 1, 4, 3],
            [2, 1, 3, 4]
        ]

        result = permutations.johnson_trotter(n)

        self.assertEqual(result, expected)

    def test_hamilton_cycles(self):
        list = [1, 2, 3, 4]
        n = len(list)
        permutation = permutations.johnson_trotter(n)
        expected = [
            [1, 2, 1],
            [2, 1, 2]
        ]

        result = []

        for item in permutation:
            if(permutations.hamilton_cycle_detector(item, 1)):
                item.append(item[0])
                result.append(item)
            else:
                result.append(-1)

        self.assertEqual(expected, result)


if __name__ == '__main__':
    unittest.main()