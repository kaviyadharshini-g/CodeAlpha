import random
import hangstages
print("\n" "-----Welcome to Hangman Game-----")
name=input("\n" "Enter your name:")
print("Hello " + name +" Best of Luck")
print("\n" "------You have only 6 lives* so guess the word within 6 attempts -----")
words_list=["Apple","Butterfly","Cherry","Delicious","Earth","Computer","Tamil Nadu","Chennai"]
lives=6
chosen_word=random.choice(words_list)
print(chosen_word)
display=[]
for i in range (len(chosen_word)):
    display +='_'
print(display)
death=False
while not death:
    guessed_letter=input("Guess a letter: ")
    for position in range(len(chosen_word)):
        letter = chosen_word[position]
        if letter == guessed_letter:
            display[position]=guessed_letter
    print(display)        
    if guessed_letter not in chosen_word:
        lives -=1
        if lives ==0:
            death = True
            print("You lose the game!!!")


    if '_' not in display:
        death =True
        print("You Win the game!!!")
    print(hangstages.stages[lives])
