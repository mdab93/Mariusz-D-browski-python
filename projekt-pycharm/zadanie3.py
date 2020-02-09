from selenium import webdriver
import time

chrome = webdriver.Chrome()
chrome.get('http://bartekkacz.ddns.net:65328/~bartosz/web/contact.php')

poleImie = chrome.find_element_by_xpath('/html/body/div/div[3]/form/div[1]/input')
poleImie.send_keys('Mariusz')

poleEmail = chrome.find_element_by_xpath('/html/body/div/div[3]/form/div[2]/input')
poleEmail.send_keys('test@test.pl')

# to nie zadziała poprawnie gdyż wpisze do pierwszej znalezionej classy o tej nazwie
poleNumer = chrome.find_element_by_class_name('form-control')
poleNumer.send_keys("35322")

# to zaś wpisze poprawnie
poleNumer = chrome.find_element_by_css_selector('#mobile')
poleNumer.send_keys("35322")

poleTemat = chrome.find_element_by_name('subject')
poleTemat.send_keys("Juhu")

poleWiadomosc = chrome.find_element_by_id('message')
poleWiadomosc.send_keys("Witam")

time.sleep(5)
chrome.close()
