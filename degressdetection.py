import mediapipe as mp
import cv2 as cv
import numpy as np
from cvzone.SerialModule import SerialObject

cap = cv.VideoCapture(0)

mp_drawing = mp.solutions.drawing_utils
mp_hands = mp.solutions.hands
hands = mp_hands.Hands()
