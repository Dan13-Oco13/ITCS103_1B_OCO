word = input("Enter a word: ")

word_length = len(word)

numbers = []
print(f"Enter {word_length} numbers:")

for i in range(word_length):
    num = float(input(f"Number {i + 1}: "))
    numbers.append(num)

def compute_average(num_list):
    return sum(num_list) / len(num_list)

def compare_length_and_average(length, average):
    if length > average:
        return "The word length is GREATER than the average."
    elif length < average:
        return "The word length is LESS than the average."
    else:
        return "The word length is EQUAL to the average."

average = compute_average(numbers)

result = compare_length_and_average(word_length, average)

print("\n--- Results ---")
print("List of numbers entered:", numbers)
print("Length of the word:", word_length)
print("Average of the numbers:", average)
print(result)
