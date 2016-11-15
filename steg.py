# !/usr/bin/python
# coding:utf-8
# 将2.png隐藏到1.png中,1.png需要比2.png大，图片格式不要求

from PIL import Image
import sys

def set_pixel(R1, R2):#修改R的最低位
	R1 >>= 1
	R1 <<= 1
	if R2 & 1 == 1:
		R1 += 1
	return R1

def hide(para1,para2):

	img1=Image.open(para1)
	img2=Image.open(para2)

	if img1.mode != "RGBA":
		img1 = img1.convert("RGBA")
	if img2.mode != "RGBA":
		img2 = img2.convert("RGBA")

	(width,height) = img2.size	#GET SIZE  只操作要隐写的图片的大小
	data1 = img1.getdata()	#获取PNG的数据
	data2 = img2.getdata()

	steg_img = img1  #作为最后保存的图片
	data_img = steg_img.getdata()


	for h in xrange(height):
		for w in xrange(width):
			(R1, G1, B1, A1) = data1.getpixel((w, h))	#处理每个像素
			(R2, G2, B2, A2) = data2.getpixel((w, h))
			R1=set_pixel(R1, R2)
			data_img.putpixel((w, h), (R1, G1, B1, A1))
	steg_img.save("save.png", "PNG")

	print "Finish!"


if __name__ == '__main__':
	if(len(sys.argv) == 1):
		print "usage example:"
		print " python steg.py first.png second.png\n"
		print "Notice:"
		print " 1. second.png is the image you want to hide"
		print " 2. first.png should be bigger than second.png"
	else:
		para = sys.argv
		hide(para[1],para[2])
