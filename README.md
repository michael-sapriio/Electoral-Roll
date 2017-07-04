# Electoral-Roll
Python - Extracting Electoral roll content from PDF format and dumping structured data to MS-Excel

Following are steps to run the code:
Step 1: Open the file 'extract_pdf.py'
Step 2: In line 7 specify the path of the folder/directory which has all the PDF Electoral roll data
        For example in my computer the directory path is:
          directory = 'E:\Python\Github_Portfolio\source'
Step 3: In line 15 and 16 specify the start and end page numbers of the PDF files. The end page number could be made dynamic
        as desired. Here the 'num_pg' variable is the total page number.
        For example:
          start_pno = 2
          end_pno = num_pg-1
Step 4: Run the code!

There will be an output file (excel file) named 'output.xlsx' which has the electoral data
