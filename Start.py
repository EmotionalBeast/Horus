#!/usr/local/bin/python3

import xlwt, xlutils, os
from picture import Picture
from video import video

PIC_FORMAT = ("png", "jpg", "jpeg")
VID_FORMAT = ("mp4","mov")

def write_to_excel(*info):
	pass


if __name__ == "__main__":
	path = os.path.dirname(__file__)
	workspace_path = path + "/workspace"
	for root, dirs, files in os.walk(workspace_path):
		for dir in dirs:
			tmp = root + "/" + dir
			dir_path_list.append(tmp)

	for i in range(len(dir_path_list)):
		for root, dirs, files in os.walk(dir_path_list[i]):
			for file in files:
				_, tmp_suffix = file.split(".")
				if tmp_suffix in PIC_FORMAT:
					tmp_file = root + "/" + file
					pic = Picture(tmp_file)

				elif tmp_suffix in VID_FORMAT:
					tmp_file = root + "/" + file
					vid = Video(tmp_file)







