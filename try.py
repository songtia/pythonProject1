import base64
import html
import json
import urllib.parse
import pandas as pd
from PIL import Image
from io import BytesIO

file_path = r'D:\ProgramData\8.xls'

# 读取Excel文件并将编码字符串添加到input_data列表中
df = pd.read_excel(file_path, header=None)
input_data = df[0].tolist()


def detect_encoding(encoded_string):
    # 尝试解码为图片
    try:
        decoded_image = base64.b64decode(encoded_string)
        image = Image.open(BytesIO(decoded_image))
        image.verify()  # 验证图片数据是否完整
        return "图片(Base64 编码)"
    except Exception as e:
        pass

    # JSON 编码检测
    try:
        json.loads(encoded_string)
        return "JSON"
    except:
        pass

    # HTML 编码检测
    try:
        if encoded_string != html.unescape(encoded_string):
            return "HTML"
    except:
        pass

    # URL 编码检测
    try:
        if encoded_string != urllib.parse.unquote(encoded_string):
            return "URL"
    except:
        pass

    # 默认认为是 UTF-8 编码
    return "UTF-8"


for encoded_string in input_data:
    encoding_type = detect_encoding(encoded_string)
    if encoding_type != "图片(Base64 编码)":
        print(f"{encoded_string} 是 {encoding_type} 编码")