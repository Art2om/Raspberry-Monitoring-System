import machine
import time
import math

adc_pin = machine.ADC(28)

def temperature():

  Read_out = adc_pin.read_u16() # The read out from the ADC pin.
  Resistence = 35400            # The resitence at room temperature.
  Room_temperature = 295.15     # Rooom temperature in Kelvin.
  Beta_constant = 1765.5        # A linear constant found in the data-sheet, (Adjusted slightly for accuracy.)

  # The temperature measured in Celsius by using the beta approximation of the Steinhart-Hart equation.
  temperature = (1 / (1 / Room_temperature + (1 / Beta_constant) * math.log(Read_out / Resistence))) - 273.15

  return (temperature)
