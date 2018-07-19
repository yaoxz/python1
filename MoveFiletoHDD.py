# -*- coding:utf-8 -*-
#Author=''
import os,os.path
import shutil
import datetime
import sys

 
def movefiles(deftime,srcpath,HDD):
	for i in os.listdir(srcpath):
		filename = os.path.join(srcpath,i)
		Filetime = datetime.datetime.fromtimestamp(os.path.getmtime(filename))
		Systime = datetime.datetime.now()
		timeb = Systime - Filetime
		#print "==11"
		if  timeb.days > deftime and os.path.splitext(i)[1] == '.bz2':
			try:
				desdir = i.split('-')[1].split('.')[0][0:6]
				#print desdir
				despath = os.path.join(HDD,desdir)
				#print despath
				if not os.path.exists(despath):
					os.mkdir(despath)
				if not os.path.exists(os.path.join(despath,i)):
					shutil.move(filename,despath)
					print "%s move success." % filename
				else:
					# desfilesize = os.path.getsize(os.path.join(despath,i))
					# srcfilesize = os.path.getsize(filename)
					# if desfilesize <= srcfilesize :
						# os.remove(os.path.join(despath,i))
					shutil.move(filename,despath)
					print "%s move success." % filename
					# else:
						# print "repeat files!!Please check dirs..."

			except Exception as error:
				print error
				print "%s move faild." % filename
				continue

if __name__ == "__main__" :
	try:
		#SourcePath:H8BAK DIR
		SourcePath="D:\\H8BAK\\YYYYMMDD"
		#Destinatiion path (mobile HDD(mobile hard disk drive)):H
		HDD="E:\\"
		#剪切10天前文件
		movefiles(10,SourcePath,HDD)
	except Exception as e:
		print e
		sys.exit(-1)