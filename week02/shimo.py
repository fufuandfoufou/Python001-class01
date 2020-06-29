# _*_ coding : UTF-8 _*_
# 开发团队    : 当场发财科技
# 开发人员    : shenglan
# 开发时间    : 2020-06-29   13:10
# 文件名称    : shimo  PY
# 开发工具    : PyCharm
import requests
from selenium import webdriver
browser = webdriver.Chrome()
browser.get('https://shimo.im/welcome')
browser.find_element_by_xpath('//button[@class="login-button btn_hover_style_8"]').click()
browser.find_element_by_xpath('//input[@type="text"]').send_keys('695134625@qq.com')
browser.find_element_by_xpath('//input[@type="password"]').send_keys('123456789')
browser.find_element_by_xpath('//button[@class="sm-button submit sc-1n784rm-0 bcuuIb"]').click()
cookies = browser.get_cookies()
print(cookies)





