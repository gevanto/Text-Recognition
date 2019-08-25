import cv2
import numpy as np
import pytesseract
from PIL import Image
from pytesseract import image_to_string
from googletrans import Translator

def get_string(src_path):
    result = pytesseract.image_to_string(Image.open(src_path))

    return result

#print("Code Begins")

pytesseract.pytesseract.tesseract_cmd = r"C:\Program Files\Tesseract-OCR\tesseract.exe"
src_path = r"C:\Users\Unken\Downloads\Video\casetwo.png"

#print(get_string(src_path))

textdetected = get_string(src_path)

translator = Translator()
translation_lang = ['en','ja','ko','fr','hi','es']

print("\nLaguage to translate into : ")
print(translation_lang)

lang = str(input("Enter your prefrence : "))

translated = translator.translate(textdetected , dest=lang)

print(translated.text)
