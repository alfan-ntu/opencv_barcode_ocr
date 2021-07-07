#
# File: barcode_cor.py
# Brief: OpenCV application providing barcode decoding and OCR text recognition
# Author: alfan-ntu
# Ver.: v. 0.1a
# Date: 2021/7/7
# Revision:
#   1. 2021/7/7: v. 0.1a, project launched
#
import sys
from argv_parser import OptionContext
from image_capture import ImageCapture


def main(argv):
    opt_context = OptionContext(argv)
    opt_context.dump_options()
    img_cap = ImageCapture(opt_context)
    if not img_cap.construct_ok:
        print("Unable to create capture object")
        exit(-1)
    cap_ret = img_cap.start()
    if cap_ret == -1:
        print("Video capture cannot be started!")


if __name__ == "__main__":
    main(sys.argv[0:])