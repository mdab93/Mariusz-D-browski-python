from selenium import webdriver
import time

przegladarka = webdriver.Chrome()
przegladarka.get('http://kmg.hcm.pl/testowanie/validate.html')

poleEmail = przegladarka.find_element_by_id('e-mail')
poleEmail.send_keys("test")

przyciskSprawdzEmail = przegladarka.find_element_by_id('emailButton')
przyciskSprawdzEmail.click()

naglowekEmail = przegladarka.find_element_by_id('emailResult')
print(naglowekEmail.text)
assert "poprawny" in naglowekEmail.text

time.sleep(5)

przegladarka.close()