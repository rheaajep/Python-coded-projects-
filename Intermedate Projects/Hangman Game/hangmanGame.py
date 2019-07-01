import pygame 
pygame.init()

gameScreen_width=3000
gameScreen_height=3000
white=(255,255,255)
black=(0,0,0)
blue=(0,0,255)
green=(0,255,0)


vowels=["a","e","i","o","u"]


guesses_one=0
guesses_two=0
guesses_three=0
guesses_four=0
guesses_five=0
guesses_six=0

gameScreen=pygame.display.set_mode((gameScreen_width,gameScreen_height))
pygame.display.set_caption('HangMan')

clock=pygame.time.Clock()
gameExit=False

hangMan_Image=pygame.image.load('/home/geekerlink/Desktop/hangman_stand.png')


def hangMan_Upload(x,y):
    gameScreen.blit(hangMan_Image,(x,y))

def hangMan_Head(guesses_one):
    if guesses_one == 1 :
        pygame.draw.circle(gameScreen,blue,(1100,300),90)

def hangMan_Body(guesses_two):
    if guesses_two == 2 :
        pygame.draw.line(gameScreen,blue,(1100,320),(1100,650),5)

def hangMan_RightLeg(guesses_three):
    if guesses_three == 3:
        pygame.draw.line(gameScreen,blue,(1100,650),(900,800),5)

def hangMan_LeftLeg(guesses_four):
    if guesses_four == 4:
        pygame.draw.line(gameScreen,blue,(1100,650),(1300,800),5)

def hangMan_LeftHand(guesses_five):
    if guesses_five == 5:
        pygame.draw.line(gameScreen,blue,(1100,500),(900,350),5)

def hangMan_RightHand(guesses_six):
    if guesses_six == 6:
        pygame.draw.line(gameScreen,blue,(1100,500),(1300,350),5)

def blank_words(length_of_word,words):
    blank_xstart=1700
    blank_xfinish=1770
    for num in range(0,length_of_word):
        pygame.draw.line(gameScreen,black,(blank_xstart,1400),(blank_xfinish,1400),5)
        if blank_xfinish>=2950 and blank_xfinish<=3000:
            blank_xfinish=1700-50
            blank_xstart=blank_xfinish-70
        elif blank_xstart<1700:
            blank_xfinish=blank_xstart-50
            blank_xstart=blank_xfinish-70
        else:
            blank_xstart=blank_xfinish+50
            blank_xfinish=blank_xstart+70
    if blank_xstart<1700:
        blank_xstart=blank_xfinish+50
        blank_xfinish=blank_xstart+70
    else:
        blank_xstart=1700
        blank_xfinish=1770

    for num in range(0,length_of_word):
        if words[num] in vowels:
            pygame.draw.line(gameScreen,black,(blank_xstart,1430),(blank_xfinish,1470),5)
            pygame.draw.line(gameScreen,black,(blank_xfinish,1430),(blank_xstart,1470),5)
        
        blank_xstart=blank_xfinish+50
        blank_xfinish=blank_xstart+70



while not gameExit:
    
    words="anaemia"
    length_of_word=len(words)
    
    

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            gameExit=True

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_h:
                guesses_one=1

            if event.key == pygame.K_t:
                guesses_two=2

            if event.key == pygame.K_r:
                guesses_three=3
                

            if event.key == pygame.K_l:
                guesses_four=4
                
            if event.key == pygame.K_a:
                guesses_five=5
                

            if event.key == pygame.K_j:
                guesses_six=6
                


            

    x=gameScreen_width *0.1
    y=gameScreen_height*0.1

    
    gameScreen.fill(white)
    hangMan_Upload(x,y)
    hangMan_Head(guesses_one)
    hangMan_Body(guesses_two)
    hangMan_RightLeg(guesses_three)
    hangMan_LeftLeg(guesses_four)
    hangMan_LeftHand(guesses_five)
    hangMan_RightHand(guesses_six)
    blank_words(length_of_word,words)
    
    pygame.display.update()
    clock.tick(60)


pygame.quit()
quit()