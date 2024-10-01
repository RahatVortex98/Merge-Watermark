import PyPDF2

with open('dummy.pdf', mode='rb') as my_file:
    reader = PyPDF2.PdfReader(my_file)

    # Access the first page (0 index)
    # first_page = reader.pages[0]

    page_number=len(reader.pages)

    # Print the text from the first page
    # print(page_number)

    writer = PyPDF2.PdfFileWriter()
    with open('dummy2.pdf',mode='wb') as my_file2:
        writer.write(my_file2)
