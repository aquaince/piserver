from picarx import Picarx

px = Picarx()

class Robot:
    def __init__(self):
        self.pan_angle = 0
        self. tilt_angle = 0
        servoangle = 3
    
    def forward():
        px.forward(5)
        time.sleep(1)
        px.stop()
    
    def backward():
        px.backward(5)
        time.sleep(1)
        px.stop()

    def right():
        servoangle += 4
        px.set_dir_servo_angle(servoangle)

    def left():
        servoangle -= 4
        px.set_dir_servo_angle(servoangle)
    
    def camera_up():
        if tilt_angle < 90:
            tilt_angle += 4
        
    def camera_down():
        if tilt_angle > -90:
            tilt_angle -= 4

    def camera_left():
        if pan_angle < 90:
            pan_angle += 4

    def camera_right():
        if pan_angle > -90:
            pan_angle -= 4

    



pan_angle = 0
tilt_angle = 0 