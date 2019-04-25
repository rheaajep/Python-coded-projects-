#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import random 
response='yes'
print("let's play a guessing game")
while response=='yes'or'YES'or'Yes':
    print("I have a number on my mind between 1 to 20\ncan you guess what that number is")
    number=random.randint(1,20)
    guess_taken=0
    guessed=0
    while guess_taken<4 and guessed==0:
        guess=input()
        value=guess.isdigit()
        if value==1:
            num=int(guess)
            if num>=1 and num<=20:
                difference=num-number
                if difference==0:
                    print("that's a correct guess, well done, you guessed it right in",guess_taken,"guess")
                    guessed=1
                elif difference>0:
                    print("your guess is high")
                    guess_taken=guess_taken+1
                else:
                    print("your guess is low")
                    guess_taken=guess_taken+1
            else:
                print("the number is not within the range")
        else:
            print("error: your input is not an integer")
    if guessed==0:
        print("Sorry, the guesses were wrong, the real number is ",number)
    response=input("do you wish to continue: ")


# In[ ]:





# In[ ]:





# In[ ]:




