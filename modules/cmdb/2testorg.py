import time
import os
from selenium import webdriver

print("get current directory")
ddir=os.getcwd()
print("ddir value "+ddir)
print("")
newp=ddir+"\modules\\tools\\python2\\chrome_driver\\chromedriver.exe"
print(newp)
print("")

#chrome_options = webdriver.ChromeOptions()
#chrome_options.add_argument("--incognito")


driver = webdriver.Chrome(newp)
#driver = webdriver.Chrome(chrome_options=chrome_options)

#driver.get('https://ibmaabpr.service-now.com/u_cmdb_ci_middleware_list.do?sysparm_query=%5EnameSTARTSWITHvm0000-CELL&sysparm_first_row=1&sysparm_view=&sysparm_choice_query_raw=&sysparm_list_header_search=true')
#driver2.get('https://ibmaabpr.service-now.com/textsearch.do?sysparm_search=vm00000176-cell')

driver.get('https://ibmaabpr.service-now.com/textsearch.do?sysparm_ck=87aa78a3db73b2c08e84f1c51d9619203b2019b1273a395f8bae10e1404c9b16fbf6bc94&sysparm_search=vm0000-cell')
#driver.URL('https://ibmaabpr.service-now.com/textsearch.do?sysparm_search=vm00000176-cell')
time.sleep(1)

html = driver.page_source
f = open(ddir+"\\modules\\cmdb\\myhtml", "wt")
f.write(html)
f.close()

#driver.quit()