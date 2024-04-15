class Robot:
    def __init__(self):
        self.pan_angle = 0
        self.tilt_angle = 0
        self.servoangle = 3
        self.px = Picarx()
        self.server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.server_socket.bind(ADDR)
        self.connected = True