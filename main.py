from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException
from dotenv import load_dotenv
load_dotenv()
import os

driver = webdriver.Edge()
url = 'https://lcs.dynamics.com/V2/EnvironmentDetailsV3New/1289467?EnvironmentId=d324bc3b-95c2-4f9f-8592-ad672d8e2ad4&IsCloudEnvironment=true&IsDiagnosticsEnabledEnvironment=true'
driver.get(url)

USERNAME = os.getenv('USERNAME')
loginEmail = driver.find_element(By.ID,"i0116")
loginEmail.send_keys(USERNAME)

loginButton = driver.find_element(By.ID, "idSIButton9")
loginButton.click()

PASS = os.getenv('PASS')
loginButton2 = driver.find_element(By.NAME,"passwd")
loginButton2.send_keys(PASS)

loginButton3 = driver.find_element(By.ID,"idSIButton9")
loginButton3.click()

stopButton = driver.find_element(By.NAME,"StopDeployment")
stopButton.click()

stopButton = driver.find_element(By.NAME,"Yes")
stopButton.click()

timeout = 10

startButtonLocator = driver.find_element(By.NAME,"StartDeployment")

while True:
    try:
        # Try to find the element
        startButton = WebDriverWait(driver, timeout).until(
            EC.presence_of_element_located(startButtonLocator)
        )
        
        # If the element is found, break out of the loop
        break
    except:
        # If the element is not found, refresh the page and try again
        driver.refresh()