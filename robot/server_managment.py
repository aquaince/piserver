import socket
import threading
import subprocess
import time
from robot.robot_actions import Robot  
from robot.micrecorder import *
import pyttsx3

class Server:
    def __init__(self, host, port, header=64, format="utf-8", disconnect_cmd="!bye"):
        self.host = host
        self.port = port
        self.header = header
        self.format = format
        self.disconnect_cmd = disconnect_cmd
        self.server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.server_socket.bind((self.host, self.port))

        # Robot
        self.servoangle = 3
        self.pan_angle = 0
        self.tilt_angle = 0

    def cleanup(self):
        self.robot.set_servo_angle(0)
        self.robot.set_camera_angles(0, 0)
        self.robot.px.stop()
        time.sleep(0.2)

    def start(self):
        self.robot = Robot()
        self.server_socket.listen()
        print(f"Server started on {self.host}:{self.port}...")
        while True:
            conn, addr = self.server_socket.accept()
            print(f"Connected to {addr}")
            threading.Thread(target=self.handle_client, args=(conn, addr)).start()

    def handle_client(self, conn, addr):
        print(f"New connection from {addr}")
        connected = True
        try:
            while connected:
                msg_length = conn.recv(self.header).decode(self.format)
                if msg_length:
                    msg_length = int(msg_length)
                    msg = conn.recv(msg_length).decode(self.format)
                    print(f"Received message: {msg}")
                    if msg == self.disconnect_cmd:
                        connected = False
                    if msg == "forward":
                        self.robot.move_forward()
                    if msg == "backward":
                        self.robot.move_backward()

                    if msg == "right":
                        self.servoangle += 3

                    if msg == "left":
                        self.servoangle -= 3

                    if msg == "camera_up":
                        self.tilt_angle += 4
                    if msg == "camera_down":
                        self.tilt_angle -= 4
                    if msg == "camera_left":
                        self.pan_angle += 4
                    if msg == "camera_right":
                        self.pan_angle -= 4

                    if msg == "over_sound":
                        connected = False
                        subprocess.call("shutdown.sh")

                    if msg == "alarm_sound":
                        # Ensure alarm_sound is properly initialized
                        alarm_sound.play()
                    if msg.startswith("word"):
                        print(msg[4:])
                        # Ensure engine is properly initialized
                        engine.say(msg[4:])
                        engine.runAndWait()

                    if msg == "record":
                        record(5)

                    self.robot.set_servo_angle(self.servoangle)
                    self.robot.set_camera_angles(self.pan_angle, self.tilt_angle)
        except Exception as e:
            print(f"Error in handling client: {e}")
        finally:
            conn.close()
