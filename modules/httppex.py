#!/usr/bin/env python
import os

def exe():
	print("starting http check")
	os.system("start %mod%\\tools\\putty.exe -ssh %arg1%@%arg0% -pw %arg2% -m ./%mod%/http.sh")
	os.system("TIMEOUT 7 > NULL")
	os.system("start \"SCREEN CAPTURE 4\" cmd /c \"call %mod%\\tools\\screenCapture.exe %fold%\\http.jpg \"VM\" & TIMEOUT 4 & exit \"")
	print("ending http check")