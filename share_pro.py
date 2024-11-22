import os
import sys
import http.server
import socketserver
import socket
import fcntl
import struct
import qrcode

__version__ = "0.0.5"

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

def show_qr():
    print("Scan qr code to url in browser :-\n")
    qr = qrcode.QRCode()
    qr.add_data(url)
    qr.print_ascii(tty=True)

class Handler(http.server.SimpleHTTPRequestHandler):
    def __init__(self, *args, **kwargs):
        try:
            super().__init__(*args, directory=DIRECTORY, **kwargs)
        except ConnectionResetError:
            pass
        except BrokenPipeError:
            pass

def run():
    try:
        show_qr()
        http = socketserver.TCPServer((ip, PORT), Handler)

        print("serving at port", f"http://{ip}:{PORT}")
        http.serve_forever()
    except KeyboardInterrupt:
        print("\nStopping share-pro sever....")
        http.server_close()
        sys.exit()

if __name__ == "__main__":
    run()
    