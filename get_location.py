from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.action_chains import ActionChains
import time
from bs4 import BeautifulSoup

def get_location():    
    href = 'https://cloud.h2os.com/'

    #options = Options()
    #options.add_argument('--headless')
    #driver= webdriver.Chrome(chrome_options=options)
    driver=webdriver.Chrome()
    driver.get(href)
    driver.maximize_window()
    time.sleep(3)

    username='13786146742'
    password='wpy162104'

    usr = driver.find_element_by_id('username')
    usr.click()
    usr.clear()
    usr.send_keys(username)

    pwd = driver.find_element_by_id('password')
    pwd.click()
    pwd.clear()
    pwd.send_keys(password)

    button = driver.find_element_by_id('nc_1_n1z')
    ActionChains(driver).drag_and_drop_by_offset(button,334,0).perform()
    time.sleep(1)

    driver.find_element_by_id('login_btn').click()
    time.sleep(1)
    driver.find_element_by_class_name('internalTest').click()
    time.sleep(3)
    soup = BeautifulSoup(driver.execute_script("return document.documentElement.outerHTML"))
    tmp = soup.find_all('div',attrs={'class':'op-infoWindow'})
    location = tmp[0].__str__()
    location = location.split('<br/>')[1].split('</span>')[0]
    driver.quit()
    if location:
        return location
    else:
        raise KeyError('Access Failure')