import cv2
import processing

if __name__ == "__main__":
    processor = processing.Processing()
    print(cv2.__version__)
    processor.gen_board()
    video = cv2.VideoCapture(0)
    target_ids = [1, 2, 3, 4, 5, 6, 7, 8]

    while True:
        if not processor.ids_filtered:
            ret, frame = video.read()
            processor.get_corners(frame)
            processor.filter_ids(target_ids)
            cv2.imshow("camera", processor.process_frame(frame, True))
            print("Wassup")
            if not ret:
                print("Cannot get camera read")
                exit()
            if cv2.waitKey(1) == ord("q"):
                break
        else:
            ret, frame = video.read()
            if not ret:
                print("Cannot get camera read")
                exit()
            cv2.imshow("camera", processor.process_frame(frame, True))
            if cv2.waitKey(1) == ord("q"):
                break

    exit()
