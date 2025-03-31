# This is the motion sensor logic.

import machine
import time

echo_pin = machine.Pin(0, machine.Pin.IN)       # Pin 1 is GP0 for ECHO
trigger_pin = machine.Pin(1, machine.Pin.OUT)   # Pin 2 is GP1 for TRIG (trigger)

def measure_distance():

    # Set the trigger to LOW, this cleans any data for this iteration.
    trigger_pin.value(0)
    time.sleep_us(2)
    
    # Send a pulse to the trigger, so it fires.
    trigger_pin.value(1)
    time.sleep_us(10)
    trigger_pin.value(0)
    
    # Wait for echo to go high
    while echo_pin.value() == 0:
        pulse_start = time.ticks_us()
    
    # Wait for echo to go low
    while echo_pin.value() == 1:
        pulse_end = time.ticks_us()
    
    # The pulse duration:
    pulse_duration = time.ticks_diff(pulse_end, pulse_start)
    
    # Speed of sound is 343 m/s or 34300 cm/s
    # Distance = (Time × Speed) / 2 (round trip)

    # Since the speed of sound is ~343 m/s, which is 34300 cm/s,
    # however, the time we multiply by is in microseconds, so we adjust the speed accordingly.
    distance = (pulse_duration * 0.0343) / 2
    
    return (distance)

try:

    while True:

        distance = measure_distance()
        print(f"Distance: {distance:.1f} cm")
        
        if (distance <= 100):
            print("Person detected.")
        
        time.sleep(1)
        
except KeyboardInterrupt:
    print("Test stopped by user")

finally:

    # Reset the trigger.
    trigger_pin.value(0)

# I need to return out of this file a boolean when a person is detected.
