import serial
import serial.tools.list_ports
import matplotlib.pyplot as plt
import matplotlib.animation as animation

# Function to find available COM ports
def find_serial_port():
    ports = list(serial.tools.list_ports.comports())
    for p in ports:
        print(p)  # Print all available ports
    return ports

# Check available ports and select the correct one
available_ports = find_serial_port()
serial_port = 'COM5'  # Change this if your device is on a different port
baud_rate = 9600

# Confirm if the specified port is available
if not any(serial_port in str(port) for port in available_ports):
    raise Exception(f"Port {serial_port} not found. Check the connection and available ports.")

# Open Serial Connection
try:
    ser = serial.Serial(serial_port, baud_rate, timeout=1)
except serial.SerialException as e:
    raise Exception(f"Failed to open {serial_port}: {e}")

# Data storage for real-time plotting
data = []

# Function to update the plot
def update(frame):
    global data
    if ser.in_waiting > 0:
        try:
            value = int(ser.readline().decode().strip())
            data.append(value)
            if len(data) > 100:  # Keep only last 100 values
                data.pop(0)
        except ValueError:
            pass  # Ignore errors from bad data
    ax.clear()
    ax.plot(data, label="Sound Level", color='blue')
    ax.set_ylim(0, 1023)  # 10-bit ADC range for ESP8266
    ax.set_title("Real-time Sound Sensor Readings")
    ax.set_xlabel("Time")
    ax.set_ylabel("Sound Level")
    ax.legend()
    ax.grid(True)

# Setup Matplotlib for Real-time Plotting
fig, ax = plt.subplots()
ani = animation.FuncAnimation(fig, update, interval=100)
plt.show()

# Close serial connection when the program is stopped
ser.close()