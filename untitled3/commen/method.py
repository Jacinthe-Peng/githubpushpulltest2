import time

# 打开网页
from selenium.webdriver.common.by import By


def open_page(driver, url):
    driver.get(url)
    driver.maximize_window()


# 登录函数
def login_fun(driver, name, passwd):
    driver.find_elements(By.CLASS_NAME, "el-input__inner")[0].send_keys("name")
    driver.find_elements(By.CLASS_NAME, "el-input__inner")[1].send_keys("passwd")
    driver.find_element(By.CLASS_NAME, 'el-button.el-button--primary').click()
