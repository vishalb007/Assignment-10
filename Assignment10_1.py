from sys import *
import os

def dw(path):
	flag=os.path.isabs(path)
	if flag==False:
		path=os.path.abspath(path)

	exists=os.path.isdir(path)
	print(exists)
	if exists:
		for foldername,subfolder,filename in os.walk(path):
			print("Current folder is ",foldername)
			print("Files are :")
			for fn in filename:
				if(fn.endswith(argv[2])):
					f=open("Extension_Automation.log","a+")
					f.write(fn)
					f.write("\n")
					f.close()
					print(fn)
			print("")
	else:
		print("invalid path")
	
def main():
	if(len(argv)!=3):
		print("Invalid number of arguments")
		exit()

	if(argv[1]=="-h")or(argv[1]=="-H"):
		print("used to display all files of given extension")
		exit()

	try:
		dw(argv[1])

	except ValueError:
		print("Error invalid datatype")

	except Exception:
		print("Error invalid input")

if __name__=="__main__":
	main()