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
Day=str(cur.day).zfill(2)
print Year,Month

SourcePath="D:\\2018"
DesPath="E:\\"+Year+Month
print DesPath
if not os.path.exists(DesPath):
	#print (DesPath,": not exists")
	os.mkdir(DesPath)
###匹配到指定日期的文件后复制

for i in os.listdir(SourcePath):
	if os.path.isfile(i) and os.path.splitext(i)[1] == '.zip' :
		#print i
		#print "star" 
		#pdb.set_trace()
		#匹配包含指定日期的文件名
		L=re.compile(r'[a-z]+'+Year+Month+'[0-9a-z]+\.[0-9a-z]+',re.I).match(i)
		if L:
			Real_DesPathFile=os.path.join(DesPath,L.group())
			print Real_DesPathFile
			#print os.path.abspath(L.group())
			if not os.path.exists(Real_DesPathFile):
				Real_SourcePathFile=os.path.join(SourcePath,L.group())
				#print Real_DesPathFile
				#print "==="
				shutil.move(Real_SourcePathFile,DesPath)
				print Real_SourcePathFile," copy to ",Real_DesPathFile
		
		