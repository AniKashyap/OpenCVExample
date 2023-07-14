import os.path
from typing import List
import cv2
from cv2 import aruco
import numpy


class Processing:
    _all_charuco_corners: List[numpy.ndarray] = []
    _all_charuco_ids: List[numpy.ndarray] = []
    _imsize = None

    # create instance of the class
    def __init__(self) -> None:
        self._aruco_dict = aruco.getPredefinedDictionary(aruco.DICT_5X5_1000)
        self._aruco_detector = aruco.ArucoDetector(self._aruco_dict)
        self._charuco_board = aruco.CharucoBoard(
            (10, 9), 0.030, 0.023, self._aruco_dict)
        self.corners = None
        self.ids = None
        self.filtered_corners = []
        self.filtered_ids = []
        self.ids_filtered = False

    # creates the checkerboard
    def gen_board(self):
        img = cv2.aruco.drawPlanarBoard(self._charuco_board, (1280, 720), 0, 1)
        cv2.imshow("checker board", img)

    def filter_ids(self, target_ids: List[int], ):

        # Filter the detected markers based on target_ids
        for corner, marker_id in zip(self.corners, self.ids):
            if marker_id in target_ids:
                self.filtered_corners.append(corner)
                self.filtered_ids.append(marker_id)

        self.ids_filtered = True

    def get_corners(self, image: numpy.array):
        (self.corners, self.ids, self.rejected) = self._aruco_detector.detectMarkers(image)

    def get_filtered_corners(self) -> []:
        return self.filtered_corners

    def process_frame(self, image: numpy.array, save: bool) -> numpy.array:
        if self._imsize is None:
            self._imsize = (image.shape[0], image.shape[1])

        self.get_corners(image)

        if len(self.filtered_corners) > 0:
            cv2.aruco.drawDetectedMarkers(image, self.filtered_corners)

            filtered_ids = numpy.array(self.filtered_ids)  # Convert to a NumPy array to prevent overload error

            (retval, charuco_corners, charuco_ids) = cv2.aruco.interpolateCornersCharuco(
                self.filtered_corners, filtered_ids, image, self._charuco_board)

            if retval:
                cv2.aruco.drawDetectedCornersCharuco(image, charuco_corners, charuco_ids)
                if save:
                    self._all_charuco_ids.append(charuco_ids)
                    self._all_charuco_corners.append(charuco_corners)
                    print("Saved calibration frame")

        return image
