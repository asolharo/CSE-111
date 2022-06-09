import random


def main():
    numbers = [16.2, 75.1, 52.3]
    print(f"numbers {numbers}")

    # Append new number and print list again
    append_random_numbers(numbers)
    print(f"numbers {numbers}")

    # Append 3 numbers and print
    append_random_numbers(numbers, 3)

    words = []
    append_random_word(words, 6)
    print(f"words {words}")


def append_random_numbers(numbers_list, quantity=1):
    for i in range(quantity):
        random_number = random.uniform(0, 100)
        rounded = round(random_number, 1)
        numbers_list.append(rounded)


def append_random_word(words_list, quantity=1):
    words = ["keyboard", "mouse", "monitor", "fan", "cup", "car",
             "controller", "glasses", "book", "console", "bottle"]
    for i in range(quantity):
        word = random.choice(words)
        words_list.append(word)


if __name__ == "__main__":
    main()
