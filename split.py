# split.py
"""
A python script to split pdf-files into separate pages using pyPDF2
$ pip install pyPDF2
"""

import sys
import os
from PyPDF2 import PdfReader, PdfWriter

def split_pdf(path):
    fname = os.path.splitext(os.path.basename(path))[0]
    dest_dir = os.path.join(os.path.dirname(path), fname)
    if not os.path.exists(dest_dir):
        os.makedirs(dest_dir)
    pdf = PdfReader(path)
    for page in range(len(pdf.pages)):
        pdf_writer = PdfWriter()
        pdf_writer.add_page(pdf.pages[page])
        output_filename = '{}_page_{}.pdf'.format(fname, page+1)
        with open(os.path.join(dest_dir, output_filename), 'wb') as out:
            pdf_writer.write(out)
        print('Created: {}'.format(output_filename))

if __name__ == '__main__':

    # split pdf
    try:
        split_pdf(sys.argv[1])
    except:
        sys.exit("invalid filepath")
