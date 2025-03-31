import machine
import utime

#Green_LED = machine.Pin(15, machine.Pin.OUT)

def Pulse_Ox():
  
    IR_PT = machine.ADC(27)
    RED_PT = machine.ADC(26)

    RED_data = []
    IR_data = []
    R_data = []
    i = 0
    j = 0
    total = 0
    calib = 0
    ref_index = 0
    f = open("data.txt","r")
    calib = float(f.readline())
    #print (calib)
    f.close()
    #f = open("data.txt","w")

    while i<100:
        #next line measures the voltage between the resistor and the phototransistor
        IR = IR_PT.read_u16()
        RED = RED_PT.read_u16()
        #print(IR, RED)
        R = RED/IR
        R_data.append(R)
        #print (R_data[i])
        RED_data.append(RED)
        IR_data.append(IR)
        utime.sleep(0.01) #modify this value to adjust the length of test, higher gives more consistency
        i += 1
    for x in R_data:
        total = total + (R_data[int(x)])
        j+=1
    ref_index = total/j
    """f.write(str(ref_index))
    f.close()"""
    #print (j, calib)
    SpO2 = -25*(total/j/calib)+124
    return SpO2
