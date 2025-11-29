import cv2
from hand_tracker import HandTracker
from cursor_controller import CursorController

tracker = HandTracker(maxHands=1)
cursor = CursorController()

cap = cv2.VideoCapture(0)

while True:
    success, img = cap.read()
    img = tracker.findHands(img)
    lmList = tracker.getLandmarks(img)

    h, w, c = img.shape

    if len(lmList) > 8:
        x1, y1 = lmList[8]   # Index finger tip
        x2, y2 = lmList[4]   # Thumb tip

        # Cursor movement
        sx, sy = cursor.mapToScreen(x1, y1, w, h)
        cursor.move(int(sx), int(sy))


        # Click gesture
        d = cursor.distance(x1, y1, x2, y2)
        cursor.click_if_needed(d)

    cv2.imshow("Hand Gesture Control", img)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
