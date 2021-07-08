import pyttsx3
import pdfplumber
import PyPDF2
from googletrans import Translator

file = 'LePetitPrince.pdf'

pdfFileObj = open(file, 'rb')
pdfReader = PyPDF2.PdfFileReader(pdfFileObj)
pages = pdfReader.numPages
translator = Translator()
with pdfplumber.open(file) as pdf:
    for i in range(12, pages):
        page = pdf.pages[i]
        text = page.extract_text()
        translation = translator.translate(text, dest='pt')
        print(translation.text)
        speaker = pyttsx3.init()
        speaker.say(translation)
        speaker.runAndWait()