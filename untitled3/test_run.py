

from commen import method  # 从Python包里导入
from testdata import data
from selenium import webdriver # 从selenium工具包里导入webdriver库
driver = webdriver.Chrome()   # webdriver 与chrome建立会话  ==赋值变量
driver.implicitly_wait(10)  # 隐式等待 --设置10s

# 取数据--字典取值
url = data.data_t.get("url")
name = data.data_t["name"]
passwd = data.data_t["passwd"]
print(url,name,passwd)

