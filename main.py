from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException

driver = webdriver.Chrome()

url = 'https://lcs.dynamics.com/V2/EnvironmentDetailsV3New/1289467?EnvironmentId=d324bc3b-95c2-4f9f-8592-ad672d8e2ad4&IsCloudEnvironment=true&IsDiagnosticsEnabledEnvironment=true'
driver.get(url)