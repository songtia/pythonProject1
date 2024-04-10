import base64


def detect_base64_origin(base64_data):
    # 特征码检查
    image_feature_codes = ["data:image/jpeg;base64,", "data:image/png;base64,", "data:image/gif;base64,"]

    for code in image_feature_codes:
        if base64_data.startswith(code):
            return "图片"

    # 长度检查
    if len(base64_data) > 500:  # 设定一个阈值，超过该长度则认为是图片数据
        return "图片"

    # 字符集检查
    valid_characters = set("ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789+/=")
    if not set(base64_data).issubset(valid_characters):
        return "文本"

    return "文本"


# 示例Base64编码字符串
base64_image = "data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAAAEAAAABCAQAAAC1HAwCAAAAC0lEQVR42mP8/B8AAwAB/AD+I9dQDAAAAABJRU5ErkJggg=="
base64_text = base64.b64encode("这是一段文本".encode('utf-8')).decode('utf-8')
base64_random = "AaBbCcDdEeFfGgHhIiJjKkLlMmNnOoPpQqRrSsTtUuVvWwXxYyZz0123456789"

# 检测
print(f"这个Base64编码来源于: {detect_base64_origin(base64_image)}")
print(f"这个Base64编码来源于: {detect_base64_origin(base64_text)}")
print(f"这个Base64编码来源于: {detect_base64_origin(base64_random)}")