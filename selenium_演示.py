import time
from selenium import webdriver
# 实例化一个游览器驱动
chrom=webdriver.Chrome()
# 访问页面
chrom.get("https://www.baidu.com/")
# 捕获元素
inputs=chrom.find_element_by_id("kw")
# 对元素进行操作
inputs.send_keys("老边饺子")
button=chrom.find_element_by_id("su")
button.click()
# 关闭游览器
time.sleep(5)
chrom.close()