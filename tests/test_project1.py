from pathlib import Path
import unittest
import project1
from simulation import Simulation

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

    def test_LENGTH_line_is_parsed(self):
        line = "LENGTH 9999"
        sim = Simulation()
        project1.parseLine(line, sim)
        self.assertEqual(sim.getLength() ,9999)

    def test_DEVICE_line_is_parsed(self):
        line = "DEVICE 1"
        sim = Simulation()
        project1.parseLine(line,sim)
        self.assertEqual(sim.getDevices()[0].getID(), 1)

    def test_PROPAGATE_line_is_parsed(self):
        line = "DEVICE 1"
        sim = Simulation()
        project1.parseLine(line,sim)
        line = "PROPAGATE 1 2 750"
        project1.parseLine(line, sim)
        self.assertEqual(sim.getDeviceByID(1).getPropagationList()[0].getPropagationString(), "1 2 750")

    def test_ALERT_line_is_parsed(self):
        sim = Simulation()
        line = "LENGTH 9999"
        project1.parseLine(line, sim)
        line = "DEVICE 1"
        project1.parseLine(line, sim)
        line = "DEVICE 2"
        project1.parseLine(line, sim)
        line = "PROPAGATE 1 2 750"
        project1.parseLine(line, sim)
        line = "ALERT 1 Trouble 0"
        project1.parseLine(line,sim)
        self.assertEqual(sim.getEvents()[0].toString(), "@0: #1 SENT ALERT TO #2: Trouble" )

    def test_CANCEL_line_is_parsed(self):
        sim = Simulation()
        line = "LENGTH 9999"
        project1.parseLine(line, sim)
        line = "DEVICE 1"
        project1.parseLine(line, sim)
        line = "DEVICE 2"
        project1.parseLine(line, sim)
        line = "PROPAGATE 1 2 750"
        project1.parseLine(line, sim)
        line = "CANCEL 1 Trouble 2200"
        project1.parseLine(line, sim)
        self.assertEqual(sim.getEvents()[0].toString() ,"@2200: #1 SENT CANCELLATION TO #2: Trouble")

    def test_simulation_runs_events(self):
        inputLines = project1.readFileLines(self._path)
        outputLines = project1.readFileLines('../samples/sample_output.txt')
        sim = Simulation()
        for line in inputLines:
            if (not project1.isLineBlank(line)) and (not project1.isLineComment(line)):
                project1.parseLine(line, sim)
        sim.run()
        self.assertEqual(sim.getEventsInString() ,outputLines)

    def test_simulation_will_not_execute_events_passed_length(self):
        sim = Simulation()
        line = "LENGTH 500"
        project1.parseLine(line, sim)
        line = "DEVICE 1"
        project1.parseLine(line, sim)
        line = "DEVICE 2"
        project1.parseLine(line, sim)
        line = "PROPAGATE 1 2 750"
        project1.parseLine(line, sim)
        line = "ALERT 1 Trouble 100"
        project1.parseLine(line, sim)
        sim.run()
        self.assertEqual(sim.getEventsInString(),['@100: #1 SENT ALERT TO #2: Trouble\n', '@500: END\n'])

    # This can not be tested since the function requires user input from terminal
    #
    #def test_correct_input_file_path_is_returned(self):
    #    path = Path('../samples/sample_input.txt')
    #    self.assertEqual(project1._read_input_file_path(),path)


if __name__ == '__main__':
    unittest.main()