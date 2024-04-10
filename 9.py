import base64


def detect_base64_origin(base64_data):
    # 图片特征码检查
    image_feature_codes = ["data:image/jpeg;base64,", "data:image/png;base64,", "data:image/gif;base64,"]
    for code in image_feature_codes:
        if base64_data.startswith(code):
            return "图片"

    # 文本特征码检查
    text_feature_codes = ["data:text/plain;base64,"]
    for code in text_feature_codes:
        if base64_data.startswith(code):
            return "文本"

    # 长度检查
    if len(base64_data) > 500:  # 设定一个阈值，超过该长度则认为是图片数据
        return "图片"

    # 字符集检查
    valid_characters = set("ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789+/=")
    if not set(base64_data).issubset(valid_characters):
        return "图片"

    # Magic Number检查
    magic_numbers = {
        b'\xff\xd8\xff': "图片/jpeg",
        b'\x89PNG\r\n\x1a\n': "图片/png",
        b'GIF87a': "图片/gif",
        b'GIF89a': "图片/gif",
        b'%PDF': "文档/pdf"  # 以PDF格式为例，可以继续添加其他常见文件类型的魔术数字
    }
    for magic, type_ in magic_numbers.items():
        if base64.b64decode(base64_data[:len(magic)]) == magic:
            return type_

    # 文件头部分析
    image_formats = {
        b'\xff\xd8\xff': "图片/jpeg",
        b'\x89PNG\r\n\x1a\n': "图片/png",
        b'GIF87a': "图片/gif",
        b'GIF89a': "图片/gif"
    }
    for magic, type_ in image_formats.items():
        if base64_data.find(magic) == 0:
            return type_

    # 数据结构分析
    try:
        decoded_data = base64.b64decode(base64_data)
        if decoded_data.startswith(b'%PDF'):
            return "文档/pdf"
        # 可以添加其他数据结构分析的逻辑
    except:
        pass

    # 模式匹配
    # 这里可以添加一些模式匹配的逻辑来判断文本数据的类型

    return "未知"


# 示例Base64编码字符串
base64_image = "data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAAAEAAAABCAQAAAC1HAwCAAAAC0lEQVR42mP8/B8AAwAB/AD+I9dQDAAAAABJRU5ErkJggg=="
base64_text = "data:text/plain;base64," + base64.b64encode("这是一段文本".encode('utf-8')).decode('utf-8')

# 检测
print(f"这个Base64编码来源于: {detect_base64_origin(base64_image)}")
print(f"这个Base64编码来源于: {detect_base64_origin(base64_text)}")