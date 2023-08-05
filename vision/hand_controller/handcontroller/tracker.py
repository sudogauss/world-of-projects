import cv2 as cv
import mediapipe as mp
from enum import Enum

mp_hands = mp.solutions.hands
mp_draw = mp.solutions.drawing_utils

class Direction(Enum):
    NONE = 1
    UP = 2
    LEFT = 3
    DOWN = 4
    RIGHT = 5
    

def direction_to_str(direction: Direction) -> str:
    if direction == Direction.NONE:
        return "none"
    elif direction == Direction.UP:
        return "up"
    elif direction == Direction.DOWN:
        return "down"
    elif direction == Direction.LEFT:
        return "left"
    elif direction == Direction.RIGHT:
        return "right"
    

class HandTracker():
    
    def __init__(self, 
                 max_hands_num: int =  1, 
                 min_detection_confidence: float = 0.7,
                 speed_measurement_frames: int = 5,
                 threshold_speed: float = 1.2):
        self.hand_detector = mp_hands.Hands(max_num_hands=max_hands_num, min_detection_confidence=min_detection_confidence)
        self.speed_measurement_frames = speed_measurement_frames
        self.threshold_speed = threshold_speed
        self.__curent_direction = Direction.NONE
        self.__current_speed = 0.0
        self.__positions = []
        
    def get_current_speed(self) -> float:
        return self.__current_speed
    
    def get_current_direction(self) -> Direction:
        return self.__curent_direction

    def __infer(self, image: any) -> any:
        results = self.hand_detector.process(image)
        return results.multi_hand_landmarks
    
    def __norm(self, x, y):
        if len(x) != len(y):
            return None
        
        _sum = 0
        for i in len(x):
            _sum += ((x[i] - y[i]) ** 2)
            
        return _sum
    
    def __abs(self, a):
        if a < 0:
            return -a
        else:
            return a
        
    def __get_speed_in_direction(self) -> float:
        if len(self.__positions) <= 1:
            return
        
        if self.__curent_direction == Direction.LEFT:
            return (self.__positions[-1][0] - self.__positions[0][0])
        elif self.__curent_direction == Direction.RIGHT:
            return (self.__positions[0][0] - self.__positions[-1][0])
        elif self.__curent_direction == Direction.DOWN:
            return (self.__positions[-1][1] - self.__positions[0][1])
        elif self.__curent_direction == Direction.UP:
            return (self.__positions[0][1] - self.__positions[-1][1])
            
    def draw_landmarks(self, image: any) -> None:
        res = self.__infer(image)
        if res:
            for hand_lms in res:
                mp_draw.draw_landmarks(image, hand_lms, mp_hands.HAND_CONNECTIONS)
            
    def draw_speed_metrics(self, image: any) -> None:
        cv.putText(image, str(self.__current_speed), (50, 50), cv.FONT_HERSHEY_COMPLEX, 1, (255, 0, 0), 2, cv.LINE_AA)
        cv.putText(image, direction_to_str(self.__curent_direction), (50, 150), cv.FONT_HERSHEY_COMPLEX, 1, (255, 0, 0), 2, cv.LINE_AA)
    
    def update_current_speed_vector(self, image: any) -> None:
        res = self.__infer(image)
        if res:
            for hand_lms in res:
                h, w, _ = image.shape
                _cnt = 0
                cx, cy = 0, 0
                for id, lm in enumerate(hand_lms.landmark):
                    if 5 <= id <= 8:
                        cx += int(lm.x * w)
                        cy += int(lm.y * h)
                        _cnt += 1
                        
                px, py = int(cx / _cnt), int(cy / _cnt)
                
                if len(self.__positions) < self.speed_measurement_frames:
                    self.__positions.append((px, py))
                else:
                    _ = self.__positions.pop(0)
                    self.__positions.append((px, py))
        else:
            if len(self.__positions) > 0:
                self.__positions.pop(0)
                    
        if len(self.__positions) <= 1:
            return
        
        axis = 0
        if self.__abs(self.__positions[-1][0] - self.__positions[-2][0]) < self.__abs(self.__positions[-1][1] - self.__positions[-2][1]):
            axis = 1
            
        if axis == 0:
            if self.__positions[-1][0] - self.__positions[-2][0] <= 0:
                self.__curent_direction = Direction.RIGHT
            else:
                self.__curent_direction = Direction.LEFT
        else:
            if self.__positions[-1][1] - self.__positions[-2][1] <= 0:
                self.__curent_direction = Direction.UP
            else:
                self.__curent_direction = Direction.DOWN
                
        self.__current_speed = self.__get_speed_in_direction()
        
        
                