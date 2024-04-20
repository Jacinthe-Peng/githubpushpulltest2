from selenium import webdriver
from selenium.webdriver.common.by import By
import time

"""
一、分析需求：
1、使用谷歌浏览器，打开计支宝官网登录页面
2、找到输入框位置，输入账号
3、找到输入框位置，输入密码
4、点击登录按钮
5、点击小计
4、关闭浏览器
二、实际操作：
1、导入需要的库和包
2、执行用例
"""
driver = webdriver.Chrome()  #初始化，建立会话
driver.maximize_window() #浏览器最大化
driver.implicitly_wait(5)  #隐式等待
driver.get("https://www.jizhibao.com.cn/login")

title = driver.title
if title == "登录-计支宝":
    print("这个页面的标题是{}".format(title))
else:
    print("这条测试不通过")
# 2、找到输入框位置，输入账号
driver.find_elements(By.CLASS_NAME, "el-input__inner")[0].send_keys("13203389294")
# 3、找到输入框位置，输入密码
driver.find_elements(By.CLASS_NAME, "el-input__inner")[1].send_keys("jzb1234556")
# 4、点击登录按钮
driver.find_element(By.CLASS_NAME, 'el-button.el-button--primary').click()
time.sleep(6)
# 5、找到登录成功后页面必定会出现的标题：登录者姓名，获取这个标签里面的内容
username = driver.find_element(By.XPATH, '//span[@class="dropdown-link"]').text
# 6、对登录成功获取的内容进行判断
# if username=="彭观灵":
#     print("登录成功，用户名是{}".format(username))
# else:
#     print("登录失败")
assert username == "彭观灵"


time.sleep(10)
# 4、关闭浏览器
driver.close()
driver.quit()
