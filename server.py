import socket
import threading
from time import *
import time
from picarx import Picarx
from pygame import mixer
mixer.init()

px = Picarx()

if __name__ == "__main__":
    try:
        pan_angle = 0
        tilt_angle = 0
    
        port = 5555
        server = "192.168.1.71"
        HEADER = 64
        ADDR = (server, port)
        FORMAT = "utf-8"
        DISCONNECT = "!bye"

        # Creating a socket, picking the family, pick a type
        server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        server_socket.bind(ADDR)

        servoangle = 3

        def handle_client(conn, addr):
            global servoangle
            connected = True
            while connected:
                msg_length = conn.recv(HEADER).decode(FORMAT)
                if msg_length != "":
                    msg_length = int(msg_length)
                    msg = conn.recv(msg_length).decode(FORMAT)

  
                    if msg == "forward":

                        px.forward(5)
                        time.sleep(1)
                        px.stop()
                        #tab

                    if msg == "backward":
                        px.backward(5)
                        time.sleep(1)
                        px.stop()
                        #tab

                    if msg == "right":
                        servoangle += 4
                        px.set_dir_servo_angle(servoangle)

                    if msg == "left":
                        servoangle -= 4
                        px.set_dir_servo_angle(servoangle)

                    if msg == "alarm_sound":
                        mixer.music.load("sounds/sounds/sounds/alarm.wav")

            conn.close()


        def start():
            server_socket.listen()
            print(server)
            print("SERVER STARTING...")
            while True:
                conn, addr = server_socket.accept()  # Waits for a connection, when a connection occurs it will store the data
                thread = threading.Thread(target=handle_client, args=(conn, addr))
                thread.start()

        start()

    finally:
        px.set_cam_tilt_angle(0)
        px.set_cam_pan_angle(0)
        px.set_dir_servo_angle(0)
        px.stop()
        sleep(.2)
