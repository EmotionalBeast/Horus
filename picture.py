#coding: utf-8

import os
from PIL import Image


class Picture(object):
	def __init__(self,file_path):
		self.img = Image.open(file_path)

		#picture name
		self.file_name = file_path.split("/")[len(file_path.split("/"))-1]

		#picture resolution
		self.width_resolution, self.height_resolution = self.img.size
		self.resolution = str(self.width_resolution) + "x" + str(self.height_resolution)

		#picture size
		self.file_size = os.path.getsize(file_path) / (1024 * 1024) #MB

		#picture dpi
		if "dpi" in self.img.info.keys():
			self.dpi = self.img.info["dpi"][0]
		else:
			self.dpi = ""

	def get_info(self):
		file_size = str(round(self.file_size, 2))
		dpi = str(self.dpi)
		return [self.file_name, self.resolution, file_size, dpi]
		

