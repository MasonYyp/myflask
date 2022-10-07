from captcha.image import ImageCaptcha
import random

import base64
import uuid

"""
Generate the captcha
"""


class OperateCaptcha:

    # Generate the code
    def generate_code(self, code_len=4):
        code_chars = '0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'
        chars_len = len(code_chars) - 1
        code = ''
        for _ in range(code_len):
            index = random.randint(0, chars_len)
            code = code + code_chars[index]
        return code

    # Generate the base64 image of captcha
    def generate_captcha_base64(self, code):
        # Generate image captcha
        img_captcha = ImageCaptcha()
        # Generate the BytesIO
        img_bytes_io = img_captcha.generate(code)

        # Translate image to base64
        image_base64 = base64.b64encode(img_bytes_io.read())
        image_base64_str = "data:image/png;base64," + str(image_base64, 'utf-8')
        return image_base64_str

    # Generate the key of code
    def generate_code_key(self):
        # Generate the uuid
        code_key = str(uuid.uuid1())
        return code_key


operate_captcha = OperateCaptcha()
