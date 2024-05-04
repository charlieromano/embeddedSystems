import serial 

# Configure the serial port
ser = serial.Serial('COM4', 9600)  

try:
    while True:
        # Read input from user
        data = input("Enter data to send (or type 'exit' to quit): ")

        # Check if the user wants to exit
        if data.lower() == 'exit':
            break

        # Send the data to the serial port
        ser.write(data.encode() + b'\n')

        # Wait for the echo response
        response = ser.readline().decode().strip()
        print("Echo response:", response)
except KeyboardInterrupt:
    # Close the serial port when Ctrl+C is pressed
    ser.close()
    print("Serial port closed")