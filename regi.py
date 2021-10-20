from selenium import webdriver
import time
driver = webdriver.Chrome('chromedriver.exe')
driver.get('https://www.breakingmars.com/login')
# f ='David'
# l = 'malan'
# e = 'davidmalan@gmail.com'
# p = '123456'
create_account = driver.find_element_by_xpath('//*[@id="__next"]/main/div/div/div/div[1]/div/div[2]/div/div[3]/div[2]/span')
create_account.click()
time.sleep(3)
def regi(f,l,e,p):


    first_name = driver.find_element_by_xpath('//*[@id="basic"]/div/div/div/div[1]/div[1]/div/div/div[1]/div/input')
    first_name.send_keys(f)
    last_name = driver.find_element_by_xpath('//*[@id="basic"]/div/div/div/div[1]/div[2]/div/div/div[1]/div/input')
    last_name.send_keys(l)
    email = driver.find_element_by_xpath('//*[@id="basic"]/div/div/div/div[2]/div/div/div[1]/div/input')
    email.send_keys(e)
    password =driver.find_element_by_xpath('//*[@id="basic"]/div/div/div/div[3]/div/div/div[1]/div/span/input')
    password.send_keys(p)
    checkbox = driver.find_element_by_xpath('//*[@id="basic"]/div/div/div/div[4]/div[1]/label/span/input')
    checkbox.click()
    start_button = driver.find_element_by_xpath('//*[@id="basic"]/div/div/div/div[5]/button')
    start_button.click()
    count = driver.find_element_by_xpath('//*[@id="__next"]/main/div/div/div/div[1]/div/div[2]/div/div[2]')
    if count:
        print('This Email Is already registered')
    temp = driver.find_element_by_xpath('//*[@id="basic"]/div/div/div/div[2]/div/div/div[2]/div')
    if temp:
        print('Enter Email Address')
    flag = driver.find_element_by_xpath('//*[@id="basic"]/div/div/div/div[1]/div[2]/div/div/div[2]/div')
    if flag:
        print('Last Name Is Required')
    firstnalert = driver.find_element_by_xpath('//*[@id="basic"]/div/div/div/div[1]/div[1]/div/div/div[2]/div')
    if firstnalert:
        print('First Name Is Required')
    passalert = driver.find_element_by_xpath('//*[@id="basic"]/div/div/div/div[3]/div/div/div[2]/div')
    if passalert:
        print('Password Required')
    time.sleep(2)
def drive():
    regi('David','malan','davidmalan@gmail.com','123456')
    dom = count = driver.find_element_by_xpath('//*[@id="__next"]/main/div/div/div/div[1]/div/div[2]/div/div[2]')
    if dom:
        regi('david','malan','zombie.com','1234')

drive()
