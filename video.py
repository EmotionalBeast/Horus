# coding: utf-8
#author:Lazy Yao

import os, cv2

class video(object):
	def __init__(self, file_path):
		self.video_file = file_path
		self.cap = cv2.VideoCapture(file_path)

	def get_video_size(self):
		self.file_size = os.path.getsize(self.video_file)/1024 #KB
		return self.file_size / 1024 #MB

	def get_fps(self):
		self.fps = self.cap.get(cv2.CAP_PROP_FPS)
		return self.fps

	def get_pixel_value(self):
		self.width_pixel = self.cap.get(cv2.CAP_PROP_FRAME_WIDTH)
		self.height_pixel = self.cap.get(cv2.CAP_PROP_FRAME_HEIGHT)
		self.pixel_value = str(self.width_pixel) + "x" + str(self.height_pixel)
		return self.pixel_value

	def get_duration(self):
		self.frame_count = self.cap.get(cv2.CAP_PROP_FRAME_COUNT)
		self.duration = self.frame_count / self.fps #s
		return int(self.duration)

	def get_bit_rate(self):
		self.bit_rate = self.file_size * 8 / self.duration
		return int(self.bit_rate)


