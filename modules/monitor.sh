#!/bin/bash
cd /usr/local/bin
echo Date is `date`
echo Hostname is `hostname`
echo " "
echo "Checking monitoring status"
echo " "
echo `pwd`
echo "sudo -u wasusr sudo ./WAS_monitor_status.sh"
sudo -u wasusr sudo ./WAS_monitor_status.sh;count=`sudo -u wasusr sudo ./WAS_monitor_status.sh | grep -i NOT| grep -v grep|wc -l`
if [[ $count == 1 ]]; then echo Starting Monitor; sudo -u wasusr sudo ./WAS_monitor_ON.sh; sudo -u wasusr sudo ./WAS_monitor_status.sh ; else echo "Monitor is UP and running"; fi

sleep 5
