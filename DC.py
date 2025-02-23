from machine import Pin
import time

# Define stepper motor pins
IN1 = Pin(18, Pin.OUT)
IN2 = Pin(19, Pin.OUT)
IN3 = Pin(21, Pin.OUT)
IN4 = Pin(22, Pin.OUT)

# Step sequence for 28BYJ-48 or similar stepper motor
step_sequence = [
    [1, 0, 0, 1],  # Step 1
    [1, 0, 0, 0],  # Step 2
    [1, 1, 0, 0],  # Step 3
    [0, 1, 0, 0],  # Step 4
    [0, 1, 1, 0],  # Step 5
    [0, 0, 1, 0],  # Step 6
    [0, 0, 1, 1],  # Step 7
    [0, 0, 0, 1]   # Step 8
]

# Function to move stepper motor in a given direction
def step_motor(direction, steps, delay=0.002):
    for _ in range(steps):
        for step in range(8):
            if direction == "CW":  # Clockwise
                seq = step_sequence[step]
            else:  # Anti-Clockwise
                seq = step_sequence[7 - step]
            
            IN1.value(seq[0])
            IN2.value(seq[1])
            IN3.value(seq[2])
            IN4.value(seq[3])
            
            time.sleep(delay)

while True:
    print("Rotating Clockwise")
    step_motor("CW", 512)  # 512 steps = one full rotation (for 28BYJ-48)
    time.sleep(1)

    print("Rotating Anti-Clockwise")
    step_motor("CCW", 512)
    time.sleep(1)
