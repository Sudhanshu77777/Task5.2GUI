import tkinter as tk  # Import Tkinter to create the graphical user interface (GUI)
from RPi import GPIO   # Import the GPIO module for controlling the Raspberry Pi's pins

# Set up the GPIO mode and specify pin for the LED
GPIO.setmode(GPIO.BOARD)  # Use BOARD numbering for the GPIO pins
LED_PIN = 11  # Assign GPIO pin 11 for the LED connection
GPIO.setup(LED_PIN, GPIO.OUT)  # Configure this pin as an output to control the LED

# Set up PWM (Pulse Width Modulation) on the LED pin at a frequency of 1000Hz
pwm = GPIO.PWM(LED_PIN, 1000)  # Create a PWM instance on pin 11 with a frequency of 1000Hz
pwm.start(0)  # Begin PWM with a duty cycle of 0% (the LED is initially off)

# Function to adjust the LED brightness based on the position of the slider
def adjust_brightness(val):
    duty_cycle = int(val)  # Convert the slider value from string to integer
    pwm.ChangeDutyCycle(duty_cycle)  # Update the PWM duty cycle to change the LED brightness

# Create the main application window for the GUI
window = tk.Tk()  # Instantiate the main window
window.title("LED Brightness Controller")  # Set the title of the window
window.configure(bg='#F0F0F0')  # Change the background color to a light gray

# Create a large slider for controlling the LED brightness
slider = tk.Scale(window, from_=0, to=100, orient=tk.HORIZONTAL, command=adjust_brightness, 
                  bg='#D9EAD3', fg='#274E13', troughcolor='#93C47D', highlightbackground='#B6D7A8', 
                  activebackground='#6AA84F', length=600)  # Customize the slider's appearance and size
slider.pack(pady=20)  # Place the slider in the window with some vertical space around it

# Set the slider's starting position to 0 (which means the LED is off)
slider.set(0)

# Begin the main event loop to keep the window active until it is closed
try:
    print("Starting the GUI...")  # Indicate that the GUI is being launched
    window.mainloop()  # Run the Tkinter main loop to keep the window open
finally:
    # Clean up the GPIO configuration when the application is closed
    print("Cleaning up GPIO and stopping PWM...")  # Indicate the cleanup process
    pwm.stop()  # Stop the PWM signal to turn off the LED
    GPIO.cleanup()  # Reset GPIO pins to their default state to avoid conflicts later
