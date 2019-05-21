# -*- coding: utf-8 -*-
import os,sys 
def list_files(path):
	if os.path.isdir(path):
		print(path + ' : ')
		content = os.listdir(path)
		print(content)
		for fname in content:
			fname = os.path.join(path,fname)
			list_files(fname)
list_files("d:/06.python")
