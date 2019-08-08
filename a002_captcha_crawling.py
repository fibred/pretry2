# -*- coding: utf-8 -*-
### Get real captcha image


#Request URL: https://www.bankoftianjin.com/pweb/GenTokenImg.do
#Request Method: GET
#Status Code: 200 OK
#2000 imgs



import shutil
import requests
import time

SAVEPATH = 'D:\\Picture\\'
url = 'https://www.********.com/pweb/GenTokenImg.do?random='
for i in range(0, 2000):
    response = requests.get(url, stream=True)
    with open(SAVEPATH + str(i) + '.jpg', 'wb') as out_file:
        shutil.copyfileobj(response.raw, out_file)
    del response
    time.sleep(0)
print("save_completed")
