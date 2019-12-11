# coding: utf-8
#author:Lazy Yao

import os, cv2

class Video(object):
	def __init__(self, file_path):
		self.file_name = file_path.split("/")[len(file_path.split("/"))-1]
		self.cap = cv2.VideoCapture(file_path)

		#video size
		self.file_size = os.path.getsize(file_path) / 1024 #KB

		#FPS
		self.fps = self.cap.get(cv2.CAP_PROP_FPS)

		#pixel value
		self.width_pixel = int(self.cap.get(cv2.CAP_PROP_FRAME_WIDTH))
		self.height_pixel = int(self.cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
		self.pixel_value = str(self.width_pixel) + "x" + str(self.height_pixel)

		#duration
		self.frame_count = self.cap.get(cv2.CAP_PROP_FRAME_COUNT)
		self.duration = self.frame_count / self.fps #s

		#bit rate
		self.bit_rate = self.file_size * 8 / self.duration #kbps

	def get_info(self):
		file_size = self.file_size / 1024 #MB
		file_size = str(round(file_size, 2))
		duration = str(round(self.duration, 2))
		fps = str(int(self.fps))
		bit_rate = str(int(self.bit_rate))
		return [self.file_name, self.pixel_value, file_size, duration, bit_rate, fps ]


