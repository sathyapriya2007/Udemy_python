import time

# Sentence for typing test
sentence = "Python is a powerful and easy to learn programming language"

print("Typing Speed Test")
print("------------------")
print("Type the following sentence:\n")
print(sentence)
print("\nPress Enter when you are ready...")
input()

# Start time
start_time = time.time()

# User input
typed_text = input("\nStart typing:\n")

# End time
end_time = time.time()

# Time taken
time_taken = end_time - start_time

# Word count
words = len(sentence.split())

# Calculate WPM
wpm = (words / time_taken) * 60

# Accuracy calculation
correct_chars = 0
for i in range(min(len(sentence), len(typed_text))):
    if sentence[i] == typed_text[i]:
        correct_chars += 1

accuracy = (correct_chars / len(sentence)) * 100

# Results
print("\nResults")
print("--------")
print(f"Time Taken : {time_taken:.2f} seconds")
print(f"Typing Speed : {wpm:.2f} WPM")
print(f"Accuracy : {accuracy:.2f}%")
