from bs4 import BeautifulSoup
import requests
#反检测
headers = {"User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_7_0) AppleWebKit/535.11 (KHTML, like Gecko) Chrome/17.0.963.56 Safari/535.11"}
response = requests.get(
    url="https://www.autohome.com.cn/news/",headers=headers)
#转义
response.encoding = response.apparent_encoding
soup = BeautifulSoup(response.text,features="html.parser")

#定位
target = soup.find(id="auto-channel-lazyload-article")
li_list = target.find_all('li')

for i in li_list:
    a = i.find('a')
    if a:
        print('https:',a.attrs.get("href"),sep="")      #去空格
        txt = a.find("h3").text             #去标签
        print(txt)
        img_url = a.find('img').attrs.get("src")
        print('https:',img_url,sep="")
