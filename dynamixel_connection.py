from dynamixel_sdk import *
import os

if os.name == 'nt':
    import msvcrt

    def getch():
        """This function gets a single character from the user on Windows."""
        return msvcrt.getch().decode()
else:
    import sys
    import tty
    import termios
    fd = sys.stdin.fileno()
    old_settings = termios.tcgetattr(fd)

    def getch():
        """This function gets a single character from the user on Unix-like systems."""
        try:
            tty.setraw(sys.stdin.fileno())
            ch = sys.stdin.read(1)
        finally:
            termios.tcsetattr(fd, termios.TCSADRAIN, old_settings)
        return ch
def nothing(x):
    """this function does nothing for the given input x

    Args:
        x (_type_): _description_
    
    """
    pass

def set_dynamixel(serialName, baudRate, protocolVersion):
    """this function sets the dynamixel connection

    Args:
        serialName (str): the serial name of the dynamixel
        baudRate (int): the baud rate of the dynamixel
    
    """
    global portHandler, packetHandler
    # Initialize PortHandler instance
    # Set the port path
    # Get methods and members of PortHandlerLinux or PortHandlerWindows
    portHandler = PortHandler(serialName)

    # Initialize PacketHandler instance
    # Set the protocol version
    # Get methods and members of Protocol1PacketHandler or Protocol2PacketHandler
    packetHandler = PacketHandler(protocolVersion)

    # Open port
    if portHandler.openPort():
        print("Succeeded to open the port")
    else:
        print("Failed to open the port")
        print("Press any key to terminate...")
        getch()
        quit()

    # Set port baudrate
    if portHandler.setBaudRate(baudRate):
        print("Succeeded to change the baudrate")
    else:
        print("Failed to change the baudrate")
        print("Press any key to terminate...")
        getch()
        quit()

    return portHandler, packetHandler
    
def __init__(self, serialName, baudRate, protocolVersion):
    """this function initializes the dynamixel connection

    Args:
        serialName (str): the serial name of the dynamixel
        baudRate (int): the baud rate of the dynamixel
    
    """
    self.portHandler, self.packetHandler = set_dynamixel(serialName, baudRate, protocolVersion)