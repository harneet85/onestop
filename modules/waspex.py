import os

def exe():
	print("inside was check")
	os.system("%cd%//%mod%//chrome.bat")
	#os.system("FOR /F %%x IN ('tasklist /NH /FI \"IMAGENAME eq %EXE%\"') DO IF %%x == %EXE% echo \"Chrome is running hence exiting\"&& echo \"Chrome is running hence exiting\" && TIMEOUT 10&& exit")
	print("step 1")
	os.system("%mod%\\tools\\python2\\python.exe %mod%\\was\\3test.py")
	print("exiting was check")
	os.system("TIMEOUT 5 >NULL")