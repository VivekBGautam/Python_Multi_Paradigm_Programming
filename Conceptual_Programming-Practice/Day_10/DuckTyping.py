# Dick Typing : it is a concept where the type of an object is determined 
# By its behaviour, not by its class 

class InkjetPrinter:
    def PrintDocument(self,document):
        print("Inkjet Printer printing : ",document) 

class LeserPrinter:
    def PrintDocument(self,document):
        print("Leser Printer printing : ",document)

class PDFWriter:
    def PrintDocument(self,document):
        print(f"Saving {document} as PDF")
        print("Saving ",document," as PDF")

def StartPrinting(Devies):
    Devies.PrintDocument("Marvellous Notes")

def main():
    StartPrinting(InkjetPrinter())
    StartPrinting(LeserPrinter())
    StartPrinting(PDFWriter())

main()