# coding:utf-8

import cv2
import sys
# from PIL import Image


def CatchUsbVideo(window_name, camera_idx):
    cv2.namedWindow(window_name)

    # 捕捉摄像头
    cap = cv2.VideoCapture(camera_idx)

    while cap.isOpened():
        ok, frame = cap.read()  # 读取一帧数据
        if not ok:
            break
        # 显示图像
        cv2.imshow(window_name, frame)
        c = cv2.waitKey(10)
        if c & 0xFF == ord('q'):
            break

            # 释放摄像头并销毁所有窗口
    cap.release()
    cv2.destroyAllWindows()


if __name__ == '__main__':
    CatchUsbVideo("opencam", 0)