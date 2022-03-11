import requests
from lxml import etree
import re
import parsel


url='https://app.ali213.net/wiki/mrfz/mrfzgy/'
headers={
    'user-agent':'Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/99.0.4844.51 Mobile Safari/537.36 Edg/99.0.1150.36'
}

data=requests.get(url=url,headers=headers).text
selector=parsel.Selector(data)
divs=selector.xpath('//div[@class="list-container"]/a')
for div in divs:
    new_url=div.xpath('./@href').get()
    new_url='https://app.ali213.net'+new_url
    new_data=requests.get(url=new_url,headers=headers)

    new_data.encoding = new_data.apparent_encoding
    new_data=new_data.text

    new_selector=parsel.Selector(new_data)
    #print(new_data)
    pic=new_selector.xpath('//div[@class="main-container"]/div/div[2]/div/img/@src').get()
    pic_url='https:'+pic
    name=new_selector.xpath('//div[@class="main-container"]/div/div[1]/div/span//text()').extract()

    img_data = requests.get(url=pic_url, headers=headers).content
    name=name[0]
    print(name)

    with open('明日方舟\\'+name,mode='wb') as f:
            f.write(img_data)
    print(name+'打印成功！')
    #print(pic_url,name)


