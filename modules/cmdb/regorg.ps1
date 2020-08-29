echo "starting reg.ps1"
#$a=(sls -Pattern "cmdb_ci_middleware.do.*" $pwd\modules\cmdb\myhtml).Matches | select -exp value| %{ $_.Split(' ')[0]; }|%{ $_.Split('?')[1]; }| %{ $_.Split('&')[0]};
####working
#$a=((((sls "u_cmdb_ci_middleware.do" $pwd\modules\cmdb\myhtml) -split "do" | sls "sys_id" | sls "vm0000")[0] -split "&amp")[0] -split "=")[1];
$a=((((sls "vm0000" $pwd\modules\cmdb\myhtml) -split " " | sls "sys_id" | sls "vm0000")[0] -split "&amp")[0] -split "=")[2]
$b=$a
#$c="https://ibmaabpr.service-now.com/u_cmdb_ci_middleware.do?changeme&sysparm_record_target=u_cmdb_ci_middleware&sysparm_record_row=1&sysparm_record_rows=2179&sysparm_record_list=name%3E%3Dvm0000-CELL%5EORDERBYname"
$c="https://ibmaabpr.service-now.com/nav_to.do?uri=%2Fu_cmdb_ci_middleware.do%3Fsys_id=changeme"
$d=$c -replace ("changeme","$b")
start "C:\Program Files (x86)\Google\Chrome\Application\chrome.exe" $d
timeout 40