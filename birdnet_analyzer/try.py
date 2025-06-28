import tensorflow as tf

model = tf.saved_model.load("./model/BirdNET_6K_GLOBAL_MODEL.tflite")
print(list(model.signatures.keys()))
