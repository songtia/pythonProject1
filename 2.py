import pandas as pd
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score
from sklearn.utils import shuffle

# 读取文本数据CSV文件和图片数据XLS文件，设定header=None
text_data = pd.read_csv('D:\\ouput.csv', header=None)
image_data = pd.read_excel('D:\\8.xls', header=None)  # 使用read_excel()函数读取XLS文件，文件路径需要正确

# 清理image_data中的数据，确保每个base64编码字符串都是有效的
image_data[0] = image_data[0].str.strip()  # 清理字符串两端的空格

# 定义一个函数来将base64编码的图像数据解码为图像对象
def decode_image(base64_string):
    # 此处不做解码，直接返回编码字符串
    return base64_string

# 不再解码图像数据
image_data['decoded_data'] = image_data[0].apply(decode_image)

# 提取n-gram特征
vectorizer = CountVectorizer(analyzer='char', ngram_range=(2, 2))
text_features = vectorizer.fit_transform(text_data[0])
image_features = vectorizer.fit_transform(image_data['decoded_data'].astype(str))  # 转换为字符串以满足CountVectorizer的要求

# 准备训练数据
X_text = text_features
X_image = image_features
y_text = pd.Series([0] * len(text_data))
y_image = pd.Series([1] * len(image_data))

# 打乱数据集顺序
X_text, y_text = shuffle(X_text, y_text, random_state=42)
X_image, y_image = shuffle(X_image, y_image, random_state=42)

# 合并文本和图像特征
X = pd.concat([pd.DataFrame(X_text.toarray()), pd.DataFrame(X_image.toarray())])
y = pd.concat([y_text, y_image])

# 划分训练集和测试集
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# 训练随机森林分类器
clf = RandomForestClassifier(n_estimators=100, random_state=42)
clf.fit(X_train, y_train)

# 在测试集上评估模型
#y_pred = clf.predict(X_test)
#accuracy = accuracy_score(y_test, y_pred)
#print("Accuracy:", accuracy)

user_input_base64 = input("请输入您要判断的 base64 编码：")

# 使用模型进行预测
data_type = clf.predict(vectorizer.transform([user_input_base64]))
if data_type == 1:
    print("Predicted data type: image")
else:
    print("Predicted data type: text")