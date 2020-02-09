from selenium import webdriver
import time

chrome = webdriver.Chrome()
chrome.get('http://www.wp.pl')
time.sleep(5)

chrome.get('http://kmg.hcm.pl/testowanie/validate.html')

emailText = chrome.find_element_by_id('e-mail')
telefonText = chrome.find_element_by_id('telefon')
peselText = chrome.find_element_by_id('pesel')

emailText.send_keys("test@test.pl")
telefonText.send_keys("535535535")
peselText.send_keys("90011293777")

buttonEmail = chrome.find_element_by_id('emailButton')
buttonTelefon = chrome.find_element_by_id('telefonButton')
buttonPesel = chrome.find_element_by_id('peselButton')

buttonEmail.click()
buttonPesel.click()
buttonTelefon.click()

wynikEmail = chrome.find_element_by_id('emailResult')
wynikPesel = chrome.find_element_by_id('peselResult')
wynikTelefon = chrome.find_element_by_id('telResult')

assert "poprawny" in wynikEmail.text
assert "poprawny" in wynikPesel.text
assert "poprawny" in wynikTelefon.text

time.sleep(5)

chrome.close()

