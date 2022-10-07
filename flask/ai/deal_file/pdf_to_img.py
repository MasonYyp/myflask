"""
# 方法1使用python-office
# 安装python-office包
# pip install -i https://pypi.tuna.tsinghua.edu.cn/simple python-office -U

import office

# 一行代码，实现转换
# 参数说明：
# pdf_path = 你的PDF文件的地址
# out_dir = 转换后的图片存放地址，可以不填，默认是PDF的地址

office.pdf.pdf2imgs(
    pdf_path='E:/xi_data_special/file_pwd.pdf',
    out_dir='E:/xi_img'
)
"""

# 方法2
# 安装pymupdf包
# pip install pymupdf

# import os
# import fitz
#
#
# def pdf_to_img(pdf_path, img_dir):
#     doc_obj = fitz.open(pdf_path)
#
#     for i in range(doc_obj.page_count):
#         page = doc_obj.load_page(i)
#         pixmap = page.get_pixmap()
#         pixmap.save(os.path.join(img_dir, str(i)+".png"))

#
# pdf_path = "E:/xi_data_special/file_pwd.pdf"
# img_dir = "E:/xi_img"
# pdf_to_img(pdf_path, img_dir)


import os
import fitz

# 此种方法可以解析含有“许可口令”的pdf文件
def pdf_to_text(pdf_path):
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

    # for i in range(doc_obj.page_count):
    #     page = doc_obj.load_page(i)
    #     pixmap = page.get_pixmap()
    #     pixmap.save(os.path.join(img_dir, str(i) + ".png"))


pdf_to_text("E:/xi_data_special/file_pwd.pdf")
