# Electoral-Roll

Python: Extracting content from PDF file to Microsoft Excel
---
Description
---
This simple python code will iterate through a folder/directory containing electoral rolls (Voter Lists) in PDF format, extract contents from it, apply regular expressions and dump the clean text (Structured attributes) into Microsoft Excel. The code will create intermediate ```.txt``` files before applying the ```regex```, and delete them on completion. As the desired output, it will create an ```.xlsx``` file with the voter list. Each row in the output file corresponds to the information (House Number, Name, Father's/Husband's name, Age) of a voter. The code is I/O intensive, since we are reading/writing multiple files.

Execution Steps
---
I'm assuming you already have `numpy` and `pandas` installed

Following are the steps to run the code:

**1.** Install `PyPDF2`. Since `PyPDF2` is on the Python Package Index, you can use `pip` to install it as:

```     
pip install PyPDF2
```
        
Or you can download the Package [Here](https://pypi.python.org/pypi/PyPDF2/). In Windows you can extract the `tar.gz` file and then `cd` to the extracted directory and do:
        
```     
python setup.py install
```

**2.** Open the file `extract_pdf.py`

**3.** In **line 7** specify the path of the folder/directory which has all the PDF Electoral roll data

For example:

```python 
directory = 'E:\Python\Github_Portfolio\source'
```

**4.** In **line 15** and **line 16** specify the start and end page numbers of the PDF files. The end page number could be made dynamic as desired. Here the `num_pg` variable is the total page number.

For example:

```python
start_pno = 2       
end_pno = num_pg-1
```

**5.** Run the code!


There will be an output file named `output.xlsx` which has the electoral data

Code customization
---
In **line 56** we have put headers based on the attributes we want.

```python
df = pd.DataFrame(row, columns = ['House No', 'Gender', 'Name', 'Age',
                                  'Father\'s/Husband\'s Name'])
```

The `DateFrame` can be customized depending on the attributes you are interested in.

Better Regex
---

The `regex` used in the code could be improved. I am still learning how to use them more efficiently and less messy like this one. Also, the `regex` code will vary with the content you are trying to extract. Here I am using whitespaces actively to breakdown text lines into tokens. If there are more efficient ways (I am sure there will be), please give me feedback. I will learn too! :)
