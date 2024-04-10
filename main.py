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
    global count_images, count_json, count_html, count_url, count_utf8
    # 尝试解码为图片
    try:
        decoded_image = base64.b64decode(encoded_string)
        image = Image.open(BytesIO(decoded_image))
        image.verify()  # 验证图片数据是否完整
        count_images += 1
        return "图片(Base64 编码)"
    except Exception as e:
        pass

    # JSON 编码检测
    try:
        json.loads(encoded_string)
        count_json += 1
        return "JSON"
    except:
        pass

    # HTML 编码检测
    try:
        if encoded_string != html.unescape(encoded_string):
            count_html += 1
            return "HTML"
    except:
        pass

    # URL 编码检测
    try:
        if encoded_string != urllib.parse.unquote(encoded_string):
            count_url += 1
            return "URL"
    except:
        pass

    # 默认认为是 UTF-8 编码
    count_utf8 += 1
    return "UTF-8"


count_images = 0
count_json = 0
count_html = 0
count_url = 0
count_utf8 = 0

for encoded_string in input_data:
    encoding_type = detect_encoding(encoded_string)
    print(f"{encoded_string} 是 {encoding_type} 编码")

print("\n统计结果:")
print(f"图片(Base64 编码): {count_images}")
print(f"JSON: {count_json}")
print(f"HTML: {count_html}")
print(f"URL: {count_url}")
print(f"UTF-8: {count_utf8}")