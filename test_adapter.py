import sys 
import textwrap
from abc import ABCMeta
from collections import ChainMap

class Renderer(metaclass=ABCMeta):
    pass

class Page:
    def __init__(self, title, renderer: Renderer):
        self.renderer = renderer
        self.title = title 
        self.paragraphs = []

    def add_paragraph(self, paragraph):
        self.paragraphs.append(paragraph)

    def render(self):
        self.renderer.header(self.title)
        for paragraph in self.paragraphs:
            self.renderer.paragraph(paragraph)
        self.renderer.footer()

class TextRenderer:
    def __init__(self, width=00, file=sys.stdout):
        self.width = width
        self.file = file 
        self.previous = False

    def header(self, title):
        self.file.write(f"{title} {len(title)*'='}\n")
    
    def paragraph(self, text):
        if self.previous:
            self.file.write("\n")
        self.file.write(textwrap.fill(text, self.width))
        self.file.write("\n")
        self.previous = True

    def footer(self):
        pass 


def test_text_page():
    title = "HWS"
    textPage = Page(title, TextRenderer(22))
    textPage.add_paragraph("AAAAAAAAA")
    textPage.add_paragraph("BBBBBBBBB")
    textPage.render()
