def main():
    print("\nThis program is an implementation of the Rosenberg")
    print("Self-Esteem Scale. This program will show you ten")
    print("statements that you could possibly apply to yourself.")
    print("Please rate how much you agree with each of the")
    print("statements by responding with one of these four letters:\n")
    print("D means you strongly disagree with the statement.")
    print("d means you disagree with the statement.")
    print("a means you agree with the statement.")
    print("A means you strongly agree with the statement.\n")
    print("1. I feel that I am a person of worth, at least on an")
    print("equal plane with others.")
    ans1 = input("Enter D, d, a, or A: ")
    print("2. I feel that I have a number of good qualities.")
    ans2 = input("Enter D, d, a, or A: ")
    print("3. All in all, I am inclined to feel that I am a failure.")
    ans3 = input("Enter D, d, a, or A: ")
    print("4. I am able to do things as well as most other people.")
    ans4 = input("Enter D, d, a, or A: ")
    print("5. I feel I do not have much to be proud of.")
    ans5 = input("Enter D, d, a, or A: ")
    print("6. I take a positive attitude toward myself.")
    ans6 = input("Enter D, d, a, or A: ")
    print("7. On the whole, I am satisfied with myself.")
    ans7 = input("Enter D, d, a, or A: ")
    print("8. I wish I could have more respect for myself.")
    ans8 = input("Enter D, d, a, or A: ")
    print("9. I certainly feel useless at times.")
    ans9 = input("Enter D, d, a, or A: ")
    print("10. At times I think I am no good at all.")
    ans10 = input("Enter D, d, a, or A: ")

    one = positiveQuestions(ans1)
    two = positiveQuestions(ans2)
    four = positiveQuestions(ans4)
    six = positiveQuestions(ans6)
    seven = positiveQuestions(ans7)

    three = negativeQuestions(ans3)
    five = negativeQuestions(ans5)
    eight = negativeQuestions(ans8)
    nine = negativeQuestions(ans9)
    ten = negativeQuestions(ans10)

    score = one + two + four + six + seven + three + five + eight + nine + ten

    print(f"Your score is {score}")
    print("A score below 15 may indicate problematic low self-esteem.\n")


def positiveQuestions(answer):
    points = 0
    if answer == "D":
        points = 0
    elif answer == "d":
        points = 1
    elif answer == "a":
        points = 2
    elif answer == "A":
        points = 3

    return points


def negativeQuestions(answer):
    points = 0
    if answer == "D":
        points = 3
    elif answer == "d":
        points = 2
    elif answer == "a":
        points = 1
    elif answer == "A":
        points = 0

    return points


if __name__ == "__main__":
    main()
