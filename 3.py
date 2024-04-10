import base64
import html
import json
import urllib.parse
import pandas as pd
from collections import Counter

file_path = r'D:\ProgramData\8.xls'

# 读取Excel文件并将编码字符串添加到input_data列表中
input_data = []
df = pd.read_excel(file_path, header=None)
input_data = df[0].tolist()


def detect_encoding(encoded_string):
    try:
        if isinstance(encoded_string, int):
            encoded_string = str(encoded_string)
        if all(char in 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789+/=' for char in encoded_string):
            # 检查长度是否符合 Base64 编码的特征
            if len(encoded_string) % 4 == 0:
                padding = encoded_string.count("=")
                if padding == 0:
                    return "Base64"
                elif padding == 1 or padding == 2:
                    return "带填充字符的Base64"
                else:
                    return "不是 Base64 编码"
    except Exception as e:
        pass

    if "&" in encoded_string:
        try:
            html.unescape(encoded_string)
            return "HTML"
        except:
            pass
    if "%" in encoded_string:
        try:
            urllib.parse.unquote(encoded_string)
            return "URL"
        except:
            pass
    try:
        json.loads(encoded_string)
        return "JSON"
    except:
        pass
    return "UTF-8"


# 统计编码类型
encoding_types = Counter()

for encoded_string in input_data:
    encoding_type = detect_encoding(encoded_string)
    encoding_types[encoding_type] += 1

# 输出统计结果
print("编码统计结果：")
for encoding_type, count in encoding_types.items():
    print(f"{encoding_type}: {count}")