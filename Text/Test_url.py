"""
用于测试网页是否异步
"""

import requests             # 访问网页
from lxml import etree      # 读取网页数据
url='https://lpl.qq.com/esnew/data/rank.shtml?iGameId=167&sGameType=1,5'
r=requests.get(url).content.decode('gbk')
html=etree.HTML(r)
print(r)
