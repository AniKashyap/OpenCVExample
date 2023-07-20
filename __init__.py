import cv2
import processing

if __name__ == "__main__":
    processor = processing.Processing()
    print(cv2.__version__)
    # processor.gen_board()
    video = cv2.VideoCapture(0)
    while True:
        ret, frame = video.read()
        if not ret:
            print("Cannot get camera read")
            exit()
        cv2.imshow("frame", processor.find_corners(frame, True))
        if cv2.waitKey(1) == ord("q"):
            break
    exit()
