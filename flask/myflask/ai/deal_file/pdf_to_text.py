"""
import PyPDF2
from PyPDF2.errors import DependencyError

def parse_pdf(pdf_path):
    pdf_file_obj = open(pdf_path, 'rb')
    try:
        pdf_reader = PyPDF2.PdfFileReader(pdf_file_obj)
    except DependencyError as e:
        print(e)
        return "-1"

    # 判断文件是否加密
    if pdf_reader.isEncrypted:
        # decrypt方法是输入加密的密码对返回1，错返回0
        return "-1"
    # 获取pdf文件的页数
    page_len = pdf_reader.numPages
    text = ""
    for page_num in range(page_len):

        cur_page = pdf_reader.getPage(page_num)
        temp_text = cur_page.extractText()

        # 清洗text
        temp_text = temp_text.encode(errors="utf-8").decode(errors='ignore', encoding="utf-8")
        temp_text = temp_text.replace('\t', '').replace('\n', '').replace('\r\n', '')
        temp_text = ' '.join(temp_text.split())
        text = text + temp_text

    return text

"""

import fitz


# 此种方法可以解析含有“许可口令”的pdf文件
def parse_pdf(pdf_path):
    doc_obj = fitz.open(pdf_path)
    pages = doc_obj.pages()

    text = ""
    for page in pages:
        temp_text = page.get_text()

        # 清洗text
        temp_text = temp_text.encode(errors="utf-8").decode(errors='ignore', encoding="utf-8")
        temp_text = temp_text.replace('\t', '').replace('\n', '').replace('\r\n', '')
        temp_text = ' '.join(temp_text.split())
        text = text + temp_text

    return text

