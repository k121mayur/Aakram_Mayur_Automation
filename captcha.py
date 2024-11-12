import pytesseract
from PIL import Image
import io
def extract_captcha_text(captcha_element):
    """
    This function takes a Selenium WebElement (for an image) as input and
    returns the text in the CAPTCHA by using OCR.

    Args:
    captcha_element (WebElement): The WebElement of the CAPTCHA image.

    Returns:
    str: The extracted text from the CAPTCHA image.
    """
    # Capture the screenshot of the CAPTCHA element
    captcha_png = captcha_element.screenshot_as_png  # Get image in PNG format

    # Convert the screenshot to a PIL Image
    captcha_image = Image.open(io.BytesIO(captcha_png))

    # Use pytesseract to extract text from the image
    captcha_text = pytesseract.image_to_string(captcha_image)

    # Clean up the extracted text
    captcha_text = captcha_text.strip()
    
    return captcha_text