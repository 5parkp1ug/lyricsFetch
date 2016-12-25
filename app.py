import os
import sys
import taglib

class getFileInfo:
	"""Main Class to Instantiate the File"""
	def __init__(self, name, path):
		self.file_name = name
		self.file_path = path

	def checkFile(self):
		
		if os.path.isfile(self.file_path) and self.file_name.split(".")[-1] == "mp3":
			print "File Exists!!!"
			return 1
		elif os.path.isfile(self.file_path):
			print "Please check the File Again as it seems to be a '"+self.file_name.split(".")[-1]+"' file"
			return 0
		else:
			print "File/Path Doesn't Exist!!!"
			return 0


	def dispInfo(self):
		print "File Name - " + self.file_name
		print "File Path - " + self.file_path
		print "==========================================="

		song = taglib.File(self.file_path)

		for key,value in song.tags.iteritems():
			print str(key) +" : "+str(value)


def main():

	if len(sys.argv) != 3:
		print "Enter File Details"

	else:
		name = sys.argv[1]
		path = sys.argv[2]

		obj = getFileInfo(name,path)
		if obj.checkFile():
			obj.dispInfo()


main()
raw_input()