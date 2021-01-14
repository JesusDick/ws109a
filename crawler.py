"請求網頁"
import requests

#re代表引入正則表達式
import re

import os

headers = {
    'user-agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.141 Safari/537.36'
}

response = requests.get('https://www.wmgirl.com/3447.html', headers = headers)

print(response.request.headers)
html = response.text

#解析網頁
dir_name = re.findall('<h1>(.*?)</h1>', html)[-1]
if not os.path.exists(dir_name):
    os.mkdir(dir_name)

urls = re.findall('<img  src="(.*?)"  title=".*?" alt=".*?"  >', html)
print(urls)

#保存圖片

for url in urls:
    TimeoutError(1)
    #圖片名稱
    flie_name = url.split('/')[-1]
    response = requests.get(url, headers = headers)
    with open(dir_name + '/' + flie_name, 'wb') as f:
        f.write(response.content)