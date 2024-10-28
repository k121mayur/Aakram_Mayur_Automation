import pygsheets
from datetime import datetime, timedelta
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
import time
from cred import username, password

login_link = "https://rcms.mahafood.gov.in/OfficeLogin.aspx"

driver = webdriver.Chrome()
driver.get(login_link)

time.sleep(3)


# /html/body/form/div[3]/div[2]/div[2]/div/div/div[3]/div/div[2]/div[2]/div/div/div[2]/input


driver.find_element(By.NAME, "ctl00$ContentPlaceHolder1$txtUserName").send_keys(username)

driver.find_element(By.NAME, "ctl00$ContentPlaceHolder1$txtPassword").send_keys(password)

driver.find_element(By.XPATH, "/html/body/form/div[3]/div[2]/div[2]/div/div/div[3]/div/div[2]/div[2]/div/div/div[2]/input").click()

captcha = input("Enter captcha: ")

driver.find_element(By.NAME, "ctl00$ContentPlaceHolder1$txtCaptcha").send_keys(captcha)

time.sleep(3)

driver.find_element(By.NAME, "ctl00$ContentPlaceHolder1$btnUserSignIn").click()

time.sleep(3)

TOTP = input("Enter TOTP: ")

driver.find_element(By.NAME, "ctl00$ContentPlaceHolder1$Txtusernameuseotp").send_keys(TOTP)

time.sleep(10)

#ctl00$ContentPlaceHolder1$btnUserUseOTP
driver.find_element(By.NAME, "ctl00$ContentPlaceHolder1$btnUserUseOTP").click()

time.sleep(5)

driver.find_element(By.XPATH, "/html/body/div[1]/form/div[3]/div/div/div/div[3]/div/div[2]/div/a").click()

time.sleep(3)

driver.find_element(By.XPATH, "/html/body/form/div[3]/div/div[1]/div/div[3]/div/div[1]/ul/li[1]/a").click()

time.sleep(3)
# eKYC Link

driver.find_element(By.XPATH, "//html/body/form/div[3]/div/div[1]/div/div[3]/div/div[1]/ul/li[1]/ul/li[11]/a").click()

time.sleep(3)
# Inside eKYC - 2nd eKYC
# Link https://rcms.mahafood.gov.in/frmekycdataverification.aspx
driver.find_element(By.XPATH, "/html/body/form/div[3]/div/div[1]/div/div[3]/div/div[1]/ul/li[1]/ul/li[11]/ul/li/a").click()

time.sleep(3)
# Reached to the Dashboard 

time.sleep(100000)