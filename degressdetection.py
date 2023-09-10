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
    image = cv.flip(frame,1)
    image.flags.writeable = False

    # Görüntüden eli yakalayarak referans noktalarının kordinatlarını liste şeklinde result değişkenine aktarır
    results = hands.process(Rgb)
    image.flags.writeable = True

    # Görüntüyü tekrar BGR formatına döndürür
    image = cv.cvtColor(image, cv.COLOR_RGB2BGR)    

    if results.multi_hand_landmarks:
        for id, hand in enumerate(results.multi_hand_landmarks):
            mp_drawing.draw_landmarks(image, hand, mp_hands.HAND_CONNECTIONS,
                            mp_drawing.DrawingSpec(color=(255,0,0), thickness=2, circle_radius=4),
                            mp_drawing.DrawingSpec(color=(0,0,250), thickness=2, circle_radius=2),
                            )
        # DrawingSpec ---> (color=BGR, daire kalınlığı/çizgi kalınlığı, daire çapı/none)

    cv.imshow("cam", image)

    if cv.waitKey(1) == ord("q"):
        break

cap.release()
cv.destroyAllWindows()