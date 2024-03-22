
import cv2
import numpy as np
from collections import deque
import datetime

cap = cv2.VideoCapture('video1.mp4')


if not cap.isOpened():
    print("Error: Couldn;t open the video stream.")
    exit()

fourcc = cv2.VideoWriter_fourcc(*'mp4v')

#video resolution
frame_width = int(cap.get(3))
frame_height = int(cap.get(4))
size = (frame_width, frame_height)

# assuming 60fps, 600 frames = 10 seconds
frame_buffer = deque(maxlen=600)

recording = False

while (cap.isOpened()):
    ret, frame = cap.read()
    if ret:
        cv2.imshow("frame", frame)
        
        if recording:
            frame_buffer.append(frame)

        
        # Press 'r' to start recording last 10 seconds
        key = cv2.waitKey(1) & 0xFF

        if key == ord('r'):
            recording = True
            frame_buffer.clear() # clear the buffer
            print('Recording started...')
        
        # Press 's' to save the last 10 seconds to a file
        elif key == ord('s') and recording:
            # recording = False
            print('Recording stopped and saving last 10 seconds...')

            # Generate a unique filename based on current date and time
            current_time = datetime.datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
            filename = f"output_{current_time}.mp4"
            out = cv2.VideoWriter(filename, fourcc, 60, size)

            for frame_capture in frame_buffer:
                out.write(frame_capture)
            print('last 10 seconds saved successfully.')
            recording= True

      
        # Press 'q' to exit
        if key == ord('q'):
            break
    else:
        break

   
cap.release()
out.release()
cv2.destroyAllWindows()