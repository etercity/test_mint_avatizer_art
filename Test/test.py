from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
import time
import datetime

chrome_options = Options()
# chrome_options.add_argument('--start-maximized')
chrome_options.add_argument('--headless')
# Disable log from webdriver
chrome_options.add_argument('--log-level=3')
url = 'https://mint.avatizer.art'


def inp_ut_qty(users):
    while True:
        try:
            text = '{}'.format(users)
            a = int(input(text))
            return a
        except ValueError:
            print("Please reinsert")


def inp_ut_password(password):
    if True:
        text = '{}'.format(password)
        b = str(input(text))
        return b


def get_url_page():
    browser = webdriver.Chrome(options=chrome_options)
    browser.set_window_size(1366, 1080)
    browser.get("https://mint.avatizer.art")
    time.sleep(1)
    return browser


def browser_quit():
    browser.quit()
    print("Quit browser\n")
    # browser.close()
    # print('Close browser')


users = inp_ut_qty('Enter the number of users: ')
password = inp_ut_password('Input password for Login (if exist): ')
now = datetime.datetime.now()
date_time = (now.strftime("%Y-%m-%d  %H:%M:%S"))
print(f"Test begin:  {date_time}")

i = 1
while i <= users:
    print("**************************\n")
    print(f"User:  {i}")
    print('Open browser')
    browser = get_url_page()
    print('Get URl')
    if password:
        inp_password = browser.find_element(By.NAME, "_vercel_password")
        inp_password.send_keys(password)
        print("input password")
        click_button_login_profile = browser.find_element_by_xpath('//*[@class="submit"]')
        click_button_login_profile.click()
        print("click button Login")
    time.sleep(1)
    click_button_connect_my_wallet = browser.find_element_by_xpath('//*[@class="wallet-form--btn btn btn-metamask metamask-connect"]')
    click_button_connect_my_wallet.click()
    print("click button Connect My Wallet")
    time.sleep(3)
    close_overlay = browser.find_element_by_xpath('//*[@class="walletconnect-modal__close__wrapper"]')
    close_overlay.click()
    print("close overlay")
    click_manage_my_avatizers = browser.find_element_by_xpath('//*[@class="main-menu-nav"]/ul[2]/li[6]/a')
    click_manage_my_avatizers.click()
    print("click Manage My Avatizers")
    click_button_connect_my_wallet = browser.find_element_by_xpath('//*[@class="wallet-form--btn btn btn-metamask metamask-connect"]')
    click_button_connect_my_wallet.click()
    print("click button Connect My Wallet")
    browser_quit()
    i += 1
now = datetime.datetime.now()
date_time = (now.strftime("%Y-%m-%d  %H:%M:%S"))
print(f"Test ended:  {date_time}\n")
input('Press ENTER to exit')
