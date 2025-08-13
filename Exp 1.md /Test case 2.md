from keras.models import Sequential
from keras.layers import Dense
import numpy as np
X = np.array([[0, 0],
              [0, 1],
              [1, 0],
              [1, 1]])
Y = np.array([[0],
              [1],
              [1],
              [0]])
model = Sequential()
model.add(Dense(4, input_dim=2, activation='relu'))
model.add(Dense(1, activation='sigmoid'))
model.compile(loss='binary_crossentropy', optimizer='adam', metrics=['accuracy'])
model.fit(X, Y, epochs=1000, verbose=0)
loss, accuracy = model.evaluate(X, Y, verbose=0)
print(f"Training Accuracy: {accuracy * 100:.2f}%\n")
predictions = model.predict(X)

print("Test Input (X)    Expected Output (Y)    Predicted Output    Remarks")
for i, x in enumerate(X):
    predicted = 1 if predictions[i] > 0.5 else 0
    expected = Y[i][0]
    if expected == 0:
        remark = "Correct" if predicted == 0 else "May fail"
    else:
        remark = "Correct" if predicted == 1 else "May fail"
    print(f"{x}           {expected}                    {predicted}                {remark}")















Output:
<img width="1107" height="605" alt="Screenshot 2025-08-13 114325" src="https://github.com/user-attachments/assets/af0109d0-6f3d-4cfe-ada4-e0a2a23ae681" />
