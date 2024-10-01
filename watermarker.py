import PyPDF2

# Open the template and watermark PDF files
template = PyPDF2.PdfReader(open('super.pdf', 'rb'))
watermark = PyPDF2.PdfReader(open('wtr.pdf', 'rb'))

# Initialize PdfWriter
output = PyPDF2.PdfWriter()

# Loop through each page of the template PDF
for i in range(len(template.pages)):  # Use len(template.pages)
    page = template.pages[i]  # Access the page using pages attribute
    page.merge_page(watermark.pages[0])  # Merge watermark
    output.add_page(page)  # Add the modified page to the writer

# Write the output PDF
with open('watermarker_output.pdf', 'wb') as file:
    output.write(file)  # Write all the pages to the new PDF
