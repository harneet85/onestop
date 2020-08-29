set EXE=chrome.exe
FOR /F %%x IN ('tasklist /NH /FI "IMAGENAME eq %EXE%"') DO IF %%x == %EXE% echo "CHROME IS RUNNING , exit chrome and rerun program" &&  TIMEOUT 20 && EXIT