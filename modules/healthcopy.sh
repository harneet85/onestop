cd /tmp/Middleware_Healthcheck/src/
mkdir /tmp/health
cd /tmp/health/
echo "Fetching HC files"
wget --no-check-certificate --user=USERID --password="PASSID" -q -r -l12 -np "https://cms-repo.nl.eu.abnamro.com:8443/svn/was/customscripts/Custom_TSCD_Healthcheck/"
echo "Completed fetching"
chmod -R 777 /tmp/health
mv "./cms-repo.nl.eu.abnamro.com:8443/svn/was/customscripts/Custom_TSCD_Healthcheck/" ./
cd Custom_TSCD_Healthcheck/src
sudo -u wasusr /tmp/health/Custom_TSCD_Healthcheck/src/hc.ksh WAS WAS85 DEV
sudo -u wasusr /tmp/health/Custom_TSCD_Healthcheck/src/hc.ksh IHS IHS85 DEV


#cd /tmp/Middleware_Healthcheck/src/
#chmod -R 777 /tmp/Middleware_Healthcheck
#sudo -u wasusr find /appl/was ! -group wasgrp -exec chown wasusr:wasgrp {} \;
#sudo -u wasusr find /appl/was ! -user wasusr -exec chown wasusr:wasgrp {} \;
#sudo -u wasusr /tmp/Middleware_Healthcheck/src/hc.ksh WAS WAS85 DEV
#sudo -u wasusr /tmp/Middleware_Healthcheck/src/hc.ksh IHS IHS85 DEV
echo " "
rm -rf /tmp/health
echo "Exiting script in 5 sec"
sleep 10
