from os import link
from cred_sargule import username, password
from tkinter import Tk, Label, Entry, Button
from datetime import datetime
from selenium import webdriver
from selenium.webdriver.common.by import By

import time
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# from captcha import extract_captcha_text
def submit_captcha():
    global captcha_text
    captcha_text = captcha_entry.get()
    window.destroy()


login_link = "https://rcms.mahafood.gov.in/OfficeLogin.aspx"

driver = webdriver.Chrome()
driver.get(login_link)

time.sleep(3)


# /html/body/form/div[3]/div[2]/div[2]/div/div/div[3]/div/div[2]/div[2]/div/div/div[2]/input
driver.find_element(By.NAME, "ctl00$ContentPlaceHolder1$txtUserName").send_keys(
    username
)

driver.find_element(By.NAME, "ctl00$ContentPlaceHolder1$txtPassword").send_keys(
    password
)

driver.find_element(
    By.XPATH,
    "/html/body/form/div[3]/div[2]/div[2]/div/div/div[3]/div/div[2]/div[2]/div/div/div[2]/input",
).click()
time.sleep(3)

captcha_element = driver.find_element(By.ID, "ContentPlaceHolder1_CaptchaImage")
window = Tk()
window.geometry("400x150")
window.title("Captcha Entry")
window.configure(bg="#f0f8ff")

captcha_label = Label(window, text="Enter Captcha:", font=("Arial", 12), bg="#f0f8ff")
captcha_label.pack(pady=5)

captcha_entry = Entry(window, font=("Arial", 12))
captcha_entry.pack(pady=5)

# Button to submit captcha and close Tkinter window
submit_button = Button(
    window,
    text="Validate Captcha",
    font=("Arial", 10, "bold"),
    bg="#4CAF50",  # Green color for the button
    fg="white",
    command=submit_captcha
    )
submit_button.pack(pady=10)

window.mainloop()
time.sleep(1)
driver.find_element(By.NAME, "ctl00$ContentPlaceHolder1$txtCaptcha").send_keys(
    captcha_text
)

time.sleep(2)

driver.find_element(By.NAME, "ctl00$ContentPlaceHolder1$btnUserSignIn").click()

time.sleep(3)

TOTP = "985045"  # input("Enter TOTP: ")

driver.find_element(By.NAME, "ctl00$ContentPlaceHolder1$Txtusernameuseotp").send_keys(
    TOTP
)

time.sleep(5)

# ctl00$ContentPlaceHolder1$btnUserUseOTP
driver.find_element(By.NAME, "ctl00$ContentPlaceHolder1$btnUserUseOTP").click()

# time.sleep(20)

# driver.find_element(
#     By.XPATH, "/html/body/div[1]/form/div[3]/div/div/div/div[3]/div/div[2]/div/a"
# ).click()

element = WebDriverWait(driver, 20).until(
    EC.presence_of_element_located(
        (By.XPATH, "/html/body/div[1]/form/div[3]/div/div/div/div[3]/div/div[2]/div/a")
    )
)
element.click()

time.sleep(3)

driver.find_element(
    By.XPATH, "/html/body/form/div[3]/div/div[1]/div/div[3]/div/div[1]/ul/li[1]/a"
).click()

time.sleep(3)
# eKYC Link
driver.execute_script("window.scrollBy(0, 1000)")

time.sleep(1)

driver.find_element(
    By.XPATH,
    "//html/body/form/div[3]/div/div[1]/div/div[3]/div/div[1]/ul/li[1]/ul/li[11]/a",
).click()

time.sleep(3)

driver.execute_script("window.scrollBy(0, 1000)")

time.sleep(1)
# Inside eKYC - 2nd eKYC
# Link https://rcms.mahafood.gov.in/frmekycdataverification.aspx
driver.find_element(
    By.XPATH,
    "/html/body/form/div[3]/div/div[1]/div/div[3]/div/div[1]/ul/li[1]/ul/li[11]/ul/li/a",
).click()

time.sleep(40)

# Reached to the Dashboard

# /html/body/form/div[3]/div/div[3]/div/div/div[1]/table/tbody/tr[2]/td[21]
# /html/body/form/div[3]/div/div[3]/div/div/div[1]/table/tbody/tr[21]/td[21]
# Table >>
driver.find_element(
    By.XPATH,
    "/html/body/form/div[3]/div/div[3]/div/div/select"
).click()
time.sleep(2)

driver.find_element(
    By.XPATH,
    "/html/body/form/div[3]/div/div[3]/div/div/select/option[2]"
).click()
time.sleep(40)

handle = open("count.csv", "a+")

while True:
    # Click on the second option in the dropdown
    driver.find_element(
        By.XPATH,
        "/html/body/form/div[3]/div/div[3]/div/div/div[1]/table/tbody/tr[2]/td[21]/a[1]"
    ).click()
    time.sleep(5)  # Sleep for 5 seconds to allow the page to load

    # Wait for and accept the first alert
    alert = WebDriverWait(driver, 5).until(EC.alert_is_present())
    alert.accept()

    time.sleep(5)  # Sleep for 5 seconds

    # Click the checkbox for the disability type
    driver.find_element(
        By.NAME, "ctl00$ContentPlaceHolder1$Chkdisabilitytype$1"
    ).click()
    time.sleep(3)  # Sleep for 3 seconds
    #/html/body/form/div[3]/div/div[3]/div/div/div[4]/div/div/div/div[2]/div/div[1]/div/div/div/div/div/table/tbody/tr[2]/td/input
    #//*[@id="ContentPlaceHolder1_Chkdisabilitytype_1"]

    # Click the reject submit button
    driver.find_element(
        By.NAME, "ctl00$ContentPlaceHolder1$btnrejectsubmit"
    ).click()

    # Wait for and accept two alerts
    alert = WebDriverWait(driver, 5).until(EC.alert_is_present())
    alert.accept()

    alert = WebDriverWait(driver, 100).until(EC.alert_is_present())
    alert.accept()

    time.sleep(2)

    handle.write(
                    str(datetime.now().strftime("%Y-%m-%d %H:%M:%S"))
                    + " ,"
                    + "1"
                    + "\n"
                )
