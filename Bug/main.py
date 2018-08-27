# coding:utf-8

from urllib import request, parse
from bs4 import BeautifulSoup
import re


def getHtml(page):
    url = "http://www.dianping.com/shop/3320692/review_all/p" + page + "?queryType=isAll&queryVal=true"
    user_agent = ' Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_4) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/65.0.3325.181 Safari/537.36'
    cookie = '_lxsdk_cuid=162d3703daec8-04cdfb3e0ce85f-336b7b05-13c680-162d3703daec8; _lxsdk=162d3703daec8-04cdfb3e0ce85f-336b7b05-13c680-162d3703daec8; _hc.v=bf8ad568-dd69-5a4a-2476-6095e08e4f65.1523965771; _dp.ac.v=b8fa875f-5d47-4736-bf13-530959970de6; _thirdu.c=fe3838f4c8a1167b2c3362b06d2f234e; ua=%E5%BB%96%E5%B8%B8%E7%AB%8B; ctu=059bd92d32d73da217eaf0475cb56504fc190de2572ac03040bbb02db128455f; thirdtoken=FD14FB603ABC070EA47E6EFBDCDC9B0B; JSESSIONID=F8C4FD94ED82D627B09B221342D6CC5C; cityid=17; default_ab=shopreviewlist%3AA%3A1; ctu=9f884bad4b8c05f4466d87d26b4c193a345ac4ed5be64eab1b6e23b069429136e5c6cd0cbb262e0902a3282355357243; cy=17; cye=xian; ll=7fd06e815b796be3df069dec7836c3df; uamo=18629648223; dper=2bc8236ef9de5eff5a2a7c09a0eb60981513ba9b6693f72146288ef14f9034d4; _lxsdk_s=162d3accac4-e95-a33-081%7C%7C1130'
    headers = {
        'User-Agent': user_agent,
        'Cookie': cookie,
    }
    req = request.Request(url,headers = headers)
    response = request.urlopen(req)
    return (response.read().decode('utf-8'))


def getData(Html):
    soup = BeautifulSoup(Html,'lxml')
    ul = soup.find(attrs={'class':'reviews-items'})
    img = ul.find_all('img')
    reg = r'data-big="(.+?\.jpg)"'
    imgre = re.compile(reg)
    text = open("img_source.txt","a")
    for imgurl in img:
        imgstr = str(imgurl)
        urllist = imgre.findall(imgstr)
        if len(urllist)!= 0 :
            text.write(urllist[0] + '\n')
        #print(imgre.findall(imgstr))


for i in range(1419) :
    print("第"+str(i)+"页")
    getData(getHtml(str(i)))


