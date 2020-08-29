import os
import signal
import subprocess
import datetime

# The os.setsid() is passed in the argument preexec_fn so
# it's run after the fork() and before  exec() to run the shell.

def exe(host,user,passs,env):
	
#os.killpg(pro.pid, signal.SIGTERM) 
	os.environ['arg1']=user
	os.environ['arg2']=passs
	os.environ['arg0']=host
	dd=datetime.datetime.now().strftime("%d-%m-%Y")
	os.environ['mm']=dd
	os.environ['fold']="snd\\"+host+"_"+dd
	os.environ['fold2']="snd\\\\"+host+"_"+dd
	os.environ['mod']="modules"
	#set mod=modules
	os.environ['cd']=str(os.getcwd())
	os.environ['envv']=str(env)
	

	
	os.system("echo argument for user is : %arg1%  ")
	os.system("echo date is : %mm%")
	os.system("echo fold is : %fold%")
#	os.system("echo fold2 is : %fold2%")
	os.system("md %fold% && echo Generating work files : && copy snd\hcresult.xsl %fold%")
	os.system("copy modules\sendcopy.txt modules\send.txt && copy modules\sendcopy2.txt modules\send2.txt && copy modules\getcopy.txt modules\get.txt  && copy modules\getcopy2.txt modules\get2.txt && copy modules\healthcopy.sh modules\health.sh")


	os.system("powershell -Command \"(gc %mod%\WAS.bat) -replace 'vm0000', '%arg0%' | Out-File -Encoding oem %mod%\\WAS.bat\"")
	os.system("powershell -Command \"(gc %mod%\\cmdb\\regorg.ps1) -replace 'vm0000', '%arg0%' | Out-File %mod%\\cmdb\\reg.ps1\"")
	os.system("powershell -Command \"(gc %mod%\\was\\3testorg.py) -replace 'vm0000', '%arg0%' | Out-File -Encoding utf8 %mod%\\was\\3test.py\"")
	os.system("powershell -Command \"(gc %mod%\\was\\3test.py) -replace 'folder', '%fold2%' | Out-File -Encoding utf8 %mod%\\was\\3test.py\"")
	os.system("powershell -Command \"(gc %mod%\\cmdb\\2testorg.py) -replace 'vm0000', '%arg0%' | Out-File -Encoding utf8 %mod%\\cmdb\\2test.py\"")
	os.system("powershell -Command \"(gc %mod%\\was\\3test.py) -replace 'USERID', '%arg1%' | Out-File -Encoding utf8 %mod%\\was\\3test.py\"")
	os.system("powershell -Command \"(gc %mod%\\was\\3test.py) -replace 'PASSID', '%arg2%' | Out-File -Encoding utf8 %mod%\\was\\3test.py\"")
	print("pre confguration done")
	#transferring files
	
#	os.system("%mod%\\tools\\winscp\\winscp.com /ini=nul /script=%mod%\\send.txt > NULL")
#	os.system("%mod%\\tools\\putty.exe -ssh %arg1%@%arg0% -pw %arg2% -m \"./%mod%/health.sh\"")
#	os.system("%mod%\\tools\\putty.exe -ssh %arg1%@%arg0% -pw %arg2% -m \"./%mod%/script.sh\"")
#	os.system("%mod%\\tools\\winscp\\winscp.com /ini=nul /script=%mod%\\get.txt")
#	os.system("%mod%\\tools\\python2\\python.exe %mod%\\pdfconvert.py %fold%\\postinstall")
#	os.system("%mod%\\tools\\python2\\python.exe %mod%\\pdfconvert.py  %fold%\\version")
#	os.system("del %fold%\\version")
#	os.system("del %fold%\\postinstall")
	
	
#exe("host","user","pass","env")