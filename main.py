from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver import ActionChains
import pyautogui
import time
import os
from PIL import ImageGrab

from selenium.webdriver.common.by import By

if __name__ == '__main__':
    options = webdriver.ChromeOptions()
    service = Service(executable_path='/home/buiquanganh85/Programs/chromedriver_linux64/chromedriver')

    options.binary_location="/usr/bin/google-chrome"

    prefs = {"download.default_directory": "/home/buiquanganh85/work/test_selenium/downloaded"
             }
    options.add_experimental_option("prefs", prefs)

    driver = webdriver.Chrome(service= service, options=options)
    actionchain = ActionChains(driver)
    driver.set_window_size(16000, 12000)
    driver.get("https://www.nettruyenus.com/truyen-tranh/truong-hoc-sieu-anh-hung-93980")
    elems = driver.find_elements(by= "xpath",value="//div[@class='col-xs-5 chapter']/a")
    chapters = [ elem.get_property('href') for elem in elems]
    chapters.reverse()
    os.mkdir('./downloaded/my_hero_academia')
    for chap_id in range(len(chapters)):
        chapter_number = chap_id + 1
        chapter_link = chapters[chap_id]
        driver.get(chapter_link)
        chap_image_elems = driver.find_elements(by='xpath', value="//div[@class='page-chapter']/img")
        os.mkdir('./downloaded/my_hero_academia/chap_{}'.format(chapter_number))
        for chap_image_id in range(len(chap_image_elems)):
            chap_image_elem = chap_image_elems[chap_image_id]
            chap_image_number = chap_image_id + 1
            actionchain.context_click(chap_image_elem).perform()
            pyautogui.typewrite(['down', 'down', 'down','enter'])
            im = ImageGrab.grabclipboard()
            im.save('./downloaded/my_hero_academia/chap_{}/page_{}.png'.format(chapter_number, chap_image_number), 'PNG')
            print('./downloaded/my_hero_academia/chap_{}/page_{}.png downloaded'.format(chapter_number, chap_image_number))


