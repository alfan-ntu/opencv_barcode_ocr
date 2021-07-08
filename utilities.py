#
# File: image_capture.py
# Project: OpenCV application providing barcode decoding and OCR text recognition
# Brief: Supporting gadgets
# Author: alfan-ntu
# Ver.: v. 0.1a
# Date: 2021/7/7
# Revision:
#   1. 2021/7/7: v. 0.1a, project launched
#               - CLI, mouse event handler framework created, ROI setup
#


def validate_vertices(v1, v2):
    x1 = v1[0]
    y1 = v1[1]
    x2 = v2[0]
    y2 = v2[1]
    print(f'Coordinates 1: ({v1[0]},{v1[1]})')
    print(f'Coordinates 2: ({v2[0]},{v2[1]})')
    valid = True
    if x1 == x2 or y1 == y2:
        valid = False
    if x1 > x2:
        x = x1
        x1 = x2
        x2 = x
    if y1 > y2:
        y = y1
        y1 = y2
        y2 = y
    w = x2-x1
    h = y2-y1
    return valid, (x1, y1), (x2, y2), w, h


