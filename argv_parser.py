#
# File: argv_parser.py
# Brief: OpenCV application providing barcode decoding and OCR text recognition
# Author: alfan-ntu
# Ver.: v. 0.1a
# Date: 2021/7/7
# Revision:
#   1. 2021/7/7: v. 0.1a, project launched
#               - Options parser for CLI input
#

import getopt
import sys


# class OptionContext processes arguments received from the command line
class OptionContext():
    def __init__(self, argv):
        self.argv = argv
        self.video_source = ""
        self.camera_index = 0
        self.window_name = "Barcode reader and OCR"
        self.parse_argv(argv)

    def parse_argv(self, argv):
        try:
            opts, args = getopt.getopt(argv[1:], "hi:w:s:",
                         ["help", "index=", "source=", "window="])
        except getopt.GetoptError:
            self.show_syntax(-1)
            sys.exit(-1)
        for opt, arg in opts:
            if opt in ("-h", "--help"):
                self.show_syntax(0)
                sys.exit(0)
            elif opt in ("-s", "--source"):
                self.video_source = arg
            elif opt in ("-i", "--index"):
                self.camera_index = int(arg)
            elif opt in ("-w", "--window"):
                self.window_name = arg
            else:
                assert False, "Unhandled options"

    def show_syntax(self, con):
        if con == -1:
            print(self.argv[0], "syntax error!")
        print("usage: barcode_ocr.py [option]...[-i camera_index | -f video_source | -w window_name | -h]")
        print("Options:")
        print("\t-s video_source : video streaming source or file")
        print("\t-i cam_index    : Camera index")
        print("\t-w window_name  : Application window name")
        print("\t-h              : Print this syntax information")

    def dump_options(self):
        print("Operation parameters:")
        print(f'\tVideo source name: {self.video_source} of type: {type(self.video_source)}')
        print(f'\tWindow name: {self.window_name} of type: {type(self.window_name)}')
        print(f'\tCamera index: {self.camera_index} of type: {type(self.camera_index)}')
