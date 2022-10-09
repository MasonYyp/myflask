import os
from pdf2docx import Converter
import shutil


def pdf_to_word(pdf_dir, docx_dir):
    filename_list = os.listdir(pdf_dir)

    for filename in filename_list:
        print("转化：", filename)
        file_suffix = os.path.splitext(filename)[-1]

        if file_suffix == ".pdf":
            filename_docx = os.path.splitext(filename)[0] + '.docx'
            file_pdf_path = os.path.join(pdf_dir, filename)
            file_docx_path = os.path.join(docx_dir, filename_docx)
            cv = Converter(file_pdf_path)
            cv.convert(file_docx_path, start=0,end=None)
            cv.close()
        else:
            shutil.copy(os.path.join(pdf_dir, filename), os.path.join(docx_dir, filename))



if __name__ == '__main__':
    pdf_dir = "E:\\xi_data_new"
    docx_dir = "E:\\xi_data_new_docx"
    pdf_to_word(pdf_dir, docx_dir)