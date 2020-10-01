import os
import sys
import glob

folder="/data/data/com.termux/files/home/termux-demos/qpython-opencv-numpy/*.egg"

for file in glob.glob(folder):
    sys.path.append(file)
    
import numpy
import cv