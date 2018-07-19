# -*- coding: UTF-8 -*-
import os,os.path
import shutil
import datetime
import string
import re 
import pdb
cur=datetime.datetime.now()
#Year=str(cur.year)
Year=str(cur.year).zfill(4)
#Month=str(cur.month)
Month=str(cur.month).zfill(2)
#Day=cur.day
#Day=str(cur.day).zfill(2)
print Year,Month

#SourcePath:H8BAK DIR
SourcePath="F:\\H8BAK\\YYYYMMDD"
#Destinatiion path (mobile HDD(mobile hard disk drive)):H
HDD="H:\\"
DesPath=HDD+Year+Month
#print DesPath

if not os.path.exists(DesPath):
	os.mkdir(DesPath)
###匹配到指定日期的文件后复制
for i in os.listdir(SourcePath):
	#print os.path.splitext(i)[1]
	#print os.path.isfile(os.path.join(SourcePath,i))
	try:
		if  os.path.splitext(i)[1] == '.bz2' :
		#print 123
		#匹配包含指定日期的文件名
			L=re.compile(r'[a-z]+\-'+Year+Month+'[0-9a-z]+\.[0-9a-z]+\.[0-9a-z]+',re.I).match(i)
			if L:
				Real_DesPathFile=os.path.join(DesPath,L.group())
				if not os.path.exists(Real_DesPathFile):
					Real_SourcePathFile=os.path.join(SourcePath,L.group())
					shutil.move(Real_SourcePathFile,DesPath)
					#print Real_SourcePathFile," copy to ",Real_DesPathFile
				else:
					if not os.path.exists(os.path.join(HDD,"Duplicate-files")):
						os.mkdir(os.path.join(HDD,"Duplicate-files"))
					Real_SourcePathFile=os.path.join(SourcePath,L.group())
					shutil.move(Real_SourcePathFile,os.path.join(HDD,"Duplicate-files"))
	except Exception,e:
		print e
		print "ERROR,Please Check!...."
		continue