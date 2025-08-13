#Test case 1
test_cases = [
    ([0, 0], 0),
    ([0, 1], 1),
    ([1, 0], 1),
    ([1, 1], 0)
]
def xor(a, b):
    return a ^ b  # Bitwise XOR
for X, expected in test_cases: 
    result = xor(X[0], X[1])
    print(f"Input: {X} -> Output: {result} (Expected: {expected})")

Output: 
<img width="658" height="348" alt="Screenshot 2025-08-13 113659" src="https://github.com/user-attachments/assets/b2c75660-2b5b-4f00-8777-b2748179a2da" />
