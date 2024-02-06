import unittest
from main import process_list

class TestProcessList(unittest.TestCase):
    def test_valid_input(self):
        input_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]
        output_list = process_list(input_list)
        self.assertEqual(output_list, [1, 4, 5, 7, 9, 11, 13, 16, 17, 19])

    def test_invalid_input(self):
        input_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19]
        with self.assertRaises(ValueError):
            process_list(input_list)

if __name__ == "__main__":
    unittest.main()
