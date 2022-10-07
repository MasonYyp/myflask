from paddleocr import PaddleOCR


class ImageAnalysis:

    def __init__(self):
        # 'use_gpu=False'不用gpu，默认使用GPU
        # 'use_angle_cls=True'自动下载相关的包
        # 'lang="ch"'设置语言，支持中英文、英文、法语、德语、韩语、日语，参数依次为`ch`, `en`, `french`, `german`, `korean`, `japan`。
        self._ocr = PaddleOCR(use_gpu=False, use_angle_cls=True, lang="ch", det_model_dir="./model/det", rec_model_dir='./model/rec')

    def img_to_text(self, img_path):
        result = self._ocr.ocr(img_path, cls=True)

        # line是一个列表' [[文本框的位置],(文字,置信度)] '
        for line in result:
            print(line)


def img_to_text():
    image_analysis = ImageAnalysis()
    image_path = "E:/xi_img/0.png"
    image_analysis.img_to_text(image_path)
    image_path = "E:/xi_img/1.png"
    image_analysis.img_to_text(image_path)


img_to_text()