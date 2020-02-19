# coding: utf-8

from PIL import Image
import cv2, os, time

# img = Image.open("./workspace/view.jpg")
# print(os.path.getsize("./workspace/view.jpg")/(1000*1000))

# print(img.size)
# print(img.format)
# # print(img.info)
# dpi = img.info["dpi"]
# print(img.info["dpi"])
# print()

# #码率计算公式：file_size(kb)*8/time(s)
# """
# get(self, propId)
# propId:
# cv2.CAP_PROP_POS_MSEC 视频
# cv2.CAP_PROP_FPS 帧率
# cv2.CAP_PROP_FRAME_COUNT 帧数
# cv2.CAP_PROP_FRAME_WIDTH 帧的高度
# cv2.CAP_PROP_FRAME_HEIGHT 帧的宽度
# """
# cap = cv2.VideoCapture("./workspace/ViewRecorder_tmp.mp4")
# print(cap.get(cv2.CAP_PROP_FPS))
# print(cap.get(cv2.CAP_PROP_FRAME_COUNT))
# print(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
# print(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))

# # img = cv2.imread("./workspace/view.jpg", 1)
# # cv2.imwrite("./workspace/view_3.jpg",img)
# video_duration = float(cap.get(7)/cap.get(5)) #视频时长
# print(video_duration)
# def bit(path):
# 	size = os.path.getsize(path)
# 	print(size/1024/1024)
# 	bit_rate = size/1024*8/video_duration
# 	print(bit_rate)
# 	print()

# bit("./workspace/ViewRecorder_tmp.mp4")
# bit("./workspace/AnimatedStory.mov")
# bit("./workspace/IMG_1348.mp4")
# content = 'a.v'
# print(len(content))

# print(time.time())
# print(time.localtime(time.time()))
# print(time.strftime('%Y_%m_%d_%H_%M', time.localtime(time.time())))




file = os.getcwd() + "/workspace"
for root, dirs, files in os.walk(file):
	for file in files:
		tmp = root + "/" + file
		print(tmp)
		print("mtime:", os.path.getmtime(tmp))
		print("ctime:", os.path.getctime(tmp))
		print()

# l1 = [1,3,4]
# tmp = l1[0]
# l1[0] = l1[1]
# l1[2] = tmp
# print(l1)
