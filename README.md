# Electoral-Roll

Python: Extracting content from PDF file and dumping structured data to MS-Excel
---
Following are steps to run the code:

**1.** Install PyPDF2. You can pip install. You can download it [here](https://pypi.python.org/pypi/PyPDF2/)

**2.** Open the file 'extract_pdf.py'

**3.** In line 7 specify the path of the folder/directory which has all the PDF Electoral roll data

For example:

        directory = 'E:\Python\Github_Portfolio\source'

**4.** In line 15 and line 16 specify the start and end page numbers of the PDF files. The end page number could be made dynamic as desired. Here the 'num_pg' variable is the total page number.

For example:
        
        start_pno = 2
              
        end_pno = num_pg-1

**5.** Run the code!


There will be an output file (Excel file) named 'output.xlsx' which has the electoral data
