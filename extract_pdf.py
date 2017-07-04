import os
import PyPDF2
import re
import pandas as pd
import numpy as np

directory = 'E:\Python\Github_Portfolio\source'

for filename in os.listdir(directory):
    if filename.endswith(".pdf"):
        src_file = open(os.path.join(directory, filename),'rb')
        pdfreader = PyPDF2.PdfFileReader(src_file)
        num_pg = pdfreader.getNumPages()

        start_pno = 2
        end_pno = num_pg-1
        
        for pg in range(start_pno,end_pno):
            pageob = pdfreader.getPage(pg)
            try:
                dest_file = open('pdf_content.txt','a')
            except FileNotFoundError:
                dest_file = open('pdf_content.txt','w')

            dest_file.write(pageob.extractText())
            dest_file.close()

        src_file.close()

out_file = open('pdf_line_content.txt','w')
new_file = open('pdf_content.txt','rb')

s = new_file.read()
strn = re.split(' No',str(s))
out_file.write('\n'.join(strn))

new_file.close()
out_file.close()

out_fl = open('pdf_line_content.txt','r')

row = []

for eachline in out_fl.readlines():
    h_no = re.findall(r'\s:\s(.*?)Gender',eachline)
    gender = re.findall(r'.Gender\s:\s(.*?)Age',eachline)
    name = re.findall(r'.\dName\s:\s(.*?)\s',eachline)
    age = re.findall(r'[A-Z]*\s\s(\d\d)\s.\w',eachline)
    f_name = re.findall(r'\sName\s:\s(.*?)\s\s\d\d',eachline)
    row.append((h_no,gender,name,age,f_name))

out_fl.close()
os.remove('pdf_content.txt')
os.remove('pdf_line_content.txt')

df = pd.DataFrame(row, columns = ['House No', 'Gender', 'Name', 'Age',
                                  'Father\'s/Husband\'s Name'])

for colmn in df.columns:
    df[colmn] = df[colmn].apply(lambda i: ''.join(i)) 

df.replace('', np.nan, inplace=True)
df.dropna(how = 'all', inplace=True)

writer = pd.ExcelWriter('output.xlsx')
df.to_excel(writer,'Content')

writer.save()
