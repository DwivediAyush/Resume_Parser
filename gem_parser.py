import os
import sys
from pyresparser import ResumeParser
import subprocess


def change_directory(filename):
    file_dir = filename.split('/',-1)
    file_dir = '/'.join(file_dir[0:-1])
    os.chdir(file_dir)

def resume_data(filename):
    change_directory(filename)
    if not filename.endswith('.pdf'):
        if filename.endswith('doc') or filename.endswith('docx'):
            filename = doc_to_pdf(filename)
        else:
            print("Only 'pdf', 'doc' and 'docx' file format supported")
            sys.exit(1)
    Resume_Data = ResumeParser(filename).get_extracted_data()
    os.remove(filename)
    return Resume_Data


def doc_to_pdf(filename):
    subprocess.call(['soffice', '--headless', '--convert-to', 'pdf',filename],stdout=subprocess.DEVNULL,stderr=subprocess.STDOUT)    
    if filename.endswith('doc'):
        filename = filename[0:-4] + ".pdf"
    if filename.endswith('docx'):
        filename = filename[0:-5] + ".pdf"
    return filename


    




    



    
  