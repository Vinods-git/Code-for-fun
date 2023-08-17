import pywhatkit
import time

phone_number = "+8830341456"
message = "Hello from Python!"
interval = 1  # Time in seconds between each message

# Run the loop
while True:
    # Send the message
    pywhatkit.sendwhatmsg(phone_number, message, 23,5)

    # Wait for the specified interval
    time.sleep(interval)