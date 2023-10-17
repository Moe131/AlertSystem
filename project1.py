from pathlib import Path
from simulation import Simulation
from device import Device, Propagation
from alert import Alert


# This function can not be tested since it requires user input for terminal
def _read_input_file_path() -> Path:
    """Reads the input file path from the standard input"""
    return Path(input())

def readFileLines(path:Path, encoding = 'utf-8') -> list:
    """Reads the lines of a file with given path and returns them as a list"""
    with open(path, 'r', encoding = encoding) as the_file:
        return the_file.readlines()

def isLineComment(line:str) -> bool:
    """Checks if an input line is a comment"""
    if line.startswith('#'):
        return True
    return False

def isLineBlank(line:str) -> bool:
    """Check if an input line is a blank line"""
    return line.isspace()

def getLineCommand(line:str) -> str:
    """Reads an input line and returns its command type as a string.
    Five command types are defined in our program:
    LENGTH, DEVICE, ALERT, PROPAGATE, CANCEL"""
    return line.split()[0]

def parseLine(line:str, sim: Simulation) -> bool:
    """Reads a line of input and parses it based on its command type"""
    command = getLineCommand(line)
    if command == 'LENGTH':
        length = int(line.split()[1])
        sim.setLength(length)

    elif command == 'DEVICE':
        ID = int(line.split()[1])
        device = Device(ID)
        sim.addDevice(device)

    elif command == 'ALERT':
        senderDeviceID = int(line.split()[1])
        description = line.split()[2]
        time = int(line.split()[3])
        alert = Alert(description)
        sim.addEvents(time, senderDeviceID, alert)

    elif command == 'PROPAGATE':
        senderDeviceID = int(line.split()[1])
        receiverDeviceID = int(line.split()[2])
        delay = int(line.split()[3])
        propagation = Propagation(senderDeviceID,receiverDeviceID,delay)
        sim.getDeviceByID(senderDeviceID).addPropagation(propagation)

    elif command == 'CANCEL':
        senderDeviceID = int(line.split()[1])
        description = line.split()[2]
        time = int(line.split()[3])
        alert = Alert(description, True)
        sim.addEvents(time, senderDeviceID, alert)
    else:
        return False
    return True

# This main() can not be tested since it requires user input in its implementation
def main() -> None:
    """Runs the simulation program in its entirety"""
    input_file_path = _read_input_file_path()
    # The if statement below can not be tested since its inside main()
    if not input_file_path.is_file():
        print("FILE NOT FOUND")
        return
    inputLines = readFileLines(input_file_path)
    sim = Simulation()

    for line in inputLines:
        if (not isLineBlank(line)) and (not isLineComment(line)) :
            parseLine(line, sim)

    sim.run()
    sim.printResults()

if __name__ == '__main__':
    main()
