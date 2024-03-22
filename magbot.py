# import serial 
# from serial.tools import list_ports
import dynamixel_connection as dxl
import keyboard

DXL_ID = [6, 7, 8, 9]  # Dynamixel ID. 9 : front right, 8 : front left, 7 : back left, 6 : back right
BAUDRATE = 1_000_000 # Dynamixel default baudrate : 57600
# AX-12A wheel mode
# If you want to use AX-12A as wheel mode, set is_wheel = True
is_wheel = True

# Protocol version
# Dynamixel protocol version 1.0 / 2.0
PROTOCOL_VERSION = 1.0 # AX - 12 : 1.0 XM-32 : 2.0
# Default setting
# If you want to use XM, XL series, set is_XL = True
# DEVICENAME = serial.Serial(port = list(list_ports.comports())[0].device, baudrate = BAUDRATE)
# DEVICENAME = '/dev/ttyUSB0' # linux
DEVICENAME = 'COM4' # windows
MOVING_SPEED = 32 # address : 32, range : CCW 0 ~ 1023 CW 1024 ~ 2047
CW_ANGLE_LIMIT = 0
CCW_ANGLE_LIMIT = 0
# If a value in the range of 0 ~ 1,023 is used, it is stopped by setting to 0 while rotating to CCW direction.
# If a value in the range of 1,024 ~ 2,047 is used, it is stopped by setting to 1,024 while rotating to CW direction.
CW_Speed = 512
CCW_Speed = 1536

dxl.set_dynamixel(DEVICENAME, BAUDRATE, PROTOCOL_VERSION)

# test : moving forward 9 : CW, 8 : CCW, 7 : CCW, 6 : CW = DXL_ID[0] : CW, DXL_ID[1] : CCW, DXL_ID[2] : CCW, DXL_ID[3] : CW
# when input key w, a, s, d in terminal, the robot moves forward, left, backward, right

def move_forward():
    dxl.packetHandler.write2ByteTxRx(dxl.portHandler, DXL_ID[0], MOVING_SPEED, CW_Speed) # CW
    dxl.packetHandler.write2ByteTxRx(dxl.portHandler, DXL_ID[1], MOVING_SPEED, CCW_Speed) # CCW
    dxl.packetHandler.write2ByteTxRx(dxl.portHandler, DXL_ID[2], MOVING_SPEED, CCW_Speed) # CCW
    dxl.packetHandler.write2ByteTxRx(dxl.portHandler, DXL_ID[3], MOVING_SPEED, CW_Speed) # CW
    
def move_backward():
    dxl.packetHandler.write2ByteTxRx(dxl.portHandler, DXL_ID[0], MOVING_SPEED, CCW_Speed) # CCW
    dxl.packetHandler.write2ByteTxRx(dxl.portHandler, DXL_ID[1], MOVING_SPEED, CW_Speed) # CW
    dxl.packetHandler.write2ByteTxRx(dxl.portHandler, DXL_ID[2], MOVING_SPEED, CW_Speed) # CW
    dxl.packetHandler.write2ByteTxRx(dxl.portHandler, DXL_ID[3], MOVING_SPEED, CCW_Speed) # CCW

def move_right():
    dxl.packetHandler.write2ByteTxRx(dxl.portHandler, DXL_ID[0], MOVING_SPEED, CCW_Speed) # CCW
    dxl.packetHandler.write2ByteTxRx(dxl.portHandler, DXL_ID[1], MOVING_SPEED, CCW_Speed) # CCW
    dxl.packetHandler.write2ByteTxRx(dxl.portHandler, DXL_ID[2], MOVING_SPEED, CCW_Speed) # CW
    dxl.packetHandler.write2ByteTxRx(dxl.portHandler, DXL_ID[3], MOVING_SPEED, CCW_Speed) # CW
    
def move_left():
    dxl.packetHandler.write2ByteTxRx(dxl.portHandler, DXL_ID[0], MOVING_SPEED, CW_Speed) # CW
    dxl.packetHandler.write2ByteTxRx(dxl.portHandler, DXL_ID[1], MOVING_SPEED, CW_Speed) # CW
    dxl.packetHandler.write2ByteTxRx(dxl.portHandler, DXL_ID[2], MOVING_SPEED, CW_Speed) # CCW
    dxl.packetHandler.write2ByteTxRx(dxl.portHandler, DXL_ID[3], MOVING_SPEED, CW_Speed) # CCW
    
def stop():
    dxl.packetHandler.write2ByteTxRx(dxl.portHandler, DXL_ID[0], MOVING_SPEED, 0) # stop
    dxl.packetHandler.write2ByteTxRx(dxl.portHandler, DXL_ID[1], MOVING_SPEED, 0) # stop
    dxl.packetHandler.write2ByteTxRx(dxl.portHandler, DXL_ID[2], MOVING_SPEED, 0) # stop
    dxl.packetHandler.write2ByteTxRx(dxl.portHandler, DXL_ID[3], MOVING_SPEED, 0) # stop
    
def main():
    def handle_key_event(event):
        global CW_Speed, CCW_Speed
        if event.event_type == keyboard.KEY_DOWN:
            if event.name == 'w':
                move_forward()
            elif event.name == 'a':
                move_left()
            elif event.name == 's':
                move_backward()
            elif event.name == 'd':
                move_right()
            elif event.name == 'e':
                CW_Speed+=50
                CCW_Speed+=50
                if CW_Speed > 1023:
                    CW_Speed= 1023
                if CCW_Speed > 2047:
                    CCW_Speed= 2047
                print(CW_Speed, CCW_Speed)
            elif event.name == 'c':
                CW_Speed-=50
                CCW_Speed-=50
                if CW_Speed < 0:
                    CW_Speed= 0
                if CCW_Speed < 1024:
                    CCW_Speed= 1024
                print(CW_Speed, CCW_Speed)
                
        elif event.event_type == keyboard.KEY_UP:
            stop()

    keyboard.on_press_key('w', handle_key_event)
    keyboard.on_press_key('a', handle_key_event)
    keyboard.on_press_key('s', handle_key_event)
    keyboard.on_press_key('d', handle_key_event)
    keyboard.on_release_key('w', handle_key_event)
    keyboard.on_release_key('a', handle_key_event)
    keyboard.on_release_key('s', handle_key_event)
    keyboard.on_release_key('d', handle_key_event)
    keyboard.on_press_key('e', handle_key_event)
    keyboard.on_press_key('c', handle_key_event)
    keyboard.wait('q')
            
if __name__ == '__main__':
    main()



