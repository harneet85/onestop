#!/usr/bin/env python
import os

def exe():
    
	print("starting monitor check")
	os.system("start %mod%\\tools\\putty.exe -ssh %arg1%@%arg0% -pw %arg2% -m ./%mod%/monitor.sh")
	os.system("TIMEOUT 3 > NULL")
	os.system("start \"SCREEN CAPTURE 2\" cmd /c \"call %mod%\\tools\\screenCapture.exe %fold%\\monitor.jpg \"VM\" & TIMEOUT 4 & exit \"")
	print("Exiting monitor check")