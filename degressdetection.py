import mediapipe as mp
import cv2 as cv
import numpy as np
from cvzone.SerialModule import SerialObject

# OpenCv Webcam Kaynagı
cap = cv.VideoCapture(0)

# Mediapipe Classları
mp_drawing = mp.solutions.drawing_utils
mp_hands = mp.solutions.hands
hands = mp_hands.Hands()

while True:
    ret, frame = cap.read()

    # Alınan görüntüyü Mediapipe'ın işlemesi için rgb ye çevirir
    Rgb = cv.cvtColor(frame, cv.COLOR_BGR2RGB)
        
    #Görüntüyü ayna görüntüsünden yansıtara karşılıklı hale getirir
    image = cv.flip(image,1)
    image.flags.writeable = False

    # Görüntüden eli yakalayarak referans noktalarının kordinatlarını liste şeklinde result değişkenine aktarır
    results = hands.process(Rgb)
    image.flags.writeable = True

    # Görüntüyü tekrar BGR formatına döndürür
    image = cv.cvtColor(image, cv.COLOR_RGB2BGR)    
    