from cred_sargule import username, password
from tkinter import Tk, Label, Entry, Button
from datetime import datetime
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

# Function to initialize and display the Tkinter window for captcha input
def create_captcha_window():
    global captcha_text, captcha_entry, window

    # Configure main window settings
    window = Tk()
    window.geometry("400x150")
    window.title("Captcha Entry")
    window.configure(bg="#f0f8ff")  # Light blue background for aesthetics

    # Set up and arrange Label, Entry, and Button
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

# Function to capture the captcha input and close Tkinter window
def submit_captcha():
    global captcha_text
    captcha_text = captcha_entry.get()
    window.destroy()  # Close the Tkinter window after submitting

# Function to initialize the Selenium WebDriver
def initialize_driver():
    driver = webdriver.Chrome()
    driver.get("https://rcms.mahafood.gov.in/OfficeLogin.aspx")
    time.sleep(3)
    return driver

# Function to perform login using provided credentials
def perform_login(driver):
    driver.find_element(By.NAME, "ctl00$ContentPlaceHolder1$txtUserName").send_keys(username)
    driver.find_element(By.NAME, "ctl00$ContentPlaceHolder1$txtPassword").send_keys(password)
    driver.find_element(
        By.XPATH, "/html/body/form/div[3]/div[2]/div[2]/div/div/div[3]/div/div[2]/div[2]/div/div/div[2]/input"
    ).click()
    time.sleep(3)

# Function to input captcha after obtaining it from Tkinter
def input_captcha(driver):
    driver.find_element(By.NAME, "ctl00$ContentPlaceHolder1$txtCaptcha").send_keys(captcha_text)
    time.sleep(2)

# Function to submit the login form
def submit_login(driver):
    driver.find_element(By.NAME, "ctl00$ContentPlaceHolder1$btnUserSignIn").click()
    time.sleep(3)

# Function to enter the TOTP (can later be modified to take dynamic input)
def enter_totp(driver, TOTP="545040"):
    time.sleep(5)
    driver.find_element(By.NAME, "ctl00$ContentPlaceHolder1$Txtusernameuseotp").send_keys(TOTP)
    driver.find_element(By.NAME, "ctl00$ContentPlaceHolder1$btnUserUseOTP").click()
    time.sleep(5)

# Function to navigate to the eKYC verification page
def navigate_to_ekyc(driver):
    
    WebDriverWait(driver, 20).until(
        EC.presence_of_element_located((By.XPATH, "/html/body/div[1]/form/div[3]/div/div/div/div[3]/div/div[2]/div/a"))
    ).click()
    time.sleep(2)
    driver.find_element(By.XPATH, "/html/body/form/div[3]/div/div[1]/div/div[3]/div/div[1]/ul/li[1]/a").click()
    driver.execute_script("window.scrollBy(0, 1000)")
    time.sleep(1)
    driver.find_element(By.XPATH, "//html/body/form/div[3]/div/div[1]/div/div[3]/div/div[1]/ul/li[1]/ul/li[11]/a").click()
    driver.execute_script("window.scrollBy(0, 1000)")
    time.sleep(1)
    driver.find_element(By.XPATH, "/html/body/form/div[3]/div/div[1]/div/div[3]/div/div[1]/ul/li[1]/ul/li[11]/ul/li/a").click()
    time.sleep(5)

# Main function to control the sequence of operations
def main():
    # Initialize Selenium WebDriver and login
    driver = initialize_driver()
    perform_login(driver)
    
    # Open Tkinter window for captcha input
    create_captcha_window()
    
    # After Tkinter closes, input captcha and submit
    input_captcha(driver)
    submit_login(driver)
    
    # Enter TOTP and proceed to eKYC navigation
    enter_totp(driver)
    navigate_to_ekyc(driver)

    # Add your further operations here for the automation tasks after reaching the dashboard

# Execute main function
if __name__ == "__main__":
    main()
