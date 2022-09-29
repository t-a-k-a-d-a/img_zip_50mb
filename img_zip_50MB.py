#!/usr/bin/env python
# coding: UTF-8
# =======================================
# 50MBごとにzip圧縮する
# 使い方：まとめたいファイルがあるフォルダにこのファイルを置いて実行
# =======================================
import re
import glob
import os.path
import zipfile

def makeZip():
	allFiles = glob.glob("*")
	toZip = []
	size = 0
	i = 1
	for e in allFiles:
		if e[-2:] == "py":
			continue
		toZip.append(e)
		size += os.path.getsize(e)
		if size > 49000000:
			print(toZip)
			zip = zipfile.ZipFile('img'+str(i)+'.zip', 'w', zipfile.ZIP_DEFLATED)
			for k in toZip:
				zip.write(k)
			toZip = []
			zip.close()
			size = 0
			i += 1

		#最後の処理
		if e == allFiles[-1]:
			print(toZip)
			zip = zipfile.ZipFile('img'+str(i)+'.zip', 'w', zipfile.ZIP_DEFLATED)
			for k in toZip:
				zip.write(k)
			zip.close()


if __name__ == "__main__":
	makeZip()
