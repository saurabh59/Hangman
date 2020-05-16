import random
word_list = ['python', 'java', 'kotlin', 'javascript']
word = random.choice(word_list)
word_char = list(word)
blanks = len(word_char) * '-'
blanks_list = list(blanks)
print("H A N G M A N")
lives = 8
user_list = []
print('Type "play" to play the game, "exit" to quit:')
menu = input()
while menu != "exit":
    if menu == "play":
        while lives > 0:
            print()
            print("".join(blanks_list))
            user_input = input("Input a letter:")
            if len(user_input) == 1:
                if user_input.islower():
                    if user_input.isalpha():
                        if user_input not in user_list:
                            if user_input in word_char:
                                indices_list = []
                                s = 0
                                for x in word_char:
                                    if x == user_input:
                                        indices_list.append(s)
                                    s += 1
                                for y in indices_list:
                                    blanks_list[y] = word_char[y]
                                if blanks_list == word_char:
                                    print("".join(blanks_list))
                                    print("You guessed the word!")
                                    print("You survived!")
                                    break
                            else:
                                lives -= 1
                                if lives > 0:
                                    print("No such letter in the word")
                                else:
                                    print("No such letter in the word")
                                    print("You are hanged!")
                                    break
                        else:
                            print("You already typed this letter")
                        user_list.append(user_input)
                else:
                    print("It is not an ASCII lowercase letter")
            else:
                print("You should print a single letter")
    print()
    print('Type "play" to play the game, "exit" to quit')
    menu = input()
