import os
import signal
import subprocess
import datetime

# The os.setsid() is passed in the argument preexec_fn so
# it's run after the fork() and before  exec() to run the shell.

def exe():
	
	print("inside healthcheck")
	
	print("starting building confguration for health checks ")
	#os.system("powershell -Command \"(gc modules\send.txt) -replace 'vm0000', '%arg0%' | Out-File modules\send.txt\" && powershell -Command \"(gc modules\send.txt) -replace 'USERID', '%arg1%' | Out-File modules\send.txt && powershell -Command \"(gc %mod%\send.txt) -replace 'PASSID', '%arg2%' | Out-File %mod%\send.txt\"")
	os.system("powershell -Command \"(gc modules\health.sh) -replace 'USERID', '%arg1%' | Out-File modules\health.sh\" && powershell -Command \"(gc %mod%\health.sh) -replace 'PASSID', '%arg2%' | Out-File %mod%\health.sh\"")
	os.system("powershell -Command \"(gc %mod%\get.txt) -replace 'vm0000', '%arg0%' | Out-File %mod%\get.txt\"")
	os.system("powershell -Command \"(gc %mod%\get.txt) -replace 'folder', '%fold%' | Out-File %mod%\get.txt\" && 	powershell -Command \"(gc %mod%\get.txt) -replace 'USERID', '%arg1%' | Out-File %mod%\get.txt\" && 	powershell -Command \"(gc %mod%\get.txt) -replace 'PASSID', '%arg2%' | Out-File %mod%\get.txt\" && 	powershell -Command \"(gc %mod%\get.txt) -replace 'dir', '%cd%' | Out-File %mod%\get.txt\" && powershell -Command \"(gc %mod%\health.sh) -replace ' DEV', ' %envv%' | Out-File -Encoding utf8 %mod%\health.sh")
	
	#print("step 1")
	#os.system("%mod%\\tools\\winscp\\winscp.com /ini=nul /script=%mod%\\send.txt > NULL")
	print("step 1")
	os.system("%mod%\\tools\\putty.exe -ssh %arg1%@%arg0% -pw %arg2% -m \"./%mod%/health.sh\"")
	print("step 2")
	os.system("%mod%\\tools\\winscp\\winscp.com /ini=nul /script=%mod%\\get.txt")
	print("exiting heatlthcheck")

#exe("host","user","pass","env")