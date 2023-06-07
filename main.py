import PyPDF3
import pyttsx3
import pdfplumber


file = 'book.pdf'

book = open(file, 'rb')
pdfReader = PyPDF3.PdfFileReader(book)

pages = pdfReader.numPages

finalText = ""
 
with pdfplumber.open(file) as pdf:
    for i in range(0, pages):
        page = pdf.pages[i]
        text = page.extract_text()
        finalText += text

engine = pyttsx3.init()
# rate = engine.getProperty('rate')   # Getting details of current speaking rate
# print (rate)                        # Printing current voice rate
engine.setProperty('rate', 150) 

voices = engine.getProperty('voices') # Getting details of current voice
engine.setProperty('voice', voices[1].id) # Setting up the voice from male to female

engine.save_to_file(finalText, 'book.mp3') # Saving up the book to mp3 format in the current directory
engine.runAndWait()
