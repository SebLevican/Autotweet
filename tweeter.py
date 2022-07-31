from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep


EMAIL = 'sebadotpy@gmail.com'
KEY = 'INSERT KEY'


class tweet():
    def __init__(self):
        super().__init__()
        
        self.driver = webdriver.Chrome('chromedriver.exe')  
       

    def internettest(self):
        
        self.driver.get('https://www.speedtest.net/result/12869457647')
           
        self.download = self.driver.find_element(by=By.XPATH, value='//*[@id="container"]/div/div[3]/div/div/div/div[2]/div[3]/div[3]/div/div[2]/div[1]/div[2]/div/div[2]/div/div[2]/span').text
        self.upload = self.driver.find_element(by=By.XPATH, value='//*[@id="container"]/div/div[3]/div/div/div/div[2]/div[3]/div[3]/div/div[2]/div[1]/div[2]/div/div[3]/div/div[2]/span').text
        
        
    def login(self):
        
        self.driver.get('https://twitter.com/i/flow/login')
        sleep(3)

        user = self.driver.find_element(by=By.NAME, value = 'text')
        user.click()
        user.send_keys(EMAIL)
        
        nextp = self.driver.find_element(by=By.XPATH, value ='/html/body/div/div/div/div[1]/div/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div[1]/div/div/div[6]/div')
        nextp.click()
        
        sleep(3)
        pwd = self.driver.find_element(by=By.NAME, value='password')
        pwd.send_keys(KEY)
        
        lgnbtn = self.driver.find_element(by=By.XPATH, value ='/html/body/div/div/div/div[1]/div/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div[2]/div/div[1]/div')
        lgnbtn.click()
        sleep(3)
        
    def tweet(self):
        msg = self.driver.find_element(by=By.XPATH, value='//*[@id="react-root"]/div/div/div[2]/main/div/div/div/div/div/div[2]/div/div[2]/div[1]/div/div/div/div[2]/div[1]/div/div/div/div/div/div/div/div/div/label/div[1]/div/div/div/div/div[2]/div/div/div/div')
        msg.send_keys(f'hey internet i have {self.download} download and {self.upload} ')
 
bot = tweet()
bot.internettest()
bot.login()
bot.tweet()