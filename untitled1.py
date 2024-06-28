
import keras
import pandas as pd
import numpy as np
# import matplotlib.pyplot as plt
# import seaborn as sns
import os
import cv2
import tensorflow as tf
from tensorflow.keras import layers, Sequential
from tqdm import tqdm

from sklearn.model_selection import train_test_split
from tensorflow.keras.metrics import Precision, Recall, AUC, F1Score

# !pip install kaggle
#para dar o comando abaixo foi necessario pegar a chave da api "arquivo json" do kaggle e adicionar na pasta do kaggle no raiz do colabs
# !kaggle datasets download -d quadeer15sh/lfw-facial-recognition
#
# !unzip -q -u lfw-facial-recognition.zip
@keras.saving.register_keras_serializable(package="MyLayers")
class DistanceLayer(tf.keras.layers.Layer):
    def __init__(self):
        super().__init__()
    def call(self, vec1, vec2):
        return tf.square(vec1 - vec2)

class SiameseNetwork(tf.keras.Model):
    def __init__(self):
        super().__init__()
        self.encoder = Sequential([
            layers.Conv2D(32, kernel_size = (3, 3), strides = 1, padding = 'same', activation = 'relu'),
            layers.BatchNormalization(),
            layers.MaxPooling2D(pool_size = (2, 2), strides = 1),

            layers.Conv2D(32, kernel_size = (3, 3), strides = 1, padding = 'same', activation = 'relu'),
            layers.BatchNormalization(),
            layers.MaxPooling2D(pool_size = (2, 2), strides = 1),

            layers.Conv2D(32, kernel_size = (3, 3), strides = 1, padding = 'same', activation = 'relu'),
            layers.BatchNormalization(),
            layers.MaxPooling2D(pool_size = (2, 2), strides = 1),

            layers.Flatten(),
            layers.Dense(128, activation = 'relu'),
            layers.BatchNormalization(),
            layers.Dense(16)
        ])
        self.get_distance = DistanceLayer()
        self.output_layer = layers.Dense(1, activation = 'sigmoid')

    def call(self, args):
        x1, x2 = args
        embedding1, embedding2 = self.encoder(x1), self.encoder(x2)
        distance = self.get_distance(embedding1, embedding2)
        out = self.output_layer(distance)
        return out

folder_path = "./Face Recognition/Faces"
nums = []
images = []
dictimages = {}
images_name = []
img_size = 64
for i, img_name in tqdm(enumerate(os.listdir(folder_path))):
    img_path = os.path.join(folder_path, img_name)
    img_array = cv2.imread(img_path)
    img_array = cv2.resize(img_array, (img_size, img_size))
    img_array = img_array[:, :, ::-1] / 255.0
    images_name.append(img_name)
    dictimages[img_name] = img_array
    images.append(img_array)
    nums.append(i)
images = np.array(images, dtype = 'float32').reshape(-1, img_size, img_size, 3)
nums = np.array(nums, dtype = 'float32')
images.shape, nums.shape

test = pd.read_csv("./Face Recognition/test.csv")
trainn = pd.read_csv("./Face Recognition/train.csv")

train, val = train_test_split(trainn, test_size=0.2, random_state=42)

train.reset_index(drop=True, inplace=True)
val.reset_index(drop=True, inplace=True)

X1_test = []
X2_test = []
y_test = []
for i in tqdm(range(len(test['Image1']) - 1)):
    X1_test.append(dictimages[test['Image1'][i]])
    X2_test.append(dictimages[test['Image2'][i]])
    y_test.append(test['class'].apply(lambda x: 1 if x=='similar' else 0)[i])

X1_test = np.array(X1_test)
X2_test = np.array(X2_test)
y_test = np.array(y_test)
X1_test.shape, X2_test.shape, y_test.shape


X1_train = []
X2_train = []
y_train = []
for i in tqdm(range(len(train['Image1']) - 1)):
    X1_train.append(dictimages[train['Image1'][i]])
    X2_train.append(dictimages[train['Image2'][i]])
    y_train.append(train['class'].apply(lambda x: 1 if x=='similar' else 0)[i])

X1_train = np.array(X1_train)
X2_train = np.array(X2_train)
y_train = np.array(y_train)
X1_train.shape, X2_train.shape, y_train.shape

X1_val = []
X2_val = []
y_val = []
for i in tqdm(range(len(val['Image1']) - 1)):
    X1_val.append(dictimages[val['Image1'][i]])
    X2_val.append(dictimages[val['Image2'][i]])
    y_val.append(val['class'].apply(lambda x: 1 if x=='similar' else 0)[i])

X1_val = np.array(X1_val)
X2_val = np.array(X2_val)
y_val = np.array(y_val)
X1_val.shape, X2_val.shape, y_val.shape

X1_test.shape, X2_test.shape, y_test.shape

print(X1_train)
# X1_train['class']
# X1_val['class']

model = SiameseNetwork()
model.compile(optimizer = 'adam', loss = 'binary_crossentropy', metrics = ['accuracy',Recall()])

model.fit([X1_train, X2_train], y_train, epochs = 25, validation_data=([X1_val, X2_val], y_val))

model.save("faceRecognition.keras", save_format="keras")
# Pass the custom objects dictionary to a custom object scope and place
# the `keras.models.load_model()` call within the scope.






x1 = np.array(X1_test[4], dtype = 'float32').reshape(-1, img_size, img_size, 3)
x2 = np.array(X2_test[4], dtype = 'float32').reshape(-1, img_size, img_size, 3)

print(model.predict([x1, x2]))

