# Electoral-Roll

Python: Extracting content from PDF file to Microsoft Excel
---
Following are the steps to run the code:

**1.** Install `PyPDF2`. Since `PyPDF2` is on the Python Package Index, you can use `pip` to install it as:

        pip install PyPDF2
        
Or you can download the Package [Here](https://pypi.python.org/pypi/PyPDF2/). In Windows you can extract the `tar.gz` file and then `cd` to the extracted directory and do:
        
        python setup.py install

**2.** Open the file `extract_pdf.py`

**3.** In line 7 specify the path of the folder/directory which has all the PDF Electoral roll data

For example:

        ```python 
        directory = 'E:\Python\Github_Portfolio\source'
        ```

**4.** In line 15 and line 16 specify the start and end page numbers of the PDF files. The end page number could be made dynamic as desired. Here the `num_pg` variable is the total page number.

For example:

        ```python
        start_pno = 2
              
        end_pno = num_pg-1
        ```

**5.** Run the code!


There will be an output file named `output.xlsx` which has the electoral data
