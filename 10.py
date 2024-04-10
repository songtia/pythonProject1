import base64
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.naive_bayes import MultinomialNB
from sklearn.metrics import accuracy_score

# 示例数据，包括图片和文本数据的 base64 编码
image_base64 = [
    "iVBORw0KGgoAAAANSUhEUgAAABAAAAAQCAMAAAAoLQ9TAAAABGdBTUEAALGPC/xhBQAAAAFzUkdCAK7OHOkAAAADUExURQX7A/71H4/0/+n1AAC9LkltAAAABlBMVEX///8AAABVwtN+AAAAJElEQVR42mL8//8/AyUYTFxAGGhoYmBhYoHioYGAwCYAOl8fO3P2CwAAAABJRU5ErkJggg==",
    "iVBORw0KGgoAAAANSUhEUgAAAAEAAAABCAIAAACQd1PeAAAACXBIWXMAABYlAAAWJQFJUiTwAAAAVklEQVQImWNgQAAXzwWP8l8UzKgFMDAwMWjJ3tTsDAwAA9AJ6vP9n8KoAAAAASUVORK5CYII="
]

text_base64 = [
    "VGhpcyBpcyBhIHRlc3Qgc3RyaW5nIGluIGJhc2U2NCBlbmNvZGluZw==",
    "U29ycnksIEkgY2FuIGJlIGEgZ3JlYXQgZXhhbXBsZSB3aXRoIHNvbWUgYmFzZTY0IGVuY29kaW5n"
]

# 更多的示例数据集
more_image_base64 = [
    "iVBORw0KGgoAAAANSUhEUgAAABAAAAAQCAMAAAAoLQ9TAAAABGdBTUEAALGPC/xhBQAAAAFzUkdCAK7OHOkAAAADUExURQX7A/71H4/0/+n1AAC9LkltAAAABlBMVEX///8AAABVwtN+AAAAJElEQVR42mL8//8/AyUYTFxAGGhoYmBhYoHioYGAwCYAOl8fO3P2CwAAAABJRU5ErkJggg==",
    "iVBORw0KGgoAAAANSUhEUgAAAAEAAAABCAIAAACQd1PeAAAACXBIWXMAABYlAAAWJQFJUiTwAAAAVklEQVQImWNgQAAXzwWP8l8UzKgFMDAwMWjJ3tTsDAwAA9AJ6vP9n8KoAAAAASUVORK5CYII="
]

more_text_base64 = [
    "VGhpcyBpcyBhIHRlc3Qgc3RyaW5nIGluIGJhc2U2NCBlbmNvZGluZw==",
    "U29ycnksIEkgY2FuIGJlIGEgZ3JlYXQgZXhhbXBsZSB3aXRoIHNvbWUgYmFzZTY0IGVuY29kaW5n"
]

# 准备数据
image_data = image_base64 + more_image_base64
text_data = text_base64 + more_text_base64
labels = ["image"] * len(image_data) + ["text"] * len(text_data)

# 将 base64 编码的字符串转换为 n-gram 特征向量
def get_ngram_features(data, n=3):
    vectorizer = CountVectorizer(analyzer='char', ngram_range=(n, n))
    X = vectorizer.fit_transform(data)
    return X.toarray(), vectorizer

# 训练朴素贝叶斯分类器
def train_classifier(X, y):
    clf = MultinomialNB()
    clf.fit(X, y)
    return clf

# 提取 n-gram 特征
X, vectorizer = get_ngram_features(image_data + text_data)

# 划分训练集和测试集
X_train, X_test, y_train, y_test = train_test_split(X, labels, test_size=0.2, random_state=42)

# 训练分类器
classifier = train_classifier(X_train, y_train)

# 预测并评估模型
y_pred = classifier.predict(X_test)
accuracy = accuracy_score(y_test, y_pred)
print("Accuracy:", accuracy)