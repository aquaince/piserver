import pygame
from pygame import mixer
import pyttsx3
from time import sleep
from robot.server_managment import Server
from robot.robot_actions import Robot

pygame.init()
pygame.mixer.init()

class Main:
    def __init__(self):
        self.engine = pyttsx3.init()
        mixer.init()
        self.server = Server(host="192.168.1.71", port=5555)
        self.robot = Robot()

        self.start_sound = pygame.mixer.Sound("sounds/sounds/sounds/start.wav")
        self.over_sound = pygame.mixer.Sound("sounds/sounds/sounds/over.wav")
        self.alarm_sound = pygame.mixer.Sound("sounds/sounds/sounds/quack.mp3")

    def start(self):
        try:
            self.start_sound.play()
            self.server.start()
        finally:
            self.cleanup()

    def cleanup(self):
        self.robot.set_servo_angle(0)
        self.robot.set_camera_angles(0, 0)
        self.robot.px.stop()
        sleep(0.2)
        self.over_sound.play()


if __name__ == "__main__":
    main = Main()
    main.start()
