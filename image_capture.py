#
# File: image_capture.py
# Brief: OpenCV application providing barcode decoding and OCR text recognition
# Author: alfan-ntu
# Ver.: v. 0.1a
# Date: 2021/7/7
# Revision:
#   1. 2021/7/7: v. 0.1a, project launched
#               - CLI, mouse event handler framework created, ROI setup
#
# ToDo's :
#   1) Starts a new thread to decode the contents in ROI
#
import cv2
from argv_parser import OptionContext


class ImageCapture():
    def __init__(self, opt_context):
        self.opt_context = opt_context
        # video_source configuration is of higher priority compared to the local webcams if both are specified in
        # the command input
        if self.opt_context.video_source != "":
            self.cap = cv2.VideoCapture(self.opt_context.video_source)
        else:
            self.cap = cv2.VideoCapture(self.opt_context.camera_index)
        # self.cap = cv2.VideoCapture(self.opt_context.camera_index)
        self.construct_ok, self.frame = self.cap.read()
        self.height = self.frame.shape[0]
        self.width = self.frame.shape[1]
        self.roi = []
        self.vertex1_set = False
        self.roi_set = False
        cv2.namedWindow(self.opt_context.window_name)
        cv2.setMouseCallback(self.opt_context.window_name, self.mouse_event_handler)

    def start(self):
        if not self.cap.isOpened():
            return -1
        print("Starting capturing....")
        while self.cap.isOpened():
            ret, self.frame = self.cap.read()
            if ret:
                if len(self.roi) == 2:
                    self.frame = cv2.rectangle(self.frame, self.roi[0], self.roi[1], (0,255,255),1)
                cv2.imshow(self.opt_context.window_name, self.frame)
            # if self.roi_set:
            #     cropped_img = self.frame[self.roi[0][0]:self.roi[1][0], self.roi[0][1]:self.roi[1][0]]
            #     cv2.imshow("Cropped Window", cropped_img)
            #     self.roi_set = False
            k = cv2.waitKey(10)
            if k & 0xFF == ord('q'):
                self.release()
                break
            elif k & 0xFF == ord('c'):
                self.reset_roi()

    def release(self):
        print("Releasing resources...")
        self.cap.release()
        cv2.destroyAllWindows()

    def mouse_event_handler(self, event, x, y, flag, params):
        if event == cv2.EVENT_LBUTTONDOWN:
            self.reset_roi()
            self.roi.append((x, y))
            self.vertex1_set = True
        elif event == cv2.EVENT_LBUTTONUP:
            # self.roi.append((x, y))
            self.display_roi_coordinate()
            self.roi_set = True
        elif event == cv2.EVENT_MOUSEMOVE:
            if self.vertex1_set and not self.roi_set:
                if len(self.roi) == 1:
                    self.roi.append((x, y))
                else:
                    self.roi[1] = (x, y)
        else:
            print("Mouse misc. events")

    def display_roi_coordinate(self):
        if len(self.roi)<2:
            return
        print(f'vertex1: ({self.roi[0][0]},{self.roi[0][1]}) to ({self.roi[1][0]},{self.roi[1][1]})')

    def reset_roi(self):
        self.roi_set = False
        self.vertex1_set = False
        self.roi.clear()






