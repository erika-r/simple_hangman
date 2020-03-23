
import random

with open("text.txt", "r") as f:
    f = f.readlines()

word_index = random.randint(0,len(f))
word = f[word_index].strip()

#possible_attempts = 6
wrong_attempts = 6
print("The word is {} letters long.".format(len(word)))
guesses = ["*"] * len(word)
print("".join(guesses))

while wrong_attempts != 0 and "".join(guesses) != word:  #only wrong amounts possible
    guess = input("Enter a letter:")

    if guess.casefold() not in word:
        wrong_attempts -= 1
        print("Wrong, guess again. Attempts left ({})".format(wrong_attempts))
        print("".join(guesses))
    elif guess.casefold() in word:
        print("Good guess ;) Attempts left ({})".format(wrong_attempts))
        for i in range(len(word)):
            if word[i] == guess.casefold():
                guesses[i] = word[i]
        print("".join(guesses))

    if "".join(guesses) == word:
        print("You win, the word was '{}'.".format(word))
        break
    if wrong_attempts == 0:     #amount of body parts
        print("You lose, the word was '{}'.".format(word))

