from sys import *
import os

def dw(path,old,new):
	flag=os.path.isabs(path)
	if flag==False:
		path=os.path.abspath(path)
	exists=os.path.isdir(path)
	if exists:
		for foldername,subfolder,filename in os.walk(path):
			for fn in filename:
				if(fn.endswith(old)):
					os.rename(os.path.join(foldername,fn),os.path.join(foldername,fn[:-4]+new))
	else:
		print("invalid path")
	
def main():
	if(len(argv)!=4):
		print("Invalid number of arguments")
		exit()

	if(argv[1]=="-h")or(argv[1]=="-H"):
		print("used to change extension of file")
		exit()

	try:
		dw(argv[1],argv[2],argv[3])

	except ValueError:
		print("Error invalid datatype")

	except Exception:
		print("Error invalid input")

if __name__=="__main__":
	main()