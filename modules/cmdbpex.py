import os

def exe():
	print("inside cmdb check")
	print("step 1")
	
	os.system("set EXE=chrome.exe")
	os.system("FOR /F %%x IN ('tasklist /NH /FI \"IMAGENAME eq %EXE%\"') DO IF %%x == %EXE% goto FOUND")
	os.system("%mod%\\tools\\python2\\python.exe %mod%\\cmdb\\2test.py")
	#print("step 1")
	#os.system("powershell -Command \"(gc %mod%\\cmdb\\regorg.ps1) -replace 'vm0000', '%arg0%' | Out-File %mod%\\cmdb\\reg.ps1\"")
	#os.system("start powershell -Command %mod%\\cmdb\\reg.ps1")
	#os.system("TIMEOUT 10 >NULL")
	#print("step 2")
	#os.system("call %mod%\\tools\\screenCapture.exe %fold%\\cmdb.jpg \"VM0000\"")
	print("exiting was check")

