import unittest
from time import sleep
from  selenium import webdriver
from HTMLTestRunner import HTMLTestRunner
class YouJiuyeTest(unittest.TestCase):
    def setUp(self):
        self.chrome=webdriver.Chrome()
        self.chrome.get("http://xue.ujiuye.com/foreuser/login/")

    def login(self, username, password):
        username_d1 = self.chrome.find_element_by_id("username_d1")
        password_d1 = self.chrome.find_element_by_id("password_d1")
        button = self.chrome.find_elements_by_class_name("loginbutton1")
        username_d1.send_keys(username)
        password_d1.send_keys(password)
        button[0].click()
        text = self.chrome.find_elements_by_id("J_usernameTip").text
        return text
    def test_login_password(self):

        text=self.login("15773938140","123")
        self.assertEqual("密码应该为6-20位之间！",text,"密码太短提示内容有误")
    def test_loin_username(self):
        text = self.login("15773938140", "8765423423")
        self.assertEqual("账号不存在！", text, "提示内容有误")
    def tearDown(self):
        sleep(5)
        self.chrome.close()

if __name__=="__main__":
    suite=unittest.TestSuite()
    suite.addTest(YouJiuyeTest("test_login_password"))
    suite.addTest(YouJiuyeTest("test_login_username"))
    with open("report.html","wb") as f:
        runner=HTMLTestRunner(
            stream=f,
            title="教学测试",
            description="就是一个教学测试"
        )
        runner.run(suite)

