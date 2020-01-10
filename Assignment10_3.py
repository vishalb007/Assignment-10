from sys import *
import os
import shutil

def dw(path,newpath):
	flag=os.path.isabs(path)
	if flag==False:
		path=os.path.abspath(path)

	exists=os.path.isdir(path)
	new=os.path.join(path,newpath)
	if not os.path.exists(new):
		os.mkdir(new)
	if exists:
		for foldername,subfolder,filename in os.walk(path):
			for fn in filename:
				shutil.copy(fn,new)
	else:
		print("invalid path")
	
def main():
	if(len(argv)!=3):
		print("Invalid number of arguments")
		exit()

	if(argv[1]=="-h")or(argv[1]=="-H"):
		print("used to copy file from one folder to other")
		exit()

	try:
		dw(argv[1],argv[2])

	except ValueError:
		print("Error invalid datatype")

	except Exception:
		print("Error invalid input")

if __name__=="__main__":
	main()