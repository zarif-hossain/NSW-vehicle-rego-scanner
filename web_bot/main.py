import configparser
import random
import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def main(regoNum):
    # setup the config parser (where HTML XPath identifiers are stored)
    config = configparser.ConfigParser()
    config.read('settings.ini')

    # not too sure what this line does
    service = Service(executable_path="chromedriver.exe")

    # #BEDUG: keeps web-browser open when program is executed
    # options = webdriver.ChromeOptions()
    # options.add_experimental_option("detach", True)

    # setup web driver
    driver = webdriver.Chrome(service=service) # add options=options to argument if you want to keep web browser open

    # Webpage I want to visit
    driver.get('https://check-registration.service.nsw.gov.au/frc?isLoginRequired=true')

    # Search the vehicle registration number in the website
    searchRego(driver, config, regoNum)
    # Web scrape
    checkRego(driver, config)

    # close the driver 
    driver.quit()     #BEDUG

# Insert desired rego number into the search field
def searchRego(driver, config: configparser, regoNum: str):
    # Wait for the page to load and find the target HTML XPath Identifier
    WebDriverWait(driver, 5).until(
        EC.presence_of_element_located((By.XPATH, config.get('searchRegoPath', 'plateNum')))
    )
    # Send the user input rego number
    driver.find_element(By.XPATH, config.get('searchRegoPath', 'plateNum')).send_keys(regoNum)
    haltStep()
    # click the T&Cs checkbox
    driver.find_element(By.XPATH, config.get('searchRegoPath', 'termsConditionsBox')).click()
    haltStep()
    # click to search rego number provided
    driver.find_element(By.XPATH, config.get('searchRegoPath', 'searchButton')).click()
    time.sleep(5)

def checkRego(driver, config):
    """
    TODO: Fix bot detection
    """
    WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.XPATH, config.get('rego', 'isRegistered')))
    )

    isRegisteredText =  driver.find_element(By.XPATH, config.get('rego', 'isRegistered'))
    print(isRegisteredText.text)
    time.sleep(10)

def haltStep():
    time.sleep(random.randint(1, 4))

if __name__ == "__main__":
    regoNum = input("Enter NSW vehicle's registration number: ")
    main(regoNum)