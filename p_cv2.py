"""
pip install opencv-python
"""

from cv2 import VideoCapture, imshow, waitKey

capture = VideoCapture(0)

while True:
    ok, img = capture.read()
    imshow("Frame", img)
    waitKey(1)

