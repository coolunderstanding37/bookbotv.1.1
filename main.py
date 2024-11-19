from available_books import books

def main():
	print("Please choose a book to analyze:")
	for i, book in enumerate(books):
		print(f"{i+1}. {book}")
	choice = int(input("Enter the number of your choice: ")) - 1

# read selected book
	if 0 <= choice < len(books):
		with open(f"books/{books[choice]}") as f:
			file_contents = f.read()

		action_choice = input("Enter '1' to print the book, '2' for the word count, or '3' for character count: ")

		if action_choice == '1':
			print(file_contents)
		elif action_choice == '2':
			print(f"Word count: {number_of_words(file_contents)}.")
		elif action_choice == '3':
			char_counts = char_count(file_contents)
			sorted_chars = sorted(char_counts.items(), key=lambda item: item[1], reverse=True)
			for char, count in sorted_chars:
				print(f"The '{char}' character was found {count} times.")
		else:
			print("Invalid choice. Please select a valid option.")

	else:
		print("Invalid choice")

def char_count(book):
	char_dict = {}
	lower_case = book.lower()
	# iterate through characters and adding them to the count
	for char in lower_case:
		if char.isalpha():
			if char in char_dict:
				char_dict[char] += 1
			else:
				char_dict[char] = 1
	return char_dict

def number_of_words(book):
	words = book.split()
	return len(words)

if __name__ == "__main__":
	main()
