"""
pip install mediapipe

This also uses opencv-python:
    -pip install opencv-python
"""

import mediapipe as mp
import cv2

PARAMETERS = {
    "static_image_mode": False,
    "max_num_hands": 2,
    "min_detection_confidence": 0.5,
    "min_tracking_confidence": 0.5,
}

capture = cv2.VideoCapture(0)

mpHands = mp.solutions.hands
mpDraw = mp.solutions.drawing_utils
hands = mpHands.Hands(PARAMETERS)


while True:
    ok, img = capture.read()

    imgRGB = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    results = hands.process(imgRGB).multi_hand_landmarks

    if results:
        for hand in results:
            mpDraw.draw_landmarks(img, hand, mpHands.HAND_CONNECTIONS)

    cv2.imshow("Frame", img)
    cv2.waitKey(1)
