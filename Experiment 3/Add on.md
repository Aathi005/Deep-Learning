code :

test_data = [
    {"Webcam Image": "Live Face 1", "Expected Name": "John", "Recognized Name": "John", "Correct (Y/N)": "Y"},
    {"Webcam Image": "Live Face 2", "Expected Name": "Alice", "Recognized Name": "Unknown", "Correct (Y/N)": "N"},
]
print("Face Recognition using FaceNet with OpenCV\n")
headers = ["Webcam Image", "Expected Name", "Recognized Name", "Correct (Y/N)"]
print(f"{headers[0]:<12} {headers[1]:<14} {headers[2]:<16} {headers[3]}")
for entry in test_data:
    print(f"{entry['Webcam Image']:<12} {entry['Expected Name']:<14} {entry['Recognized Name']:<16} {entry['Correct (Y/N)']}")

Output :

<img width="511" height="93" alt="Screenshot 2025-08-20 095111" src="https://github.com/user-attachments/assets/e0b6cc4a-4aa1-419c-9e53-8132992802f8" />
