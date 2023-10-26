import pyttsx3
import pdfplumber
import PyPDF2
from deep_translator import GoogleTranslator
from googletrans import Translator

file = 'LePetitPrince.pdf'

pdfFileObj = open(file, 'rb')
pdfReader = PyPDF2.PdfFileReader(pdfFileObj)
pages = pdfReader.numPages
translator = Translator()
with pdfplumber.open(file) as pdf:
    for i in range(4, pages):
        page = pdf.pages[i]
        text = page.extract_text()
        # Verifica se o texto não está vazio ou None
        if text and text.strip():
            try:
                translation = GoogleTranslator(source='auto', target='pt').translate(text)
                print(translation)
                speaker = pyttsx3.init()
                speaker.say(translation)
                speaker.runAndWait()
            except Exception as e:
                print(f"Erro durante a tradução: {e}")
