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

# List
serial= []
son_list= [0,0,0,0,0]
total_list= [0,0,0,0,0]
joint_list = [[4,3,2,1,0],[8,7,6,5],[12,11,10,9],[16,15,14,13],[20,19,18,17]]

# Variables
s = 0

def finger_angles(image, results, joint_list):
    for hand in results.multi_hand_landmarks:
        
        serial.clear()

        for joint in joint_list:            
            a = np.array([hand.landmark[joint[0]].x, hand.landmark[joint[0]].y]) # üst
            b = np.array([hand.landmark[joint[1]].x, hand.landmark[joint[1]].y]) # orta
            c = np.array([hand.landmark[joint[2]].x, hand.landmark[joint[2]].y]) # en alt
            d = np.array([hand.landmark[joint[3]].x, hand.landmark[joint[3]].y]) # avuc boğum

            radians = np.arctan2(c[1] - b[1], c[0]-b[0]) - np.arctan2(a[1]-b[1], a[0]-b[0])
            angle = np.abs(radians*180.0/np.pi)
            
            if angle > 180.0:
                angle = 360-angle

            # 5 değeri ---> 0-30 derece --> Kapalı
            # 4 değeri ---> 30-60 derece
            # 3 değeri ---> 60-90 derece
            # 2 değeri ---> 90-120 derece
            # 1 değeri ---> 120-150 derece
            # 0 değeri ---> 150-180 derece --> Açık

            
            # Liste parmak sıralaması:
            # [ Baş , İşaret , Orta , Yüzük , Serçe]

            # Baş Parmak - Kapalı
            if joint == joint_list[0]:
                if hand.landmark[joint[4]].x < d[0]:
                    if a[0] < c[0]:
                        serial.append(5)
                        angle = 0

                elif hand.landmark[joint[4]].x > d[0]:
                    if a[0] > c[0]:
                        serial.append(5)
                        angle = 0

            # Diğer parmaklar - Kapalı
            if joint != joint_list[0]:
                    if d[1] < a[1]:
                        serial.append(5)
                        angle = 0

            # Açıların aralığına göre listeye eklenmesi
            if angle != 0:
                
                if 0 <= angle <=30:
                    serial.append(5)
                elif 30 < angle <=60:
                    serial.append(4)
                elif 60 < angle <= 90:
                    serial.append(3)
                elif 90 < angle <= 120:
                    serial.append(2)
                elif 120 < angle <= 150:
                    serial.append(1)
                elif 150 < angle <= 180:
                    serial.append(0)

            cv.putText(image, str(round(angle, 2)), tuple(np.multiply(b, [640, 480]).astype(int)),
                    cv.FONT_HERSHEY_SIMPLEX, 0.5, (255,255,255), 2, cv.LINE_AA)
            
    return serial

while True:
    ret, frame = cap.read()

    # Alınan görüntüyü Mediapipe'ın işlemesi için rgb ye çevirir
    image = cv.cvtColor(frame, cv.COLOR_BGR2RGB)
        
    #Görüntüyü ayna görüntüsünden yansıtara karşılıklı hale getirir
    image = cv.flip(image,1)
    image.flags.writeable = False

    # Görüntüden eli yakalayarak referans noktalarının kordinatlarını liste şeklinde result değişkenine aktarır
    results = hands.process(image)
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
        finger_angles(image, results, joint_list)
        # print(serial)
    cv.imshow("cam", image)

    if cv.waitKey(1) == ord("q"):
        break

cap.release()
cv.destroyAllWindows()