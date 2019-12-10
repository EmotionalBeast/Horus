#coding: utf-8

import os
from PIL import Image


class Picture(object):
	def __init__(self,file_path):
		self.img = Image.open(file_path)
		self.img_file = file_path

	def get_picture_resolution(self):
		self.width_resolution, self.height_resolution = img.size
		self.resolution = str(self.width_resolution) + "x" + str(self.height_resolution)
		return self.resolution

	def get_picture_size(self):
		self.size = os.path.getsize(self.img_file) / 1024 #KB
		return self.size / 1024 #MB	

	def get_picture_dpi(self):
		return self.img.info["dpi"]

