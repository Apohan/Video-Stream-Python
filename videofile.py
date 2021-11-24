import os
import cv2
from glob import glob

def videocikart():

    while True:
        videolist = sorted(glob(r"VİDEOS\*.mp4"))

        for video in videolist:
            cv2.namedWindow("frame", cv2.WND_PROP_FULLSCREEN)
            cv2.setWindowProperty('frame', cv2.WND_PROP_FULLSCREEN, cv2.WINDOW_FULLSCREEN)
            cv2.resizeWindow('frame', 1080, 720)
            cap = cv2.VideoCapture(video)


            while (cap.isOpened()):
                ret, frame = cap.read()

                if ret:
                    cv2.imshow('frame', frame)

                elif ret is False:
                    cv2.waitKey(10)
                    cap.release()

                else:
                    print('video not found')
                    cap.set(cv2.CAP_PROP_POS_FRAMES, 0)

                if (cv2.waitKey(1) & 0xFF == ord('q')):

                    break

        cap.release()
        cv2.destroyAllWindows()

videocikart()


