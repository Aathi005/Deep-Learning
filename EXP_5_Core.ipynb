{
  "nbformat": 4,
  "nbformat_minor": 0,
  "metadata": {
    "colab": {
      "provenance": []
    },
    "kernelspec": {
      "name": "python3",
      "display_name": "Python 3"
    },
    "language_info": {
      "name": "python"
    }
  },
  "cells": [
    {
      "cell_type": "code",
      "execution_count": 1,
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "x5UlibbvTytJ",
        "outputId": "4fe282bb-bed0-41e9-dc15-cfa6fcb2c590"
      },
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "Downloading data from https://storage.googleapis.com/tensorflow/tf-keras-datasets/imdb.npz\n",
            "\u001b[1m17464789/17464789\u001b[0m \u001b[32m━━━━━━━━━━━━━━━━━━━━\u001b[0m\u001b[37m\u001b[0m \u001b[1m1s\u001b[0m 0us/step\n",
            "Epoch 1/5\n"
          ]
        },
        {
          "output_type": "stream",
          "name": "stderr",
          "text": [
            "/usr/local/lib/python3.12/dist-packages/keras/src/layers/core/embedding.py:97: UserWarning: Argument `input_length` is deprecated. Just remove it.\n",
            "  warnings.warn(\n"
          ]
        },
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "\u001b[1m313/313\u001b[0m \u001b[32m━━━━━━━━━━━━━━━━━━━━\u001b[0m\u001b[37m\u001b[0m \u001b[1m52s\u001b[0m 158ms/step - accuracy: 0.6562 - loss: 0.6014 - val_accuracy: 0.8354 - val_loss: 0.3919\n",
            "Epoch 2/5\n",
            "\u001b[1m313/313\u001b[0m \u001b[32m━━━━━━━━━━━━━━━━━━━━\u001b[0m\u001b[37m\u001b[0m \u001b[1m82s\u001b[0m 160ms/step - accuracy: 0.8825 - loss: 0.2964 - val_accuracy: 0.8454 - val_loss: 0.3654\n",
            "Epoch 3/5\n",
            "\u001b[1m313/313\u001b[0m \u001b[32m━━━━━━━━━━━━━━━━━━━━\u001b[0m\u001b[37m\u001b[0m \u001b[1m82s\u001b[0m 161ms/step - accuracy: 0.9185 - loss: 0.2202 - val_accuracy: 0.8414 - val_loss: 0.3884\n",
            "Epoch 4/5\n",
            "\u001b[1m313/313\u001b[0m \u001b[32m━━━━━━━━━━━━━━━━━━━━\u001b[0m\u001b[37m\u001b[0m \u001b[1m50s\u001b[0m 161ms/step - accuracy: 0.9449 - loss: 0.1581 - val_accuracy: 0.8384 - val_loss: 0.4298\n",
            "Epoch 5/5\n",
            "\u001b[1m313/313\u001b[0m \u001b[32m━━━━━━━━━━━━━━━━━━━━\u001b[0m\u001b[37m\u001b[0m \u001b[1m80s\u001b[0m 154ms/step - accuracy: 0.9578 - loss: 0.1219 - val_accuracy: 0.8284 - val_loss: 0.4803\n"
          ]
        },
        {
          "output_type": "execute_result",
          "data": {
            "text/plain": [
              "<keras.src.callbacks.history.History at 0x79ee369fb8c0>"
            ]
          },
          "metadata": {},
          "execution_count": 1
        }
      ],
      "source": [
        "from keras.datasets import imdb\n",
        "from keras.models import Sequential\n",
        "from keras.layers import Embedding, LSTM, Dense\n",
        "from keras.preprocessing.sequence import pad_sequences\n",
        "# Load dataset\n",
        "(X_train, y_train), (X_test, y_test) = imdb.load_data(num_words=10000)\n",
        "X_train = pad_sequences(X_train, maxlen=100)\n",
        "X_test = pad_sequences(X_test, maxlen=100)\n",
        "# Model\n",
        "model = Sequential([\n",
        "Embedding(10000, 32, input_length=100),\n",
        "LSTM(100),\n",
        "Dense(1, activation='sigmoid')\n",
        "])\n",
        "model.compile(loss='binary_crossentropy', optimizer='adam', metrics=['accuracy'])\n",
        "model.fit(X_train, y_train, epochs=5, batch_size=64, validation_split=0.2)"
      ]
    }
  ]
}
