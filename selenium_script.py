import time
from selenium import webdriver
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.by import By
# import pandas as pd

ShelterPetFinderId = input("Enter your shelter id: ")
UserName = input("Enter your user name: ")
Password = input("Enter your password: ")

######################################################
# LOGIN ##############################################
browser = webdriver.Chrome()
browser.get('https://sms.petpoint.com/sms3/forms/signinout.aspx?ReturnUrl=%2fsms3%2f')

def send_login_key (element_id, value):
    page_element = browser.find_element_by_id('cphSearchArea_txt{}'.format(element_id))
    page_element.send_keys(value)

login_dict = {
    'ShelterPetFinderId': ShelterPetFinderId,
    'UserName': UserName,
    'Password': Password }

for identifier, value in login_dict.items():
    send_login_key(identifier, value)
    time.sleep(2)

browser.find_element_by_name('ctl00$cphSearchArea$btn_SignIn').click()
time.sleep(2)

######################################################
# NAVIGATE ###########################################
browser.get('https://sms.petpoint.com/sms3/forms/AnimalTab.aspx')

def select_dropdown (element_id, value):
    select = Select(browser.find_element_by_id(element_id))
    select.select_by_visible_text(value)

filter_dict = {
    'cphSearchArea_ctrlAnimal_ctrlAnimalSearch_ddlCriteria': 'Location',
    'cphSearchArea_ctrlAnimal_ctrlAnimalSearch_DDL_Site': 'Lynnwood',
    'cphSearchArea_ctrlAnimal_ctrlAnimalSearch_ddlLocation': 'Dog Kennels' }

for identifier, value in filter_dict.items():
    select_dropdown(identifier, value)
    time.sleep(2)

browser.find_element_by_name('ctl00$cphSearchArea$ctrlAnimal$ctrlAnimalSearch$btnFind').click()

######################################################
# RETRIEVE DATA ######################################
select_dropdown('cphSearchArea_ctrlAnimal_ctrlAnimalSearch_dgFoundItems_ddlPS',
                'All')

# columns =
i = 0
while True:
    try:
        print(browser.find_element_by_xpath("//table[@id='cphSearchArea_ctrlAnimal_ctrlAnimalSearch_dgFoundItems']/tbody/tr/td[{}]/a".format(i)).text)
        i+=1
    except:
        print("Done reading header")
        break

# browser.find_element_by_name('ctl00$cphSearchArea$ctrlAnimal$ctrlAnimalSearch$btnFind').click()

# browser.quit()
