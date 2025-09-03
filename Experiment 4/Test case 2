code :

import numpy as np
import tensorflow as tf
from tensorflow.keras.preprocessing.text import Tokenizer
from tensorflow.keras.preprocessing.sequence import pad_sequences
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Embedding, LSTM, Dense
text = """
To be or not to be that is the question
What light through yonder window breaks
"""
text = text.lower()
tokenizer = Tokenizer()
tokenizer.fit_on_texts([text])
total_words = len(tokenizer.word_index) + 1
input_sequences = []
token_list = tokenizer.texts_to_sequences([text])[0]
for i in range(1, len(token_list)):
    n_gram_seq = token_list[:i+1]
    input_sequences.append(n_gram_seq)
max_seq_len = max(len(seq) for seq in input_sequences)
input_sequences = pad_sequences(input_sequences, maxlen=max_seq_len, padding='pre')
input_sequences = np.array(input_sequences)
X = input_sequences[:, :-1]
y = input_sequences[:, -1]
y = tf.keras.utils.to_categorical(y, num_classes=total_words)
model = Sequential()
model.add(Embedding(total_words, 10, input_length=max_seq_len - 1))
model.add(LSTM(100))
model.add(Dense(total_words, activation='softmax'))
model.compile(loss='categorical_crossentropy', optimizer='adam', metrics=['accuracy'])
model.fit(X, y, epochs=200, verbose=0)
def predict_next_word(model, tokenizer, text, max_seq_len):
    sequence = tokenizer.texts_to_sequences([text.lower()])[0]
    sequence = pad_sequences([sequence], maxlen=max_seq_len - 1, padding='pre')
    pred = model.predict(sequence, verbose=0)
    predicted_index = np.argmax(pred, axis=1)[0]
    for word, index in tokenizer.word_index.items():
        if index == predicted_index:
            return word
    return None
test_inputs = [
    "To be or not",
    "What light through yonder window"
]
for test_input in test_inputs:
    next_word = predict_next_word(model, tokenizer, test_input, max_seq_len)
    print(f"Input Sequence: '{test_input}' -> Predicted Word: '{next_word}'")

output :

<img width="623" height="58" alt="Screenshot 2025-09-03 110958" src="https://github.com/user-attachments/assets/248ddf64-3131-453c-ae68-034cee7b838c" />
