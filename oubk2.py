from selenium.webdriver import Chrome,PhantomJS
import urllib.request
import urllib.parse
import http.cookiejar
import time
class readpage():
    def __init__(self,):

        path1 = r'D:\PythonStudy\Spider\chromedriver.exe'
        self.browser = Chrome(path1)

        # path2 = r'D:\PythonStudy\Spider\phantomjs.exe'
        # self.browser = PhantomJS(path2)

        self.url2 = 'https://oubk.com/super-sudoku/very-insane'
        self.login_obk()
    def login_obk(self):
        url = 'https://oubk.com/login'
        self.browser.get(url)
        name_imput = self.browser.find_element_by_id('login_name')
        password_imput = self.browser.find_element_by_id('password')
        chk = self.browser.find_element_by_id('remember')
        name_imput.send_keys('1782154228@qq.com')
        password_imput.send_keys('yb1122yb')
        chk.click()
        self.browser.execute_script('jAccount.Logon()')
        # self.browser.execute_script('window.open()')
        # self.browser.switch_to_window(self.browser.window_handles[-1])
    def read(self,):
        self.browser.get(self.url2)
        self.imput = []
        martix = []
        for s in range(1,10):
            imput_row = []
            martix_row = []
            for k in range(1, 10):
                key = self.browser.find_element_by_id('k'+str(k)+'s'+str(s))
                value = key.get_attribute('value')
                martix_row.append(value if value else '123456789')
                imput_row.append(key)
            self.imput.append(imput_row)
            martix.append(martix_row)
        return martix
    def write(self,martix):
        for s in range(9):
            for k in range(9):
                self.imput[s][k].send_keys(martix[s][k])

        self.browser.execute_script('Save()')

        # self.browser.save_screenshot( str(time.time()) + '.png')

        time.sleep(2)
        msg = self.browser.find_element_by_xpath("//div[@class='jqimessage ']/div")
        print(msg.text)
        sure = self.browser.find_element_by_id('jqi_state0_button确定')
        sure.click()

if __name__ == "__main__":
    url = 'https://oubk.com/super-sudoku/super-insane'
    read = readpage()
    print(read.read())


