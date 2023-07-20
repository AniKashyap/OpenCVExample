import os.path
from typing import List
import cv2
from cv2 import aruco
import numpy

class Calibration:

    mtx, dist, rvecs, tvecs = cv2.calibrateCamera(objpoints, imgpoints, , None, None):

    nx = 0
    ny = 0

    img = cv2.imread(INSERT_HERE)

    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    ret, corners = cv2.findChessboardCorners(gray, (nx, ny), None)

    if ret is True:
        cv2.drawChessboardCorners(img, (nx, ny), corners, ret)
        cv2.imshow("Chess Board" ,img)
