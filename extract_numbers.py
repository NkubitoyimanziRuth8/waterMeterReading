
import cv2
import numpy as np
import pytesseract

sharpened_image = cv2.imread('./images/image.png', flags=cv2.IMREAD_COLOR)

if sharpened_image is None:
    print("Error: Unable to load image from the specified path.")
else:
    gray_image = cv2.cvtColor(sharpened_image, cv2.COLOR_BGR2GRAY)

    _, threshold_image = cv2.threshold(gray_image, 0, 255, cv2.THRESH_BINARY_INV + cv2.THRESH_OTSU)

    custom_config = r'--psm 6 outputbase digits'
    extracted_text = pytesseract.image_to_string(threshold_image, lang='eng', config=custom_config)

    output_file_path = 'text.txt'
    with open(output_file_path, 'a') as file:
        file.write("\n" + extracted_text.strip())  # Append extracted text on a new line

    print("Numbers extracted from the sharpened image have been saved to:", output_file_path)
