from selenium import webdriver
from selenium.webdriver.common.by import By
import time
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

import easyocr
import cv2
import numpy as np
from PIL import Image
import io
from PIL import ImageEnhance

def binarize_image(image_bytes):
    """Convert image bytes to a binary (black and white) image."""
    # Convert bytes to a PIL Image
    image = Image.open(io.BytesIO(image_bytes))
    
    # Convert to grayscale
    grayscale = image.convert("L")
    
    # Apply binarization
    binary_image = grayscale.point(lambda x: 0 if x < 128 else 255, '1')
    return binary_image

def enhance_contrast(image, factor=2):
    """Enhance the contrast of the image."""
    if image.mode == '1':
        # Convert binary image to 'L' mode for enhancement
        image = image.convert('L')
    enhancer = ImageEnhance.Contrast(image)
    return enhancer.enhance(factor)

def denoise_image(image):
    """Remove noise from the image using OpenCV."""
    open_cv_image = np.array(image.convert('RGB'))  # Convert to RGB format
    open_cv_image = cv2.fastNlMeansDenoisingColored(open_cv_image, None, 10, 10, 7, 21)
    return Image.fromarray(open_cv_image)

def main():
    login_link = "https://rcms.mahafood.gov.in/OfficeLogin.aspx"

    # Initialize WebDriver
    driver = webdriver.Chrome()
    driver.get(login_link)

    # Wait for the CAPTCHA element to load
    captcha_element = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.ID, "ContentPlaceHolder1_CaptchaImage"))
    )
    
    # Capture the CAPTCHA image
    captcha_png = captcha_element.screenshot_as_png

    # Process the image
    image = binarize_image(captcha_png)
    image = enhance_contrast(image)
    image = denoise_image(image)

    # Initialize EasyOCR reader with GPU support
    reader = easyocr.Reader(['en'], gpu=True)

    # Read the text from the image
    result = reader.readtext(np.array(image))  # Convert to NumPy array for EasyOCR

    # Display results
    for detection in result:
        bbox, text, confidence = detection
        print(f"Detected Text: {text}, Confidence: {confidence:.2f}")

    # Extract text only (assuming you want the most confident text result)
    captcha_text = ' '.join([detection[1] for detection in result])
    print("Extracted CAPTCHA Text:", captcha_text)

    time.sleep(300)
    # Close the driver
    driver.quit()

if __name__ == "__main__":
    main()
      # Pause to see the output if necessary
