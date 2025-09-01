import tkinter as tk
import RPi.GPIO as GPIO

# Set GPIO mode to BCM
GPIO.setmode(GPIO.BCM)

# Define GPIO pins for LEDs
pins = [17, 27, 22]
pwms = []

# Setup each pin and initialize PWM
for pin in pins:
    GPIO.setup(pin, GPIO.OUT)
    pwm = GPIO.PWM(pin, 100)  # 100Hz frequency
    pwm.start(0)              # Start with 0% duty cycle (LED off)
    pwms.append(pwm)

# Create GUI window
root = tk.Tk()
root.title("LED Intensity Controller")

# Function to update PWM duty cycle
def update_pwm(index, val):
    pwms[index].ChangeDutyCycle(float(val))

# Create sliders for each LED
for i in range(3):
    slider = tk.Scale(root, from_=0, to=100, orient=tk.HORIZONTAL,
                      label=f"LED {i+1} Intensity",
                      command=lambda val, idx=i: update_pwm(idx, val))
    slider.pack()

# Run the GUI loop
try:
    root.mainloop()
finally:
    # Cleanup GPIO on exit
    for pwm in pwms:
        pwm.stop()
    GPIO.cleanup()