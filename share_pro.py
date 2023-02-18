import threading
import sys
import os
import http.server
import socketserver
import socket
import fcntl
import struct
import qrcode
import tkinter as tk
from PIL import Image, ImageTk


__version__ = "0.0.1"

def get_ip_address(ifname):
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    return socket.inet_ntoa(fcntl.ioctl(
        s.fileno(),
        0x8915,
        struct.pack('256s', bytes(ifname[:15], 'utf-8'))
    )[20:24])

ip = get_ip_address('wlan0')

PORT = 5050

url = f"http://{ip}:{PORT}"

DIRECTORY = os.getcwd()

class Handler(http.server.SimpleHTTPRequestHandler):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, directory=DIRECTORY, **kwargs)

class HttpServerThread(threading.Thread):
    def run(self):

        http = socketserver.TCPServer((ip, PORT), Handler)

        print("serving at port", f"http://{ip}:{PORT}")
        http.serve_forever()

class TkinterThread(threading.Thread):
    def run(self):

        root = tk.Tk()

        qr = qrcode.make(url)

        # Convert the PIL Image object to a Tkinter PhotoImage object
        img = ImageTk.PhotoImage(qr)

        # Create a new Tkinter window to display the QR code
        root.geometry("%dx%d" % (qr.size[0] + 10, qr.size[1] + 10))

        # Add the QR code to a Tkinter Label widget
        label = tk.Label(root, image=img)
        label.image = img
        label.pack()

 
        root.mainloop()

def run():
    # starting threads
    http_thread = HttpServerThread()
    http_thread.start()

    tk_thread = TkinterThread()
    tk_thread.start()

    try:
        tk_thread.join()
    except KeyboardInterrupt:
        sys.exit()

    try:
        http_thread.join()
    except KeyboardInterrupt:
        sys.exit()

if __name__ == "__main__":
    run()
    