import urllib.request
from docx import Document
from docx.shared import Inches

document = Document()

document.add_heading('My class', 0) # title

document.add_heading('Colegiul', level=1) # headings
document.add_heading('Costache Negruzzi', level=2)
document.add_heading('Iasi', level=3)

document.add_paragraph('Busiest days of the week').bold = True # unordered list
document.add_paragraph('Wednesday', style='ListBullet')
document.add_paragraph('Monday', style='ListBullet')
document.add_paragraph('Thursday', style='ListBullet')

document.add_paragraph('Best teachers').bold = True # ordered list
document.add_paragraph('Mr. Yes', style='ListNumber')
document.add_paragraph('Mrs. No', style='ListNumber')
document.add_paragraph('Ms. Maybe', style='ListNumber')

urllib.request.urlretrieve("http://placehold.it/1680x720", "placeholder.png") # retrieve picture
document.add_picture('placeholder.png', width=Inches(5)) # add picture


timetable = [
    {
        "first": "Rom", # Mon
        "second": "Mat",
        "third": "Rom",
        "fourth": "Eng",
        "fifth": "Drg"
    },
    {
        "first": "Bio", # Tue
        "second": "Fr",
        "third": "Ist",
        "fourth": "Mat",
        "fifth": "Fiz"
    },
    {
        "first": "Rom", # Wen
        "second": "Mat",
        "third": "Eng",
        "fourth": "Rom",
        "fifth": "Fiz"
    },
    {
        "first": "Bio", # Thu
        "second": "Mat",
        "third": "Mat",
        "fourth": "Info",
        "fifth": "Ch" 
    },
    {
        "first": "Ch", # Fri
        "second": "Inf",
        "third": "Inf",
        "fourth": "Fiz",
        "fifth": "Ed-Fiz"
    },

]

table = document.add_table(rows=1, cols=5)
cells = table.rows[0].cells
cells[0].text = 'Mon'
cells[1].text = 'Tue'
cells[2].text = 'Wen'
cells[3].text = 'Thu'
cells[4].text = 'Fri'

for item in timetable:
    row_cells = table.add_row().cells
    row_cells[0].text = item["first"]
    row_cells[1].text = item["second"]
    row_cells[2].text = item["third"]
    row_cells[3].text = item["fourth"]
    row_cells[4].text = item["fifth"]

document.add_page_break()

document.save('test.docx')




