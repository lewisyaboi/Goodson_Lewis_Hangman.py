import random
file = open("word_list.txt")
content = file.readlines()
new_content = [x[:-1] for x in content]

word = random.choice(new_content)
length = len(word)
lives = 7
blanks = '*' * length
letters = 0
win = False

while True:
    print(blanks, '\t\tLives: ', lives, '\n')
    guess = input('Please enter your next guess:')

    if guess in blanks:
        print('Letter already guessed\n')

    elif guess in word:
        print ('Correct!\n')
        letters = letters + 1

    elif guess not in word:
        print ('Wrong!\n')
        lives = lives - 1
        if lives == 0:
            break

    for i in range(len(word)):  # replace blanks with correct guessed letters
        if word[i] in guess:
            blanks = blanks[:i] + word[i] + blanks[i+1:]

    if letters == length:
        print('You Lose')
        break
    if '*' not in blanks:
        print('Congratulations You Win')
        break
