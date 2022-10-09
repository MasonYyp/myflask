# -*- coding:utf-8 -*-

from win32com import client

import os
import shutil


# dir_old为原数据目录，dir_new为重命名后数据目录
def rename_file(dir_old, dir_new):
    # 获取文件列表
    filename_list = os.listdir(dir_old)
    for i in range(len(filename_list)):
        # 获取文件名称
        file_name = filename_list[i]
        # 获取文件后缀
        file_suffix = os.path.splitext(file_name)[-1]
        # 复制文件，并重命名
        shutil.copy(os.path.join(dir_old, file_name), os.path.join(dir_new, "file_" + str(i) + file_suffix))


def doc_to_docx(dir_old, dir_new):
    filename_list = os.listdir(dir_old)
    word = client.Dispatch("Word.Application")
    try:
        for filename in filename_list:
            file_suffix = os.path.splitext(filename)[-1]

            if file_suffix == ".doc":
                print("转换文件：", filename)
                filename_docx = os.path.splitext(filename)[0] + '.docx'
                file_doc_path = os.path.join(dir_old, filename)
                file_docx_path = os.path.join(dir_new, filename_docx)
                # 打开word文件
                doc = word.Documents.Open(file_doc_path)
                doc.SaveAs("{}".format(file_docx_path), 16)
                doc.Close()

            else:
                shutil.copy(os.path.join(dir_old, filename), os.path.join(dir_new, filename))

    except Exception as e:
        print(e)
    word.Quit()


if __name__ == "__main__":
    # 重命名文件
    # dir_old = r'E:\xi_data'
    # dir_new = r'E:\xi_data_new'
    # rename_file(dir_old, dir_new)

    # 支持文件夹批量导
    origin_dir = "E:\\xi_data_new"
    out_dir = "E:\\xi_docx"
    doc_to_docx(origin_dir, out_dir)



