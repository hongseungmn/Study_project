import cv2
import mediapipe as mp

mp_draw = mp.solutions.drawing_utils
mp_hand = mp.solutions.hands

video = cv2.VideoCapture(0)

with mp_hand.Hands(min_detection_confidence=0.5,
                    min_tracking_confidence=0.5) as hands:
    while True:
        ret,image = video.read()
        image.flags.writeable = False
        results = hands.process(image)
        image.flags.writeable= False
        result = cv2.cvtColor(image,cv2.COLOR_BAYER_BG2BGR)
        if result.multi_hand_landmarks:
            for hand_landmark in result.multi_hand_landmarks:
                mp_draw.draw_landmarks(image, hand_landmark, mp_hand.HAND_CONNECTIONS)
                
        
        cv2.imshow("Frame",image)
        k = cv2.waitKey(1)
        if k==ord('q'):
            break

video.release()
cv2.destroyAllWindows()
        
    