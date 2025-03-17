import network
import socket
import website

# Encrypt this in the actual final product.
ssid = 'Local_Network'
password = 'Local Only'

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
    s.listen(5) # maximum number of requests that can be queued

    try:
       while (True):
        
            connection, address = s.accept()
            print(f"Connection from {address}")

            request = connection.recv(1024)
            request = str(request)
            print("User Request: " + request)

            connection.send("HTTP/1.1 200\n")
            connection.send(website)

            connection.close()

    except Exception as err:
        print(f"Occured an error: {err}")

    finally:
        
        s.close()
        ap.active(False)

if (__name__ == "__main__"):
    application()

