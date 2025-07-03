import os
import datetime   # Agregar la importación de datetime
os.environ['TF_ENABLE_ONEDNN_OPTS'] = '0'

import numpy as np
from model import NUM_EPOCH, get_model
from keras.preprocessing.sequence import pad_sequences
from keras.utils import to_categorical
from helpers import get_actions, get_sequences_and_labels
from constants import MAX_LENGTH_FRAMES, MODEL_NAME
from keras.callbacks import TensorBoard   # Importar TensorBoard

def training_model(data_path, model_path):
    actions = get_actions(data_path)
   
    sequences, labels = get_sequences_and_labels(actions, data_path)
    
    sequences = pad_sequences(sequences, maxlen=MAX_LENGTH_FRAMES,padding='post', truncating='post', dtype='float32')

    X = np.array(sequences)
    y = to_categorical(labels).astype(int)
    
    model = get_model(len(actions))
    
    # Crear el callback de TensorBoard
    log_dir = os.path.join("logs", "fit", datetime.datetime.now().strftime("%Y%m%d-%H%M%S"))
    tensorboard_callback = TensorBoard(log_dir=log_dir, histogram_freq=1)
    
    # Entrenar el modelo con el callback de TensorBoard
    model.fit(X, y, epochs=NUM_EPOCH, callbacks=[tensorboard_callback])
    model.summary()
    model.save(model_path)

    # tensorboard --logdir=logs/fit -> Ejecutar en la terminal para ver el tensorboard

if __name__ == "__main__":
    root = os.getcwd()
    data_path = os.path.join(root, "data")
    save_path = os.path.join(root, "models")
    model_path = os.path.join(save_path, MODEL_NAME)
    
    training_model(data_path, model_path)