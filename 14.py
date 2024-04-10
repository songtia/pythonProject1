import base64
from PIL import Image

def image_to_base64(image_path):
    with open(image_path, "rb") as img_file:
        # 读取图像文件
        img = img_file.read()
        # 将图像数据转换为base64编码
        base64_data = base64.b64encode(img)
        # 将base64编码的数据以字符串形式返回
        return base64_data.decode('utf-8')

# 输入图片文件路径
image_path = input("请输入图片文件路径：")

try:
    # 将图像文件转换为base64编码并输出
    base64_encoded = image_to_base64(image_path)
    print("Base64编码结果：", base64_encoded)
except FileNotFoundError:
    print("找不到指定的文件，请确保路径正确并重新输入。")