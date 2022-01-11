import time
import robomaster
from robomaster import conn
from MyQR import myqr
from PIL import Image


QRCODE_NAME = "qrcode.png"

if __name__ == '__main__':

    helper = conn.ConnectionHelper()
    info = helper.build_qrcode_string(ssid="WiFi-Name", password="wifi-password")
    myqr.run(words=info)
    time.sleep(1)
    img = Image.open(QRCODE_NAME)
    img.show()  # This will display the QR code on-screen
                # Press the "Connect" button besides the "Wi-Fi or Router" slider
                # Place the QR code in front of the camera and wait for connection
                # There will be a voice feedback
    if helper.wait_for_connection():
        print("Connected!")
    else:
        print("Connect failed!")
