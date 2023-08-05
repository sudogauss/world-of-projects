import cv2 as cv
from handcontroller.tracker import HandTracker, Direction
import pyautogui as pgui
import sys

def run():
    debug = False
    if len(sys.argv) > 1 and sys.argv[1] == "debug":
        debug = True
        
    cap = cv.VideoCapture(0)
    tracker = HandTracker()
    
    while True:
        _, im = cap.read()
        proc_im = cv.cvtColor(im, cv.COLOR_BGR2RGB)
        
        tracker.update_current_speed_vector(proc_im)
        
        direction = tracker.get_current_direction()
        speed = tracker.get_current_speed()
        
        if direction == Direction.DOWN and speed > 100.0:
            pgui.scroll(-1 * int(speed / 100.0))
        elif direction == Direction.UP and speed > 100.0:
            pgui.scroll(1 * int(speed / 100.0))
            
        if debug:
            tracker.draw_landmarks(im)
            tracker.draw_speed_metrics(im)
            
            cv.imshow("Debug", im)
            cv.waitKey(1)
        