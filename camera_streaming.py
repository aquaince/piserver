import socket
import struct
import io
import picamera
import time

client_socket = socket.socket()

client_socket.connect(('192.168.1.53', 5555))

connection = client_socket.makefile('wb')
try:
    camera = picamera.PiCamera()
    camera.vflip = True
    camera.resolution = (500, 480)

    camera.start_preview()
    time.sleep(2)

    start = time.time()
    stream = io.BytesIO()

    for foo in camera.capture_continuous(stream, 'jpeg'):
        # Write the length of the image data to the connection
        connection.write(struct.pack('<L', stream.tell()))
        connection.flush()

        # Rewind the stream and write the image data to the connection
        stream.seek(0)
        connection.write(stream.read())

        # Reset the stream for the next capture
        stream.seek(0)
        stream.truncate()

        # Sleep for a short time to control the capture rate
        time.sleep(0.1)

        # Break the loop if capturing for too long (e.g., 30 seconds)
        if time.time() - start > 30:
            break

finally:
    connection.close()
    client_socket.close()

