from ebooklib import epub
from bs4 import BeautifulSoup
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer
from reportlab.lib.styles import getSampleStyleSheet
import ebooklib

book = epub.read_epub("Introduction-to-Data-Science-AAgah-20240620-1.epub")
pdf = SimpleDocTemplate("Introduction-to-Data-Science.pdf")
styles = getSampleStyleSheet()
story = []

for item in book.get_items():
    if item.get_type() == ebooklib.ITEM_DOCUMENT:
        soup = BeautifulSoup(item.get_content(), "html.parser")
        for line in soup.get_text().split("\n"):
            line = line.strip()
            if line:
                story.append(Paragraph(line, styles["Normal"]))
                story.append(Spacer(1, 10))

pdf.build(story)
