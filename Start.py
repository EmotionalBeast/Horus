#!/usr/local/bin/python3
# coding: utf-8

import xlwt, os, time
from picture import Picture
from video import Video

PIC_FORMAT = ("png", "jpg", "jpeg")
VID_FORMAT = ("mp4","mov")
PIC_SHEET_TITLE = ["图片名称", "分辨率", "大小(MB)", "DPI"]
VID_SHEET_TITLE = ["视频名称", "分辨率", "大小(MB)", "视频时长","码率(KBPS)", "帧率(FPS)"]

def write_to_excel(path, *info):
	# #设置字体
	# font = xlwt.Font()
	# font.name = "宋体"
	# font.color = "black"
	# font.height = "340"

	# #设置居中
	# alignment = xlwt.Alignment()
	# alignment.horz = xlwt.Alignment.HORZ_CENTER
	# alignment.vert = xlwt.Alignment.VERT_CENTER

	# #设置边框
	# borders = xlwt.Borders()
	# borders.left = xlwt.Borders.THIN
	# borders.right = xlwt.Borders.THIN
	# borders.top = xlwt.Borders.THIN
	# borders.bottom = xlwt.Borders.THIN

	# #设置背景颜色
	# pattern = xlwt.Pattern()
	# pattern.pattern = xlwt.Pattern.SOLID_PATTERN
	# pattern.pattern_fore_colour = 3

	# #定义style
	# style = xlwt.XFStyle()
	# style.font = font
	# style.borders = borders
	# style.alignment = alignment 

	workbook = xlwt.Workbook(encoding="utf-8")
	sheet = workbook.add_sheet("sheet1")
	for i in range(len(info)):
		for j in range(len(info[i])):
			sheet.write(i, j, info[i][j])
	workbook.save(path)
	print("表格写入数据成功！")

def get_info_list(path):
	workspace_path = path + "/workspace"
	pic_info = []
	pic_info.append(PIC_SHEET_TITLE)
	vid_info = []
	vid_info.append((VID_SHEET_TITLE))
	dir_path_list = []
	for root, dirs, files in os.walk(workspace_path):
		for dir in dirs:
			tmp = root + "/" + dir
			dir_path_list.append(tmp)

	for i in range(len(dir_path_list)):
		for root, dirs, files in os.walk(dir_path_list[i]):
			for file in files:
				tmp_file = root + "/" + file
				_, tmp_suffix = file.split(".")
				if tmp_suffix in PIC_FORMAT:
					pic = Picture(tmp_file)
					pic_item = pic.get_info()
					pic_info.append(pic_item)
				elif tmp_suffix in VID_FORMAT:
					vid = Video(tmp_file)
					vid_item = vid.get_info()
					vid_info.append(vid_item)
				else:
					continue
	return pic_info, vid_info

def print_info(*info):
	for i in range(len(info)):
		print(info[i])
	print()

if __name__ == "__main__":
	path = os.path.dirname(__file__)
	pic_info, vid_info = get_info_list(path)

	print_info(*pic_info)
	print_info(*vid_info)

	timeStr = time.strftime('%Y_%m_%d_%H_%M', time.localtime(time.time()))

	pic_xls_path = path + "/workspace/picture_info_" + timeStr + ".xls"
	vid_xls_path = path + "/workspace/video_info_" + timeStr + ".xls"
	if len(pic_info) != 0:
		write_to_excel(pic_xls_path, *pic_info)
	else:
		print("没有图片文件")
	if len(vid_info) != 0:
		write_to_excel(vid_xls_path, *vid_info)
	else:
		print("没有视频文件")













