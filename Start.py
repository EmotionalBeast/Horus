##!/usr/local/bin/python3
# coding: utf-8

'''
写入格式属性控制：在Formatting.py中
font 
alignment 
borders
pattern 
protection
'''
import xlwt, os, time
from picture import Picture
from video import Video

PIC_FORMAT = ("png", "jpg", "jpeg")
VID_FORMAT = ("mp4","mov", "MOV")
PIC_SHEET_TITLE = ["图片名称", "分辨率", "大小(MB)", "DPI"]
VID_SHEET_TITLE = ["视频名称", "分辨率", "大小(MB)", "视频时长","码率(KBPS)", "帧率(FPS)"]

#控制输出格式
def setStyle():
	style = xlwt.XFStyle()
	#对齐方式
	alignment = xlwt.Alignment()
	alignment.horz = alignment.HORZ_CENTER
	alignment.vert = alignment.VERT_CENTER
	style.alignment = alignment
	return style

#写入文件
def write_to_excel(path, *info):
	workbook = xlwt.Workbook(encoding="utf-8")
	sheet = workbook.add_sheet("sheet1")
	for i in range(len(info)):
		for j in range(len(info[i])):
			sheet.write(i, j, info[i][j], setStyle())
	sheet.col(0).width = 256 * 50
	for i in range(len(info[0])):
		if i != 0:
			sheet.col(i).width = 256 * 20
	workbook.save(path)
	print("表格写入数据成功！")

def sort_by_creation_time(files):
	for i in range(len(files)-1):
		for j in range(len(files)-i-1):
			if os.path.getctime(files[j+1]) > os.path.getctime(files[j]):
				files[j], files[j+1] = files[j+1], files[j]
	return files

#得到文件中关键信息
def get_info_list(path):
	workspace_path = path + "/workspace"
	pic_info = []
	pic_info.append(PIC_SHEET_TITLE)
	vid_info = []
	vid_info.append((VID_SHEET_TITLE))
	target_files = []

	for root, dirs, files in os.walk(workspace_path):
		for file in files:
			tmp_file = root + "/" + file
			target_files.append(tmp_file)

	for file in sort_by_creation_time(target_files):
		_, file_suffix = file.split(".")
		if file_suffix in PIC_FORMAT:
			pic = Picture(file)
			pic_item = pic.get_info()
			pic_info.append(pic_item) #二维列表
		elif file_suffix in VID_FORMAT:
			vid = Video(file)
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













