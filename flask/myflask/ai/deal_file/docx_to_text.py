import docx

def parse_docx(docx_path):
    # 读取docx文件
    file_docx = docx.Document(docx_path)
    text = ""

    # 读取段落
    for paragraph in file_docx.paragraphs:
        temp_text = str(paragraph.text)
        temp_text = temp_text.encode(errors="utf-8").decode(errors='ignore', encoding="utf-8")
        temp_text = temp_text.replace('\t', '').replace('\n', '').replace('\r\n', '')
        temp_text = ' '.join(temp_text.split())

        # 删除空段落
        if temp_text != "":
            text = text + temp_text

    return text
