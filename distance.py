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
    
    # Wait for Echo to go catch the sounds emitted by the Trig.
    while echo_pin.value() == 0:
        pulse_start = time.ticks_us()
    
    # Wait for Echo to stop reciving the sound.
    while echo_pin.value() == 1:
        pulse_end = time.ticks_us()
    
    # The pulse duration:
    pulse_duration = time.ticks_diff(pulse_end, pulse_start)
    
    # Since the speed of sound is ~343 m/s, which is 34300 cm/s,
    # however, the time we multiply by is in microseconds, so we adjust the speed accordingly.
    # We divide by 2 since the sound had to travel there and back, which accounts for twice the distance.
    distance = (pulse_duration * 0.0343) / 2
    
    return (distance)

def person_detected():

    # If a patient is within 100cm of the device, then he is using the device.
    return (measure_distance() <= 100)

# Run this file directly to test this sensor exclusively.
if (__name__ == "__main__"):

    try:

        while (True):

            print(f"Distance: {distance: .1f} cm")

            if (person_detected()):
                print("Person detected!")

            time.sleep(1)

    except KeyBoardInterrupt:
        print("Interrupted by User.")

    finally:

        # Reset the Trig.
        trigger_pin.value(0)
