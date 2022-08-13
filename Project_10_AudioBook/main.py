import pyttsx3 as speech
import PyPDF2 as pdf

# Open Book for reading
book = open('./Resources/resource.pdf', 'rb')
pdfReader = pdf.PdfFileReader(book)
total_pages = pdfReader.numPages

print(f" Total Pages in this book: {total_pages}")

starting_page = int(input("Enter starting page number: "))-1

# Speaker to start reading
speaker = speech.init()

# For changing sound property
voices = speaker.getProperty('voices')
speaker.setProperty('voice', voices[0].id)

for num in range(starting_page, total_pages):
    page = pdfReader.getPage(num)
    text = page.extractText()
    speaker.say(text)
    speaker.runAndWait()