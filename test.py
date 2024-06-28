import tensorflow as tf
import keras
from untitled1 import DistanceLayer
custom_objects = {"DistanceLayer": DistanceLayer}

with keras.saving.custom_object_scope(custom_objects):
    reconstructed_model = keras.models.load_model("faceRecognition.keras")