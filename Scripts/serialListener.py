
import serial

ser = serial.Serial('COM4', 9600)  # Change 'COM3' to the appropriate port and 9600 to baud rate

try:
    while True:
        # Read a line from the serial port
        received_data = ser.readline().decode().strip()
        print("Received:", received_data)

        # Echo back to the sender
        ser.write(received_data.encode() + b'\n')
except KeyboardInterrupt:
    # Close the serial port when Ctrl+C is pressed
    ser.close()
    print("Serial port closed")