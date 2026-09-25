import random

def number_guessing_game():
    print("\n--- Number Guessing Game ---")
    secret_number = random.randint(1, 100)
    attempts = 0
    print("I have chosen a number between 1 and 100. Try to guess it!")
    
    while True:
        try:
            guess = int(input("Enter your guess: "))
            attempts += 1
            if guess < secret_number:
                print("Too low! Try again.")
            elif guess > secret_number:
                print("Too high! Try again.")
            else:
                print(f"Congratulations! You found the number in {attempts} attempts.")
                score = max(100 - (attempts - 1) * 10, 10) # Scoring system
                print(f"Your Score: {score}/100")
                break
        except ValueError:
            print("Invalid input. Please enter a valid integer.")

def word_counter():
    print("\n--- File-Based Word Counter Tool ---")
    filename = input("Enter the filename to read (e.g., sample.txt): ")
    
    try:
        with open(filename, 'r') as file:
            text = file.read()
            words = text.split()
            word_count = len(words)
            
            # Word frequency analysis
            frequency = {}
            for word in words:
                word_clean = word.lower().strip(".,!?()[]{}\"''")
                frequency[word_clean] = frequency.get(word_clean, 0) + 1
                
            print(f"\nTotal words in '{filename}': {word_count}")
            print("Top frequent words:")
            sorted_words = sorted(frequency.items(), key=lambda x: x[1], reverse=True)
            for word, count in sorted_words[:5]:
                print(f"  - '{word}': {count} time(s)")
                
    except FileNotFoundError:
        print(f"Error: The file '{filename}' was not found. Let's create a sample file for you.")
        with open(filename, 'w') as f:
            f.write("Python programming is fun. Python is powerful and easy to learn.")
        print(f"Created '{filename}' with sample text. Run the word counter again to test it!")

def main():
    while True:
        print("\n=== InternCircle Task 2 Menu ===")
        print("1. Play Number Guessing Game")
        print("2. Run Word Counter Tool")
        print("3. Exit")
        
        choice = input("Enter your choice (1-3): ")
        if choice == '1':
            number_guessing_game()
        elif choice == '2':
            word_counter()
        elif choice == '3':
            print("Exiting program. Good luck with your submission!")
            break
        else:
            print("Invalid choice. Please enter 1, 2, or 3.")

if __name__ == "__main__":
    main()
