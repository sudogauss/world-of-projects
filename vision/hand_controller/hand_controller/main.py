import cv2 as cv
from hand_controller.tracker import HandTracker

def run():
    cap = cv.VideoCapture(0)
    tracker = HandTracker()
    while True:
        ret, im = cap.read()
        proc_im = cv.cvtColor(im, cv.COLOR_BGR2RGB)
        
        tracker.update_current_speed_vector(proc_im)
        tracker.draw_landmarks(im)
        tracker.draw_speed_metrics(im)
        
        cv.imshow("Main", im)
        cv.waitKey(1)