from selenium import webdriver
from selenium.webdriver.edge.service import Service
import requests
from time import sleep

s = Service('../edge/msedgedriver.exe')
edge = webdriver.Edge(service=s)
edge.get("https://lpl.qq.com/es/stats.shtml?bmid=8414")
# requests库，构造会话
session = requests.Session()
# 获取cookies
cookies = edge.get_cookies()
# 填充
for cookie in cookies:
    session.cookies.set(cookie['name'], cookie['value'])

# 给网页留一点加载的时间，不然之后find不了元素
sleep(10)
detail = edge.find_elements(by='xpath', value="//div[@class='detail']")
print(len(detail))
for i in range(0, len(detail)):
    title = detail[i].find_element(by='xpath', value="./div[@class='title']")
    rating_nums = detail[i].find_elements(by='xpath', value="./div/span[@class='rating_nums']")
    title_a = detail[i].find_element(by='xpath', value="./div[@class='title']/a").get_property('href')
    if (len(rating_nums) == 0):
        print(i, title.text, '暂无评分', title_a)
    else:
        print(i, title.text, rating_nums[0].text, title_a)
    if (i >= 5):  # 最多显示6个结果就行
        break
