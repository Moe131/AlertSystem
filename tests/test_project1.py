from pathlib import Path
import unittest
import project1

class project1Test(unittest.TestCase):

    def setUp(self) -> None:
        self._path = Path('../samples/sample_input.txt')

    def test_file_lines_are_returned_as_a_string(self):
        with open(self._path, 'r', encoding = 'utf-8') as the_file:
            self.assertEqual(project1.readFileLines(self._path), the_file.readlines())

    # This can not be tested since the function requires user input from terminal
    #
    #def test_correct_input_file_path_is_returned(self):
    #    path = Path('../samples/sample_input.txt')
    #    self.assertEqual(project1._read_input_file_path(),path)


if __name__ == '__main__':
    unittest.main()