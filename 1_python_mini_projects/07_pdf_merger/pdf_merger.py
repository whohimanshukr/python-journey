"""PDF Merger Project

This script merges multiple PDF files into a single PDF using PyPDF2.
It asks the user how many PDF files to merge, collects file names one by one,
and then writes all collected PDF pages into a single output file.

Usage:
    python PyPDFMerger.py

Make sure the PDF file names you enter are correct and available in the
same folder as this script, or provide full paths.
"""

# Import PdfWriter from the PyPDF2 library to create and combine PDF documents.
from PyPDF2 import PdfWriter

# Create a PdfWriter object that will hold the merged PDF content.
merger = PdfWriter()

# Prepare an empty list to store the user-provided PDF file names.
pdfs = []

# Ask the user for the number of PDFs they want to merge.
# Convert the input string to an integer so we can use it in a loop.
n = int(input("How many PDFs do you want to merge?\n"))

# Loop over the range from 0 to n-1 to collect each PDF file name.
for i in range(0, n):
    # Prompt the user to enter the name of the next PDF file.
    name = input(f"Enter the name of the PDF {i + 1}: ")
    # Add the entered file name to the pdfs list for later processing.
    pdfs.append(name)

# Loop through the collected PDF file names and append them to the merger.
for pdf in pdfs:
    # Append each PDF file's content into the PdfWriter object.
    merger.append(pdf)

# Write the final merged PDF to a new file named PDFMerger.pdf.
merger.write("PDFMerger.pdf")

# Close the PdfWriter to release any system resources.
merger.close()