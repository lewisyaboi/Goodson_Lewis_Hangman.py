import random
import time
file = open("word_list.txt")
content = file.readlines()
new_content = [x[:-1] for x in content]

word = random.choice(new_content)
length = len(word)
lives = 7
blanks = '*' * length
letters = 0
lists = ['']
win = False

while True:
    print(blanks, '\t\tLives: ', lives, '\n')
    guess = input('Please enter your next guess:')

    if guess in lists:
        print('Letter already guessed\n')
    else:
        if guess in word:
            print ('Correct!\n')
            letters = letters + 1
        if guess not in word:
            print ('Wrong!\n')
            lives = lives - 1
    lists.append(guess)
    
    for i in range(len(word)):  # replace blanks with correct guessed letters
        if word[i] in guess:
            blanks = blanks[:i] + word[i] + blanks[i+1:]

    if lives == 0:
        print('The original word was:', word)
        print('You Lose')
        break
    if '*' not in blanks:
        print('Congratulations You Win')
        break
