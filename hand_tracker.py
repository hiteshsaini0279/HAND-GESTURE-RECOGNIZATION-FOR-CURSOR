import mediapipe as mp
import cv2

class HandTracker:
    def __init__(self, maxHands=1):
        self.mpHands = mp.solutions.hands
        self.hands = self.mpHands.Hands(max_num_hands=maxHands)
        self.mpDraw = mp.solutions.drawing_utils

    def findHands(self, img):
        imgRGB = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
        self.results = self.hands.process(imgRGB)

        if self.results.multi_hand_landmarks:
            for handLms in self.results.multi_hand_landmarks:
                self.mpDraw.draw_landmarks(img, handLms, self.mpHands.HAND_CONNECTIONS)
        return img

    def getLandmarks(self, img):
        h, w, c = img.shape
        lmList = []

        if self.results.multi_hand_landmarks:
            hand = self.results.multi_hand_landmarks[0]
            for id, lm in enumerate(hand.landmark):
                cx, cy = int(lm.x * w), int(lm.y * h)
                lmList.append((cx, cy))
        return lmList
