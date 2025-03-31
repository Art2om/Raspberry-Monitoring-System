import network
import socket
import time
from website import *
from temperature import temperature
from oxymeter import Pulse_Ox
from distance import person_detected

# Encrypt this in the actual final product.
ssid = 'Local_Network'
password = 'Local Only'

def generate_html():

    temperature = temperature()

    try:
        oxygination = Pulse_Ox()
    except:
        oxygination = "Error"

    user_active = person_detected()

    # Format the current time to be displayed.
    current_time = time.localtime()
    time_string = "{:02d}:{02d}:{02d}".format(current_time[3], current_time[4], current_time[5])

    # Create the HTML with the sensor data.
    HTML = f"""
    <!DOCTYPE html>

    <html>
        <head>
            <title>Patient Status:</title>
            <meta http-equiv = "refresh" content = "10">
        </head>
        
        <body>
            <h1>Local Patient Status:</h1>
            <p>Last Updated: {time_sting}</p>
            <ul>
                <li>Temperature: {temperature:.1f} °C</li>
                <li>SpO2 Level: {oxygination}</li>
                <li>Patient Present: {user_active}</li>
            </ul>
        </body>
    </html>
    """

    return (HTML)


def application():

    # Create an Access Point.
    ap = network.WLAN(network.AP_IF)
    ap.config(essid = ssid, password = password)
    ap.active(True)

    while (not ap.active()):

       print("Unable to host an access point.")
       pass

    print("Access point created.")
    print(ap.ifconfig())

    # Socket server creation:
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.bind(('', 80))
    s.listen(5) # Maximum number of requests that can be queued

    try:
       while (True):
        
            connection, address = s.accept()
            print(f"Connection from {address}")

            request = connection.recv(1024)
            request = str(request)
            print("User Request: " + request)

           response = generate_html()

            connection.send("HTTP/1.1 200\n")
            connection.send("Conent-Type: text / html\n")
            connection.send("Closing the Connection.\n\n")
            connection.send(response)

            connection.close()

    except Exception as err:
        print(f"Occured an error: {err}")

    finally:
        
        s.close()
        ap.active(False)

if (__name__ == "__main__"):
    application()

