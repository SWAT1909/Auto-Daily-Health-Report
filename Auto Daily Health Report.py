import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
 
stuID = '' #填写学号
pw = '' #填写密码
 
url = 'https://ids.xmu.edu.cn/authserver/login?service=https://xmuxg.xmu.edu.cn/login/cas/xmu'
 
start = time.perf_counter()
 
def timeFlag():
    startTime = time.strftime("%Y-%m-%d 07:00:00", time.localtime())
    endTime = time.strftime("%Y-%m-%d 19:30:00", time.localtime())
 
    startTimeStamp = time.mktime(time.strptime(startTime, "%Y-%m-%d %H:%M:%S"))
    endTimeStamp = time.mktime(time.strptime(endTime, "%Y-%m-%d %H:%M:%S"))
 
    if startTimeStamp < time.time() < endTimeStamp:
        return True
    else:
        print("该时段不能打卡!")
        return False
 
def autoSignIn():
    driver = webdriver.Chrome()
    driver.get(url)
    driver.maximize_window()
    time.sleep(1)
 
    driver.find_element_by_xpath('//*[@id="casLoginForm"]/p[4]/button').click()
    time.sleep(1)
 
    driver.find_element_by_xpath('//*[@id="username"]').send_keys(stuID)
    driver.find_element_by_xpath('//*[@id="password"]').send_keys(pw)
    driver.find_element_by_xpath('//*[@id="password"]').send_keys(Keys.ENTER)
    time.sleep(1)
 
    driver.find_element_by_xpath('//*[@id="mainPage-page"]/div[1]/div[3]/div[2]/div[2]/div[3]/div/div[1]').click()
    time.sleep(1)
 
    window1 = driver.current_window_handle
    for handle in driver.window_handles:
        if handle != window1:
            driver.switch_to.window(handle)
            print(handle)
            break
 
    time.sleep(1)
 
    driver.find_element_by_xpath('//*[@id="mainM"]/div/div/div/div[1]/div[2]/div/div[3]/div[2]').click()
    time.sleep(3)
 
    span = driver.find_element_by_xpath('//*[@id="select_1582538939790"]/div')
    print(span.get_attribute('title'))
    span.click()
    driver.find_element_by_xpath('/html/body/div[8]/ul/div/div[3]/li/label/span[2]').click()
 
    driver.find_element_by_xpath('//*[@id="pdfDomContent"]/../span/span').click()
    time.sleep(2)
 
    driver.switch_to.alert.accept()
    driver.quit()
 
if __name__ == '__main__':
    if timeFlag():
        autoSignIn()
        log()
