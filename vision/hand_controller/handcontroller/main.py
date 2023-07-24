import cv2 as cv
from handcontroller.tracker import HandTracker
import sys

def run():
    debug = False
    if len(sys.argv) > 1 and sys.argv[1] == "debug":
        debug = True
        
    if debug:    
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
    else:
        print("Not implemented")
        