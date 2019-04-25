#!/usr/bin/env python
# coding: utf-8

# In[ ]:





# In[ ]:


import random
print('Welcome to hangman, lets begin the guessing game') 
words=['bungler','bagpipe','dwarves','awkward','faking','equip','buffoon','oxygen','rhythm']
continueMoving="yes"
while continueMoving=='yes':
    hangmanWord=random.choice(words)
    lengthWord=len(hangmanWord)
    #print(hangmanWord)
    hangmanWord_dict=[_]*lengthWord
    #print(lengthWord)
    print("it is a ",lengthWord,"letter word")
    print("you get 4 guesses")
    done=0
    NumberofGuesses=4
    failedGuesses=[]
    while NumberofGuesses>0 and done==0:
        guessedLetter=input("Guess your letter: ")
        if len(guessedLetter)==1:
            if guessedLetter in hangmanWord_dict:
                print("you already guessed that letter")
            elif guessedLetter in hangmanWord:
                count=hangmanWord.count(guessedLetter)
                #print(count)
                start=0
                for i in range(0,count):
                    a=hangmanWord.find(guessedLetter,start)
                    hangmanWord_dict[a]=guessedLetter
                    print(hangmanWord_dict)
                    i=i+1
                    start=a+1
                    #print("start:",start)
            elif guessedLetter in failedGuesses:
                print("you already made a wrong guess on that letter")
            else:
                    print("It was a wrong guess")
                    NumberofGuesses=NumberofGuesses-1
                    print("you have ",NumberofGuesses,"guesses left")
                    failedGuesses.append(guessedLetter)
            if '' not in hangmanWord_dict:
                    done=1
        else:
            print("it is not a single alphabet, input your guess again")
    if done==1:
        print("you guessed the right word and that is ",hangmanWord)
    
    else:
        print("sorry, you lost the game")
        print("the word is: ",hangmanWord)
    
    continueMoving=input("would you like to play again: ")

        


# In[ ]:





# In[ ]:




