from pathlib import Path
import unittest
import project1

class project1Test(unittest.TestCase):

    def setUp(self) -> None:
        self._path = Path('../samples/sample_input.txt')

    def test_file_lines_are_returned_as_a_string(self):
        with open(self._path, 'r', encoding = 'utf-8') as the_file:
            self.assertEqual(project1.readFileLines(self._path), the_file.readlines())

    def test_input_line_is_a_comment(self):
        line = '# ICS 33 Fall 2023'
        self.assertEqual(project1.isLineComment(line), True)

    def test_input_line_is_blank(self):
        line = "   "
        self.assertEqual(project1.isLineBlank(line), True)

    def test_input_line_command_is_returned(self):
        line = "LENGTH 9999"
        self.assertEqual(project1.getLineCommand(line),'LENGTH')


    # This can not be tested since the function requires user input from terminal
    #
    #def test_correct_input_file_path_is_returned(self):
    #    path = Path('../samples/sample_input.txt')
    #    self.assertEqual(project1._read_input_file_path(),path)


if __name__ == '__main__':
    unittest.main()