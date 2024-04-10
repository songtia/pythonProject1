import base64
import json
import html
import random
import string

def generate_data_set(size=10000):
    data_set = []
    for _ in range(size):
        choice = random.randint(0, 3)
        if choice == 0:
            # 生成随机的 Base64 编码
            random_bytes = ''.join(random.choices(string.ascii_letters + string.digits + '+/', k=random.randint(10, 50)))
            encoded_data = base64.b64encode(random_bytes.encode()).decode()
            data_set.append(encoded_data)
        elif choice == 1:
            # 生成随机的 HTML 编码
            random_html = ''.join(random.choices(string.ascii_letters + string.digits + '><&;', k=random.randint(10, 50)))
            encoded_data = html.escape(random_html)
            data_set.append(encoded_data)
        elif choice == 2:
            # 生成随机的 JSON 编码
            random_json = '{"' + ''.join(random.choices(string.ascii_letters, k=random.randint(3, 10))) + '": ' + \
                          str(random.randint(1, 100)) + '}'
            data_set.append(random_json)
        else:
            # 生成随机的 UTF-8 编码
            random_utf8 = ''.join(random.choices(string.ascii_letters + '你好', k=random.randint(10, 50)))
            encoded_data = random_utf8.encode('utf-8')
            data_set.append(encoded_data)
    return data_set

def detect_encoding(data):
    if isinstance(data, str):
        if all(char in 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789+/=' for char in data) and len(data) % 4 == 0:
            # 检查长度是否符合 Base64 编码的特征
            if len(data) % 4 == 0:
                padding = data.count("=")
                if padding == 0:
                    return "是 Base64 编码"
                elif padding == 1 or padding == 2:
                    return "可能是 Base64 编码，带有填充字符"
                else:
                    return "不是 Base64 编码"
            else:
                return "不是 Base64 编码"

        if '%' in data:
            return "不是 Base64 编码"

        if '&lt;' in data or '&gt;' in data or '&#' in data:
            return "不是 Base64 编码"

        try:
            json.loads(data)
            return "不是 Base64 编码"
        except json.JSONDecodeError:
            pass

    elif isinstance(data, bytes):
        try:
            data.decode('utf-8')
            return "不是 Base64 编码"
        except UnicodeDecodeError:
            pass

    return "不是 Base64 编码"

def detect_encoding_accuracy(data_set):
    correct_count = 0
    for data in data_set:
        result = detect_encoding(data)
        if 'Base64' in result and isinstance(data, str):
            correct_count += 1
        elif '不是 Base64' in result and not isinstance(data, str):
            correct_count += 1
    accuracy = correct_count / len(data_set)
    return accuracy

# 测试数据集
data_set = generate_data_set()

# 检测编码类型准确率
accuracy = detect_encoding_accuracy(data_set)
print(f"准确率：{accuracy:.2%}")