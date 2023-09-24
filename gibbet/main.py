import random


HANGMAN = ("0/8", "1/8", "2/8", "3/8", "4/8", "5/8", "6/8", "7/8")
MAX_WRONG = len(HANGMAN) - 1
WORDS = ("AWOKADO", "MAŁŻ", "ŻÓŁW")

word = random.choice(WORDS)
so_far = "-" * len(word)
wrong = 0
used = []

print("Witaj w grze 'Szubienica'.Powodzenia")

while wrong < MAX_WRONG and so_far != word:
    print(HANGMAN[wrong])
    print("\nWykorzystałeś już następujące litery:\n", used)
    print("\nNa razie zagadkowe słowo wygląda tak:\n", so_far)

    guess = input("\n\nWprowadź literę: ")
    guess = guess.upper()
    while guess in used:
        print("Już wykorzystałeś literę: ", guess)
        guess = input("Wprowadź literę: ")
        guess = guess.upper()

    used.append(guess)

    if guess in word:
        print("\nTak!", guess, "znajduje się w zagadkowym słowie!")

        new = ""
        for i in range(len(word)):
            if guess == word[i]:
                new += guess
            else:
                new += so_far[i]
        so_far = new
    else:
        print("\nNiestety,", guess, "nie występuje w zagadkowym słowie.")
        wrong += 1

if wrong == MAX_WRONG:
    print(HANGMAN[wrong])
    print("\nZostałeś powieszony!")
else:
    print("\nOdgadłeś!")

print("\nZagadkowe słowo to ", word)

input("\n\nAby zakończyć program, naciśnij klawisz Enter.")
