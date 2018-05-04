#!/usr/bin/python

import cv2
import numpy as np
import sys

if len(sys.argv) < 4:
  print("You need to enter 3 numbers")
  sys.exit()

# Can have flag for BGR and switch the fields around
rgb = np.uint8([[[int(str(sys.argv[1]).replace(',', '')), int(
    str(sys.argv[2]).replace(',', '')), int(str(sys.argv[3]).replace(',', ''))]]])
cvt = cv2.cvtColor(rgb, cv2.COLOR_RGB2HSV)

# rgb = np.uint8([[[int(sys.argv[3]), int(sys.argv[2]), int(sys.argv[1])]]])
# cvt = cv2.cvtColor(rgb, cv2.COLOR_BGR2HSV)

print("HSV Colors", str(cvt[0][0][0]) + ', ' + str(cvt[0][0][1]) + ', ' + str(cvt[0][0][2]))